import os
import pymysql

#get username from workspace

username = os.getenv('C9_USER')

#connect to the datbase
connection = pymysql.connect(host='localhost',
                                user=username,
                                password='',
                                db='Chinook')


try:
    #Run a query
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close connection, regardless of whether the above was successful
    connection.close()

