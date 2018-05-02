import pymysql
def database_opr(str):
    db = pymysql.connect(host='39.108.185.66', port=3306, user='root', db='dormitory_manage_system_database', password='1234',useUnicode=True)
    cursor = db.cursor()
    cursor.execute(str)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data