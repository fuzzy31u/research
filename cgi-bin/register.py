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
    connector = MySQLdb.connect(host="localhost",db="research",user="root",passwd="")
    cursor = connector.cursor()


    ## request parameters
    form = cgi.FieldStorage()
    # name
    if form.has_key("name"):
        name = form["name"].value

    
        ## register user
        sql1 = "insert into user (name) values ('" + str(name) + "')"
        print sql1
        cursor.execute(sql1)
        connector.commit
        id = cursor.lastrowid
        print id

        ## register history data        
        sql2 = "select * from image"
        cursor.execute(sql2)
        result2 = cursor.fetchall()
        for row in result2:
            sql3 = "insert into history values (" + str(row[0]) + ", " + str(id) + ", " + str(row[1]) + ", 0)";
            print sql3
            cursor.execute(sql3)


    ## data for view
    dirpath = os.path.dirname(os.path.abspath(__file__))
    t = Template(filename = dirpath + "/templates/register.html")
    data = {"name": name, "id": id}
    html = t.render(**data)
    print html


main()
