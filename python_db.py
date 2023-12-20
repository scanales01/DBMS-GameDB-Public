import mysql.connector
from tabulate import tabulate
           
def open_database (hostname,user_name,mysql_pw,database_name):
      global conn
      conn = mysql.connector.connect(
          host= hostname, 
          user = user_name,  
          password = mysql_pw, 
          database = database_name
        ) 
      global cursor
      cursor = conn.cursor() 

def printFormat(result):
    header=[]
    for cd in cursor.description:# get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    return(tabulate(result, headers=header))# print results in table format

# select and display query
def executeSelect (query):
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res
def  insert(table,values):
     query ="INSERT into " + table + " values (" + values + ")" +';'
     cursor.execute(query)
     conn.commit()


def executeUpdate(query): # use this function for delete and update
    cursor.execute(query)
    conn.commit()


def close_db ():  # use this function to close db
    cursor.close()
    conn.close()

##### Test #######
'''mysql_username = 'MYMYSQLUSERNAME' # please change to your MySQL username
mysql_password ='MYMYSQLPASSWORD'  # please change to your MySQL password
open_database('localhost',mysql_username,mysql_password,mysql_username) # open database   
executeSelect('SELECT * FROM ITEM'); # This is just a sample test, replace with your query
insert('ITEM',"22,'test',23.5,'M'")# This is just a sample test, replace with your query
executeSelect('SELECT * FROM ITEM where id = 22;')# checking if the value is updated
executeUpdate('delete from ITEM where id = 22;')# testing delete
executeSelect('SELECT * FROM ITEM where id = 22;')# checking if the id = 22 does not exist
executeUpdate("Update SUPPLIER set id = 20 where address ='Yemen';")# testing update
executeSelect("SELECT * FROM SUPPLIER where address = 'Yemen';")# checking the updated value
close_db()# close database'''







