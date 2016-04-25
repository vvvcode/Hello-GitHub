#coding=utf-8
from DBUtils import DBUtils

__author__ = 'liwei1'
#数据库执行sql测试 ：DBUtils(host,port,user,passwd,db,charset,sql_list)
sql_list=["select * from student where id = 1;",
          "INSERT INTO `daily_cost` ( `date`, `cost_content`, `cost_num`, `remark`) VALUES ('2016-04-25', '晚饭', '16', '');"]

DBUtils("localhost",3306,"root","","test","utf8",sql_list)