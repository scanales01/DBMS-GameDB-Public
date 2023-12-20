import sys
import traceback
import logging
import python_db


mysql_username = '' # please change to your username
mysql_password= ''  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    # res =python_db.executeSelect('SELECT NAME FROM DEVELOPER;')
    # res=res.split('\n')# split the header and data for printing
    # print("<br/>"+ "Developer List:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    # for i in range(len(res)-2):
    #     print(res[i+2]+"<br/>")
    # insert into item tables by getting the values passed from PHP
    NAME = sys.argv[1]
    val = "'" + NAME + "'"
    res = python_db.executeSelect('SELECT g.NAME, g.RELEASE_DATE, g.TOTAL_SALES, g.PLATFORM, p.MANUFACTURER, g.DEVELOPER, d.Games, d.Location FROM GAME g, DEVELOPER d, PLATFORM p WHERE TOTAL_SALES =(select MAX(TOTAL_SALES) FROM GAME where DEVELOPER = ' + val + ') and g.DEVELOPER = d.NAME AND g.PLATFORM = p.NAME;')
    res=res.split('\n')# split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>"+ ""+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
       print(res[i+2]+"<br/>")
    python_db.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc()) 