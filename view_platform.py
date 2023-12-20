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
    print("<br/>"+ "PLATFORM Table"+"<br/>" + res[0]+ "<br/>"+res[1]+ "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close() # close db    
except Exception as e:
        logging.error(traceback.format_exc())
