# -*- coding: utf-8 -*-

import MySQLdb
import MySQLdb.cursors
import copy


class AliasPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host='10.0.8.198', user='dashuju', passwd='8FTeR5dA!', db='crawler', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item):
        asynitem = copy.deepcopy(item)
        self._conditional_insert(self.cursor, asynitem)

    def _conditional_insert(self, tb, item):
        try:
            tb.execute("update t_web_lj_xiaoqu set alias=%s where url=%s",
                       (item['alias'], item['url']))
            self.conn.commit()
            print("========== data update successful !!! ===========")
        except Exception, e:
            print e