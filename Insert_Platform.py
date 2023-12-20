import sys
import traceback
import logging
import python_db


mysql_username = '' # please change to your username
mysql_password= ''  # please change to your MySQL password

try:
    python_db.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    res =python_db.executeSelect('SELECT * FROM PLATFORM;')
    res=res.split('\n')# split the header and data for printing
    print("<br/>"+ "Table PLATFORM before:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    # insert into item tables by getting the values passed from PHP
    #id= '17' # ID is unique, it needs to be changed for every insert
    NAME = sys.argv[1]
    RELEASE_DATE = sys.argv[2]
    MANUFACTURER = sys.argv[3]
    PREDECESSOR = sys.argv[4]
    SALES = sys.argv[5]
    val = "'"+ NAME + "'" + ", STR_TO_DATE('" + RELEASE_DATE + "','" + "%m/%d/%Y'),'" + MANUFACTURER + "','" + PREDECESSOR + "','" + SALES + "'"
    python_db.insert("PLATFORM",val)
    res =python_db.executeSelect('SELECT * FROM PLATFORM;')
    res=res.split('\n')# split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>"+ "Table PLATFORM after:"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())
