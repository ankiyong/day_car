import pymysql 
def make_db():
    conn = pymysql.connect(host='localhost', user='root', password='1234', charset='utf8')
    cursor = conn.cursor()

    sql = "CREATE DATABASE data"
    cursor.execute(sql)

    conn.commit()
    conn.close()


    conn = pymysql.connect(host='localhost', user='root', password='1234', db='data', charset='utf8')
    cursor = conn.cursor()

    sql = '''CREATE TABLE raw_data (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    brand varchar(200),
    name varchar(200),
    model varchar(200),
    trim varchar(200),
    fuel varchar(200),
    km int,
    year int,
    location varchar(20),
    price int,
    link varchar(2000),
    photo varchar(2000),
    color varchar(20),
    accident varchar(20)
    )
    '''

    cursor.execute(sql)

    conn.commit()
    conn.close()

    conn = pymysql.connect(host='localhost', user='root', password='1234', db='data', charset='utf8')
    cursor = conn.cursor()

    sql = '''CREATE TABLE news (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(2000),
    script text,
    link varchar(2000),
    media varchar(200),
    image varchar(2000)
    )
    '''

    cursor.execute(sql)

    conn.commit()
    conn.close()

