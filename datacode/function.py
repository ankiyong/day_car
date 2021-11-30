from . import encar,encar_for,kcar
import pymysql
a = encar.get_all()
b = encar_for.get_all()
c = kcar.all()


def save_db():
    car_db = pymysql.connect(
        user='root',
        passwd='0000',
        host='0.0.0.0',
        db='data',
        charset='utf8'
    )
    list = [a,b,c]
    for i in list:
        cursor = car_db.cursor(pymysql.cursors.DictCursor)
        info = i
        insert_data = sum(i, [])
        insert_sql2 = "INSERT INTO `kcar` VALUES (%(brand)s,%(name)s,%(info)s,%(type)s,%(km)s,%(year)s,%(location)s,%(price)s,%(link)s);"
        cursor.executemany(insert_sql2, insert_data)
        car_db.commit()
