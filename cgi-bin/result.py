#!/usr/bin/env python

import cgi
import os
import sys
import MySQLdb
from mako.template import Template
from mako.lookup import TemplateLookup

def main():
    ## 
    print "Content-type: text/html\n"
    userId = 0
    totalShownCnt = 40
    totalLikeCnt = 0
    connector = MySQLdb.connect(host="localhost",db="research",user="root",passwd="")
    cursor = connector.cursor()


    ## request parameters
    form = cgi.FieldStorage()
    # page
    if form.has_key("likeCnt"):
        totalLikeCnt = form["likeCnt"].value


    ## calculate hit_ratio
    ratio = float(totalLikeCnt) / float(totalShownCnt)

    sql3 = "insert into hit_analyzed_ratio (user_id, like_cnt, ratio) values (" + str(userId) + ", " + str(totalLikeCnt) + ", " + str(ratio) + ")"
    print sql3
#    cursor.execute(sql3)


    ## data for view
    dirpath = os.path.dirname(os.path.abspath(__file__))
    t = Template(filename = dirpath + "/templates/result.html")
    data = {"userId": userId}
    html = t.render(**data)
    print html


main()
