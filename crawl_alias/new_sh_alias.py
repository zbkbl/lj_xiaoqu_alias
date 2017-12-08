# coding=utf-8

import json
from crawl_alias.getparam import GetMissionUrl
import requests
from crawl_alias.pipelines import AliasPipeline
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    'Host': 'sh.lianjia.com',
    'Referer': 'http://sh.lianjia.com/'
}

data = {
    'cityCode': 'sh',
    'pageType': 'xiaoqu',
    'keyword': ''
}


class Alias(object):

    def __init__(self):
        mission = GetMissionUrl()
        self.mission_list = mission.get_lj_param(u'上海')
        self.pipe = AliasPipeline()

    def get_alias(self):
        for item in self.mission_list:
            keyword = item['name']
            data['keyword'] = keyword
            res = requests.get(url='http://sh.lianjia.com/headerMind.json?', params=data, headers=header)
            result = json.loads(res.content)
            # print result

            try:
                result_dict = result['list'][0]
                alias = result_dict['remark']
                item['alias'] = alias
                self.pipe.process_item(item)
            except Exception, e:
                print e


if __name__ == "__main__":
    test = Alias()
    test.get_alias()