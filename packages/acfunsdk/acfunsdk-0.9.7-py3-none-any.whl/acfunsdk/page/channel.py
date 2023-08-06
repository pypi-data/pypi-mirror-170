# coding=utf-8
from .utils import json, time, Bs
from .utils import AcSource, match1

__author__ = 'dolacmeo'


class BlockContent:
    raw_data = None

    def __init__(self, acer, raw_data: dict):
        self.acer = acer
        self.raw_data = raw_data

    def __repr__(self):
        if self.name:
            key = f"[{self.keyname}]" if self.keyname else ""
            return f"AcContent({self.name}{key})"
        return f"AcContent(#{self.blockId} Σ{self.contentCount})"

    @property
    def blockId(self):
        return self.raw_data.get('blockId')

    @property
    def name(self):
        return self.raw_data.get('name')

    @property
    def keyname(self):
        return self.raw_data.get('interfaceParameter', '').strip()

    @property
    def contentCount(self):
        return self.raw_data.get('contentCount')

    def list(self, obj: bool = True) -> (dict, None):
        if obj is False:
            return self.raw_data.get('webContents')
        data_list = list()
        for v in self.raw_data.get('webContents'):
            if v['mediaType'] == 0:
                data_list.append(self.acer.acfun.AcVideo(v['mediaId']))
            elif v['mediaType'] == 1:
                data_list.append(self.acer.acfun.AcArticle(v['mediaId']))
            elif v['mediaType'] == 2:
                data_list.append(self.acer.acfun.AcBangumi(v['mediaId']))
            elif v['mediaType'] == 4:
                data_list.append(self.acer.acfun.AcUp(v))
            elif v['mediaType'] == 8:
                data_list.append(self.acer.acfun.AcImage(v['image'], v['link'], v['title']))
        return data_list


class ChannelBlock:
    raw_data = None

    def __init__(self, acer, raw_data: dict):
        self.acer = acer
        self.raw_data = raw_data

    @property
    def name(self):
        return self.raw_data.get('name', '').strip()

    @property
    def blockType(self):
        return self.raw_data.get('blockType')

    def __repr__(self):
        return f"AcBlock(#{self.blockType} {self.name})"

    def list(self, obj: bool = True) -> (dict, None):
        if obj is False:
            return self.raw_data.get('content', [])
        return [BlockContent(self.acer, content) for content in self.raw_data.get('content', [])]


