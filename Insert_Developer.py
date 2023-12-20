import sys
import traceback
import logging
import python_db


mysql_username = '' # please change to your username
mysql_password= ''  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database

    res = python_db.executeSelect('SELECT * FROM DEVELOPER;')
    res = res.split('\n')# split the header and data for printing

    print("<br/>"+ "Table DEVELOPER before:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")

    # insert into item tables by getting the values passed from PHP
    NAME = sys.argv[1]
    CREATION = sys.argv[2]
    GAMES = sys.argv[3]
    Location = sys.argv[4]
    val = "'"+ NAME + "'" + ", STR_TO_DATE('" + CREATION + "','" + "%m/%d/%Y'),'" + GAMES + "','" + Location + "'"
    
    python_db.insert("DEVELOPER",val)

    res = python_db.executeSelect('SELECT * FROM DEVELOPER;')
    res = res.split('\n')# split the header and data for printing
    print("<br/>" + "<br/>")

    print("<br/>"+ "Table DEVELOPER after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")

    python_db.close() # close db  

except Exception as e:
        logging.error(traceback.format_exc())
