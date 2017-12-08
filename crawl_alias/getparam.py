# coding: utf-8
import MySQLdb
import MySQLdb.cursors

class GetMissionUrl(object):
    def __init__(self):
        self.host = '10.0.8.198'
        self.user = 'dashuju'
        self.password = '8FTeR5dA!'
        self.db = 'crawler'

        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db, charset='utf8')
        self.cursor = self.conn.cursor()
        self.url_list = []

    def get_lj_param(self, city):
        try:
            self.cursor.execute("select residence_name,url from t_web_lj_xiaoqu where city=%s and alias is null", (city,))
            rs = self.cursor.fetchall()
            for line in rs:
                item = dict()
                item['name'] = line[0]
                item['url'] = line[1]
                self.url_list.append(item)
        except Exception, e:
            print e
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        return self.url_list

if __name__=="__main__":
    test = GetMissionUrl()
    urls = test.get_lj_param()
    print len(urls)