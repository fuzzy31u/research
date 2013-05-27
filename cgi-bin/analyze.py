#!/usr/bin/env python

import cgi
import os
import sys
import random
import MySQLdb
from mako.template import Template
from mako.lookup import TemplateLookup

## import my modules
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath+"/models")
from image import Image


def main():
    ## 
    print "Content-type: text/html\n"
    page = 1
    trialPageCnt = 10
    dispCntPerPage = 6
#    likeCnt = 0
    connector = MySQLdb.connect(host="localhost",db="research",user="root",passwd="")
    connector.autocommit(True)
    cursor = connector.cursor()


    ## request parameters
    form = cgi.FieldStorage()
    # userId
    if form.has_key("userId"):
        userId = form["userId"].value

    # page
    if form.has_key("page"):
        page = int(form["page"].value) + 1
    
    # like    
    if form.has_key("like"):
        likeCnt = form.getlist("like")
        for i in form.getlist("like"):
            likeCnt = int(likeCnt) + 1
            print likeCnt
    else:
        likeCnt = 0

    # list
#    if form.has_key("list"):
#        list = form.getlist("list")

    ## create total image data
    if page == 1:
        list = []
        sql1 = "select count(*) from genre"
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        totalShownCnt = int(result1[0][0]) * trialPageCnt

        # calculate ratio image count
        sql2 = "select * from result_ratio where user_id = " + str(userId)
        cursor.execute(sql2)
        result2 = cursor.fetchall()
        # ratio image count dictionary
        dict = {}
        for row in result2:
            cnt = totalShownCnt * row[3]
            dict[row[0]] = cnt
            # TODO: adjust so that just 40 OR 90


        # create ratio image list
        for k, v in dict.items():
            v = int(v)
            sql3 = "select * from history where shown_flg = 0 and user_id = " + str(userId) + " and genre_id = " + str(k) + " limit " + str(v)
            # TODO:if data is not enough amount, better to get also from shown_flg = 1?
            cursor.execute(sql3)
            result3 = cursor.fetchall()
            for row in result3:
                imageId = row[0]

                sql4 = "select file_name from image where id = " + str(imageId)
                cursor.execute(sql4)
                result4 = cursor.fetchall()
    
                name = result4[0][0]
           
                image = Image(imageId, name, k)
                list.append(image)

        random.shuffle(list)


        ## save list data temporary
        for l in list:
            sql5 = "insert into temp_analyzed_image values (" + str(l.id) + ", " + str(userId) + ", " + str(l.genreId) + ", '" + l.name + "')"
            cursor.execute(sql5)



    ## create display data
    dispList = []    
#    for i in range(dispCntPerPage):
#        print len(list)
#        if len(list) > 0:
#            dispList.append(list.pop())
    offset = dispCntPerPage * (page - 1)
    sql6 = "select * from temp_analyzed_image where user_id = " + str(userId) + " limit " + str(dispCntPerPage) + " offset " + str(offset)
    print sql6
    cursor.execute(sql6)
    result6 = cursor.fetchall()
    for row in result6:
        image = Image(row[0], row[3], row[2])
        dispList.append(image)


    ## data for view
    t = Template(filename = dirpath + "/templates/analyze.html")

 
#    ip = os.environ["REMOTE_ADDR"]
    ip = "localhost"
#    data = {"list": list, "ip": ip, "page": page, "likeCnt": likeCnt, "dispList": dispList, "userId": userId}
    data = {"ip": ip, "page": page, "likeCnt": likeCnt, "dispList": dispList, "userId": userId}

    html = t.render(**data)
    print html

main()
