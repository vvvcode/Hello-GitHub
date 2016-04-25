#coding=utf-8
import MySQLdb
__author__ = 'liwei1'

#链接数据库+执行sql
def DBUtils(host,port,user,passwd,db,charset,sql_list):
    #链接数据库,返回游标cursor
    conn=MySQLdb.connect(host=host,port=port,user=user,passwd=passwd,db=db,charset=charset)
    print "DB connect success!"
    cursor=conn.cursor()
    print "####sql execute start######"
    #执行sql,i 为执行条数count
    i=1
    for sql in sql_list:
        cursor.execute(sql)
        print "第%d条执行成功!####%s" %(i,sql)
    #执行sql结束
    print "####sql execute end#####"
    #sql执行结果
    for data in cursor.fetchall():
        for item in data:
            print item
    cursor.close()
    conn.commit()
    conn.close()


