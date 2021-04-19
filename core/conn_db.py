import pymysql

def get_reslut_by_sql(sql,index=0):
    CONNECT = pymysql.connect(host="0.0.0.1", port=3306, db="data_name", user="root", password="123456")
    cursor = CONNECT.cursor()
    cursor.execute(sql)
    reslut = cursor.fetchall()[index]  # 返回元组,查出多组数据时，加索引查要第几个
    return reslut