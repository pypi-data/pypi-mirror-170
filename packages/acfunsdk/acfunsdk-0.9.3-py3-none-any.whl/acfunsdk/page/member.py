# coding=utf-8
from .utils import json, time, Bs
from .utils import AcSource

__author__ = 'dolacmeo'


class AcUp:
    resource_type = 5
    uid = None
    raw_data = None
    page_obj = None

    video_count = None
    article_count = None
    album_count = None
    following_count = None
    followed_count = None
    is_404 = False

    def __init__(self, acer, uid: [str, int], up_data: [dict, None] = None):
        self.uid = int(uid)
        self.raw_data = dict() if up_data is None else up_data
        self.acer = acer
        self._get_acup()

    def _get_acup(self):
        api_req = self.acer.client.get(AcSource.apis['userInfo'], params={"userId": self.uid})
        if api_req.json().get('result') != 0:
            self.is_404 = True
            return None
        self.raw_data.update(api_req.json().get('profile', {}))

    @property
    def name(self):
        if self.is_404:
            return None
        return self.raw_data.get('userName', self.raw_data.get('name'))

    @property
    def avatar(self):
        if self.is_404:
            return None
        return self.raw_data.get("headUrl")

    def __repr__(self):
        return f"Acer([#{self.uid}] @{self.name})".encode(errors='replace').decode()

    @property
    def referer(self):
        return f"{AcSource.routes['up']}{self.uid}"

    def loading(self):
        if self.is_404 is True:
            return None
        page_req = self.acer.client.get(AcSource.routes['up'] + self.uid)
        self.page_obj = Bs(page_req.text, "lxml")
        self.video_count = self.page_obj.select_one(
            '.ac-space-contribute-list > .tags > li[data-index=video]').attrs['data-count']
        self.article_count = self.page_obj.select_one(
            '.ac-space-contribute-list > .tags > li[data-index=article]').attrs['data-count']
        self.album_count = self.page_obj.select_one(
            '.ac-space-contribute-list > .tags > li[data-index=album]').attrs['data-count']
        self.following_count = self.page_obj.select_one(
            '.tab-list > li[data-index=following] > span').text
        self.followed_count = self.page_obj.select_one(
            '.tab-list > li[data-index=followed] > span').text

    def AcLive(self) -> object:
        return self.acer.acfun.AcLiveUp(self.uid)

    def follow_add(self, attention: [bool, None] = None):
        return self.acer.follow_add(self.uid, attention)

    def follow_remove(self):
        return self.acer.follow_remove(self.uid)

    def _get_data(self, viewer, page, limit, orderby) -> dict:
        viewers = ['video', 'article', 'album', 'following', 'followed']
        assert viewer in viewers
        orders = ['newest', 'hotest']
        assert orderby in orders
        param = {
            "reqID": viewers.index(viewer) + 1,
            "ajaxpipe": 1,
            "type": viewer,
            "page": page,
            "pageSize": limit,
            "t": str(time.time_ns())[:13]
        }
        if viewers.index(viewer) < 3:
            param.update({"quickViewId": f"ac-space-{viewer}-list", "order": orderby})
        else:
            param.update({"quickViewId": f"ac-space-{viewer}-user-list"})
        req = self.acer.client.get(AcSource.routes['up'] + self.uid, params=param)
        assert req.text.endswith("/*<!-- fetch-stream -->*/")
        return json.loads(req.text[:-25])

    def video(self, page=1, limit=10, orderby='newest') -> list:
        data = list()
        acer_data = self._get_data('video', page, limit, orderby)
        for item in Bs(acer_data.get('html', ''), 'lxml').select('a.ac-space-video'):
            ac_num = item.attrs['href'][5:]
            infos = {
                'title': item.select_one('p.title').attrs['title'],
                'dougaId': ac_num,
                'coverUrl': item.select_one('.video > img').attrs['src'],
                'createTime': item.select_one('p.date').text.replace('/', '-'),
                'user': self.raw_data
            }
            data.append(self.acer.acfun.AcVideo(ac_num, infos))
        return data

    def article(self, page=1, limit=10, orderby='newest') -> list:
        data = list()
        acer_data = self._get_data('article', page, limit, orderby)
        for item in Bs(acer_data.get('html', ''), 'lxml').select('.ac-space-article'):
            ac_num = item.a.attrs['href'][5:]
            infos = {
                'title': item.a.attrs['title'],
                'dougaId': ac_num,
                'user': self.raw_data
            }
            data.append(self.acer.acfun.AcArticle(ac_num, infos))
        return data

    def album(self, page=1, limit=10, orderby='newest') -> list:
        data = list()
        acer_data = self._get_data('album', page, limit, orderby)
        for item in Bs(acer_data.get('html', ''), 'lxml').select('.ac-space-album'):
            ac_num = item.a.attrs['href'][5:]
            data.append(self.acer.acfun.AcAlbum(ac_num))
        return data

    def _follow(self, key, page=1, limit=10, orderby='newest') -> list:
        assert key in ['following', 'followed']
        data = list()
        acer_data = self._get_data(key, page, limit, orderby)
        for item in Bs(acer_data.get('html', ''), 'lxml').select('li'):
            infos = {
                "id": item.select_one('div:nth-of-type(2) > a.name').attrs['href'][3:],
                "name": item.select_one('div:nth-of-type(2) > a.name').text
            }
            data.append(AcUp(self.acer, infos['id']))
        return data

    def following(self, page=1, limit=10, orderby='newest') -> list:
        return self._follow("following", page, limit, orderby)

    def followed(self, page=1, limit=10, orderby='newest') -> list:
        return self._follow("followed", page, limit, orderby)

    def report(self, crime: str, proof: str, description: str):
        return self.acer.acfun.AcReport.submit(
            self.referer, self.uid, self.resource_type,
            self.uid,
            crime, proof, description)
