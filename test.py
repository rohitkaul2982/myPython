#!/usr/bin/python

import MySQLdb
import pprint
# importing "array" for array operations
import array
#include "includefile.py"
# Open database connection
#db = MySQLdb.connect("192.168.6.52","application","s@myD#@mnl@sy","login_details")
db = MySQLdb.connect("172.29.67.215","application","s@myD#@mnl@sy","test")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sqlquery = "SELECT * from test.tbl_employee_info_log WHERE emptype!='3' and empcode!='' order by empcode limit 100";
# execute SQL query using execute() method.
cursor.execute(sqlquery)
arrEmp = {}
arrEmp2 = {}
# Fetch a single row using fetchone() method.
data = cursor.fetchall()
a=0
i=0;
for row in data:
    formatted_date = row[6].strftime('%Y-%m-%d %H:%M:%S')
    if arrEmp2.has_key(row[0]):
        i=i+1;
        arrEmp2[row[0]][formatted_date]={}
        arrEmp2[row[0]][formatted_date]['Teamtype']=row[8]
        arrEmp2[row[0]][formatted_date]['monthSel']=row[17]
        arrEmp2[row[0]][formatted_date]['count']=i
        arrEmp2[row[0]][formatted_date]['countA']=a
        a=a+i;
    else:
        arrEmp2[row[0]]={}
        i=0;

    arrEmp2[row[0]]['Teamtype']=row[8]
    arrEmp2[row[0]]['UpdateDateTime']=formatted_date
    arrEmp2[row[0]]['monthSel']=row[17]
    arrEmp2[row[0]]['countA']=a

    #for key in arrEmp[row[0]]:
    #    print "********"
    #    print(key)
    #    arrEmp[row[0]][row[3]] = row[2]

    #    print "********"
print (a)
print len(data)
print "********"
print len(arrEmp2)
pprint.pprint (arrEmp2);
    #exit
    #print "Datetime",row['datetime']
#pprint.pprint(arrEmp)
# disconnect from server
db.close()
