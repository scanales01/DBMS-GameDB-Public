import sys
import traceback
import logging
import python_db


mysql_username = '' # please change to your username
mysql_password= ''  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    res =python_db.executeSelect('SELECT * FROM GAME;')
    res=res.split('\n')# split the header and data for printing
    print("<br/>"+ "Table GAME before:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    # insert into item tables by getting the values passed from PHP
    ID = sys.argv[1]
    NAME = sys.argv[2]
    RELEASE_DATE = sys.argv[3]
    PLATFORM = sys.argv[4]
    DEVELOPER = sys.argv[5]
    GENRE = sys.argv[6]
    TOTAL_SALES = sys.argv[7]
    val = "'"+ ID + "','" + NAME + "'" + ", STR_TO_DATE('" + RELEASE_DATE + "','" + "%m/%d/%Y'),'" + PLATFORM + "','" + DEVELOPER +  "','" + GENRE + "','" + TOTAL_SALES + "'"
    python_db.insert("GAME",val)
    res =python_db.executeSelect('SELECT * FROM GAME;')
    res=res.split('\n')# split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>"+ "Table GAME after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())
