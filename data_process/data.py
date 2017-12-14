# coding=utf-8
import MySQLdb
import re

class GetMissionItem(object):

    def __init__(self):
        self.host = '10.0.8.198'
        self.user = 'dashuju'
        self.password = '8FTeR5dA!'
        self.db = 'crawler'

        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db, charset='utf8')
        self.cursor = self.conn.cursor()
        self.url_list = []

    def get_lj_data(self):
        """
        获取小区均价种子
        :return:
        """
        try:
            self.cursor.execute("select id,floor from t_web_lj_deal_copy where total_floor is null")
            rs = self.cursor.fetchall()
            for line in rs:
                # print line
                item = dict()
                item['id'] = line[0]
                item['floor'] = line[1]
                self.url_list.append(item)
        except Exception, e:
            print e
        return self.url_list

    def process_data(self):
        for item in self.url_list:
            floor_string = item['floor'].split("(")
            item['floor'] = floor_string[0]
            item['total_floor'] = re.findall(r'\d+',floor_string[1])[0]
            try:
                self.cursor.execute("UPDATE t_web_lj_deal_copy AS a SET floor=%s, total_floor=%s WHERE total_floor is null AND a.id=%s",
                                    (item['floor'],item['total_floor'],item['id']))
                print (item['floor'], item['total_floor'], item['id'],'update successful')
                self.conn.commit()
            except Exception,e:
                print e

if __name__=='__main__':
    DataProcess = GetMissionItem()
    DataProcess.get_lj_data()
    DataProcess.process_data()