class AcChannel:
    page_obj = None
    raw_data = None
    nav_data = dict()
    parent_data = None
    sub_data = None
    is_main = False
    is_404 = False

    def __init__(self, acer, cid):
        self.acer = acer
        self.cid = str(cid)
        self.loading()

    @property
    def ctype(self):
        if self.is_404:
            return None
        if self.is_main:
            if self.cid != '63':
                return 'main'
            return 'wen'
        if self.parent_data['channelId'] == '63':
            return 'wen'
        return 'videos'

    @property
    def referer(self):
        return f"{AcSource.routes['index']}/v/list{self.cid}/index.htm"

    @property
    def _main_channels(self):
        return {x["channelId"]: x for x in AcSource.channel_data}

    @property
    def name(self):
        return self.nav_data.get('name')

    def __repr__(self):
        if self.is_404 is True:
            return f"AcChannel(#{self.cid} 404)"
        return f"AcChannel(#{self.cid} {self.name})"

    def _get_channel_info(self):
        for channel in AcSource.channel_data:
            if self.cid == channel['channelId']:
                self.nav_data = self.parent_data
                self.sub_data = channel["children"]
                break
            for sub in channel['children']:
                if self.cid == sub['channelId']:
                    self.parent_data = channel
                    self.nav_data = sub
                    break
        self.is_main = self.parent_data is None
        if self.nav_data is None:
            self.is_404 = True

    def loading(self):
        self._get_channel_info()
        if not self.is_main:
            return False
        page_req = self.acer.client.get(self.referer)
        self.page_obj = Bs(page_req.text, 'lxml')
        json_text = match1(page_req.text, r"(?s)__INITIAL_STATE__\s*=\s*(\{.*?\});")
        if json_text is None:
            self.is_404 = True
            return False
        self.raw_data = json.loads(json_text)

    def hot_words(self) -> (dict, None):
        if not self.is_main:
            return None
        return self.raw_data['channel']['hotWordList']

    def blocks(self):
        if not self.is_main:
            return None
        if self.cid == '63':
            return [ChannelBlock(self.acer, data) for data in self.raw_data['article']['blockList']]
        return [ChannelBlock(self.acer, data) for data in self.raw_data['channel']['blockList']]

    def ranks(self, limit: int = 50, date_range: str = None):
        if self.is_main:
            cid = int(self.cid)
            sub_cid = None
        else:
            cid = int(self.parent_data['channelId'])
            sub_cid = int(self.cid)
        return self.acer.acfun.AcRank(cid, sub_cid, limit, date_range=date_range)

    def articles(self) -> (dict, None):
        if self.ctype != 'wen':
            return None
        if self.cid == '63':
            return self.acer.acfun.AcWen()
        rids = list()
        for item in self.nav_data.get("realms", []):
            rids.append(item['realmId'])
        return self.acer.acfun.AcWen(rids)

    def videos(self,
               page: int = 1,
               sortby: [str, None] = None,
               duration: [str, None] = None,
               datein: [str, None] = None,
               obj: bool = True) -> (dict, None):
        if self.ctype != 'videos':
            return None
        sortby_list = {
            "rankScore": "综合",
            "createTime": "最新投稿",
            "viewCount": "播放最多",
            "commentCount": "评论最多",
            "bananaCount": "投蕉最多",
            "danmakuCount": "弹幕最多"
        }
        assert sortby in sortby_list or sortby is None
        duration_list = {
            "all": "全部",
            "0,5": "5分钟以下",
            "5,30": "5-30分钟",
            "30,60": "30-60分钟",
            "60,": "60分钟以上"
        }
        assert duration in duration_list or duration is None
        datein_list = {
            "default": "近三个月",
            "20200101,20210101": "2020",
            "20190101,20200101": "2019",
            "20180101,20190101": "2018",
            "20170101,20180101": "2017",
            "20160101,20170101": "2016",
            "20150101,20160101": "2015",
            "20100101,20150101": "2014-2010",
            ",20100101": "更早",
        }
        assert datein in datein_list or datein is None
        api_req = self.acer.client.get(self.referer, params={
            "sortField": "rankScore" if sortby is None else sortby,
            "duration": "all" if duration is None else duration,
            "date": "default" if datein is None else datein,
            "page": page,
            "quickViewId": "listwrapper",
            "reqID": 0,
            "ajaxpipe": 1,
            "t": str(time.time_ns())[:13]
        })
        assert api_req.text.endswith("/*<!-- fetch-stream -->*/")
        api_data = json.loads(api_req.text[:-25])
        api_obj = Bs(api_data.get('html', ''), 'lxml')
        v_datas = list()
        for item in api_obj.select('.list-content-item'):
            item_data = {
                'ac_num': item.select_one('.list-content-top').attrs['href'][5:],
                'title': item.select_one('.list-content-title').a.attrs['title'],
                'duration': item.select_one('.danmaku-mask .video-time').text,
                'commentCountShow': item.select_one('.list-content-data .commentCount').text,
                'viewCountShow': item.select_one('.list-content-data .viewCount').text,
                'coverUrl': item.select_one('.list-content-cover').attrs['src'],
                'user': {
                    'id': item.select_one('.list-content-uplink').attrs['data-uid'],
                    'name': item.select_one('.list-content-uplink').attrs['title'],
                }
            }
            if obj is True:
                v_datas.append(self.acer.acfun.AcVideo(item_data['ac_num'], item_data))
            else:
                v_datas.append(item_data)
        return v_datas
