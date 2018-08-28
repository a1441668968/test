import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tedu', charset='utf8')
cursor = conn.cursor()
insert_dep1 = 'insert into departments VALUES (%s,%s)'
delete1 = 'delete from departments WHERE dep_name=%s'
update_dep1 = 'update departments set dep_name=%s WHERE dep_name=%s'
cursor.execute(insert_dep1, ('1', '人事部'))
cursor.executemany(insert_dep1, [('2', '财务部'), ('3', '业务部'), ('4', '采购部'), ('5', '生产部')])
cursor.execute(update_dep1, ('人力资源部', '人事部'))
cursor.execute(delete1, ('人力资源部',))
conn.commit()
find='select * from departments'
cursor.execute(find)
result = cursor.fetchone()
cursor.scroll(1)
result2 = cursor.fetchmany(2)
cursor.scroll(0, mode='absolute')
result3 = cursor.fetchall()
print(result, result2, result3)
cursor.close()
conn.close()
