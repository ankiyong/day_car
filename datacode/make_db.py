import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pymysql
#전처리 한 데이터를 db에 저장하는 코드

#spark session을 python으로 불러옴
def spark():
    spark = SparkSession\
        .builder\
        .master("yarn")\
        .appName("Python Spark SQL basic example")\
        .getOrCreate()

    df = spark.read.format("csv").option("header","true").load("all_csv.csv")
    return df
#spark sql을 사용하여 전처리 진행
def edit():
    df = spark()
    #wd 구분 추가
    df = df.withColumn("wd",when(col("model").contains("2WD"),lit(0)))
    df1 = df.fillna(1)

    #fuel 변경
    df1 = df1.na.replace({'LPG(일반인 구입)':'LPG','가솔린+전기':'하이브리드','디젤+전기':'하이브리드','가솔린+LPG':'바이퓨얼'})

    #color 변경
    df1 = df1.na.replace({'etc':'기타','black':'검정색','white':'흰색','gray':'회색'})

    #차량 이름 list
    car_n = ['그랜저', '쏘나타', '아반떼', '스타렉스', '싼타페', '제네시스', '투싼', '에쿠스', '크루즈', '코나', 'i3', '팰리세이드', '엑센트', '벨로스터', '쿠페', 'i40', '아슬란', '아이오닉', '갤로퍼', '쏠라티', '베뉴', '테라칸', '스타리아', '베르나', 'X4', '클릭', '투스카니', '넥쏘', '트라제', '다이너스티', '포니투', '레이', '마르샤', '티뷰론', '스텔라', '아토스', '뉴엘란트라', '라비타', '엑셀', '프레스토','카니발','카렌스','스포티지','니로','K3','K5','K7','K8','K9','모하비','오피러스','쏘렌토','스토닉','모닝','포르테','프라이드','쏘울','스팅어','레이','쎄라토','셀토스','로체','옵티마','SLS AMG','SLK-클래스','SLC-클래스','SL-클래스','GLK-클래스','GLE-클래스','GLS-클래스','스프린터','GL-클래스','GLB-클래스','GLC-클래스','GLA-클래스','CLS-클래스','CLA-클래스','CL-클래스','EQC','AMG GT','CLK-클래스','L-클래스','S-클래스','A-클래스','C-클래스','E-클래스','G-클래스','B-클래스','M-클래스','V-클래스','C-클래스','R-클래스','G-클래스','3시리즈', '7시리즈', 'M4', 'X5', 'X6', 'i3', '6시리즈', 'X4', 'M5', 'M3', 'Z4', 'X4M', 'X6M', '1시리즈',  'X2', 'M6', 'C4', 'X3', '5시리즈', '8시리즈', 'M8', '2시리즈','4시리즈', 'X1', 'M2', 'i8', 'X5M','스파크', '말리부', '크루즈', '올란도', '트랙스', '다마스', '라보', '마티즈', '알페온', '라세티', '임팔라', '레이', '캡티바', '윈스톰', '콜로라도', '토스카', '아베오', '트래버스', '볼트', '카마로', '이쿼녹스', '베리타스', '젠트라', '티코', '프린스', '매그너스', '스테이츠맨', '뉴프린스', '아카디아', 'G2X', '칼로스', '레조', '익스프레스밴', '콜벳', '서버밴', '실버라도', '체비밴', '기타', '아스트로밴', '콜로라도', '레이', 'S-10', '아발란치','SM5', 'SM6', 'SM3', 'SM7', '클리오', '마스터', '트위지', '캡처', '조에','티볼리', '코란도', '렉스턴', '체어맨', '액티언', '로디우스', '카이런', '무쏘 스포츠', '이스타나', '무쏘 밴', '무쏘','A6', 'A4', 'A7', 'A8', 'Q5', 'A5', 'Q7', '뉴 A3', 'Q3', 'S7', 'TT', 'R8', 'Q8', 'S6', 'S5', 'e-트론', 'S8', 'R8 (4S)', 'S3', 'S4', 'A1', 'Q2', '올로드 콰트로','G80', 'EQ900', 'G70', 'G90', 'GV80', 'GV70','쿠퍼', '로드스터', '원', '로버 미니','레인지로버', '디스커버리', '프리랜더', '디펜더','익스플로러', '머스탱', '토러스', 'F150', '몬데오', '포커스', '이스케이프', '퓨전', 'E-Series', 'F350', '쿠가', '익스페디션', '레인저', '파이브', 'S-MAX', '트랜짓','티구안', '골프', '폴로', 'GT', '투아렉 블루모션', '아테온', '파사트', '페이톤', '제타','골프 블루모션', '뉴 CC 블루모션', '비틀', 'CC', '제타 블루모션', '뉴 CC', '시로코',
    '티록','투아렉','CC 블루모션']

    df2 = df1.withColumn('name1',split(col("name")," "))
    df2 = df2.withColumn('name1',split(col("name")," "))
    df2 = df2.withColumn('name2',explode(col('name1')))
    df2 = df2.filter(col('name2').isin(car_n))


    #필요없는 컬럼 삭제
    df2 = df2.drop('name')
    df2 = df2.drop('name1')

    #필요한 컬럼만 새로운 변수에 담음
    df3 = df2.select("brand",col("name2").alias('name'),'trim','fuel','km','year','color','accident','wd','price')


    #쉐보레 수정
    df4 = df3.na.replace({"쉐보레(GM대우)":"쉐보레"})

    df5 = df4.na.replace({
        "x":'기본형',
        "(세부등급 없음)":"기본형",
        "프레스티지 ":"프레스티지",
        "VIP 패키지":"VIP",
        "일반형":"기본형",
        "베스트 셀렉션Ⅰ":"베스트 셀렉션",
        "프레스티지 에코플러스":"프레스티지",
        "프리미엄 플러스":"프리미엄",
        "최고급형 스페셜":"최고급형",
        "VIP PACK":"VIP",
        "최고급형 세이프티팩":"최고급형",
        "익스클루시브 스페셜":"익스클루시브",
        "프레스티지 스페셜 (5링크)":"프레스티지",
        "스마트 스페셜":"스마트",
        "프리미엄 스페셜":"프리미엄",
        "프레스티지 하이루프":"프레스티지",
        "스마트(렌터카용)":"스마트",
        "스패셜 팩":"스페셜",
        "파이오니어 X (리프)":"파이오니어 X",
        "GRX 고급형":"고급형",
        "프레스티지 (5링크)":"프레스티지",
        "프로페셔널 S (5링크)":"프로페셔널 S",
        "CVX 프리미엄":"프리미엄",
        "프로페셔널 X (5링크)":"프로페셔널 X",
        "LTZ 프리미엄 세이프티":"LTZ",
        "프레스티지 스페셜":"프레스티지",
        "개인형":"기본형",
        "노블레스 (5링크)":"노블레스",
        "플래티넘Ⅰ":"플레티넘",
        "다이내믹 에디션 (5링크)":"다이내믹 에디션",
        "프리미어 VIP":"VIP",
        "VIP팩":"VIP",
        "MX 노블레스":"노블레스",
        "TLX 스페셜":"TLX",
        "1 밀리언 얼티밋":"1 밀리언",
        "프레스티지 (리프)":"프레스티지",
        "노블레스 (리프)":"노블레스",
        "디럭스(블랙휠)":"디럭스",
        "GRX 일반형":"기본형",
        "스마트 기본형":"스마트",
        "노블레스 스페셜":"노블레스",
        "엘레강스 스페셜":"엘레강스",
        "럭셔리 스페셜":"럭셔리",
        "마제스티 스페셜":"마제스티",
        "MX 디럭스":"디럭스",
        "CVS 디럭스":"디럭스",
        "LT 코어":"LT",
        "프레스티지 (7인승)":"프레스티지",
        "베스트 셀렉션Ⅱ":"베스트 셀렉션",
        "베스트 셀렉션 Ⅱ":"베스트 셀렉션",
        "R-PLUS 화이트":"R-PLUS",
        "고급형 VIP 패키지":"고급형",
        "스타일 스페셜":"스타일",
        "5.0 프레스티지":"프레스티지",
        "럭셔리 그레이 에디션":"럭셔리",
        "세부등급 없음":"기본형",
        "고급형 블랙 스페셜":"고급형",
        "330i M 스포츠":"330i",
        "고급형 스페셜":"고급형",
        "파이오니어 S (리프)":"파이오니어 S"
        })
    # csv로 하둡에 저장
    df5.coalesce(1).write.format("csv").mode("overwrite").save("/user/engineer/uesdcar_info.csv")
    return df5

#전처리 데이터가 저장될 table 생성
def mkdb():
    db = pymysql.Connect(host='localhost',user='root',password='1234',database='data')
    cursor = db.cursor()
    query = '''CREATE TABLE learning_data(id INT AUTO_INCREMENT, 
                                       brand VARCHAR(200),
                                       name VARCHAR(200),
                                       trim VARCHAR(200),
                                       fuel VARCHAR(20),
                                       km INT,
                                       year INT,
                                       color VARCHAR(20),
                                       accident VARCHAR(20),
                                       wd INT,
                                       price INT,
                                       PRIMARY KEY(id)
                                       );
                                       '''
    cursor.execute(query)
    db.commit()

#전처리 데이터를 db에 저장
def savedb():
    mkdb()
    df5 = edit()
    #data 데이터 베이스의 encar 테이블과 연결
    user="root"
    password="1234"
    url="jdbc:mysql://localhost:3306/data"
    driver="com.mysql.cj.jdbc.Driver"
    dbtable="learning_data"
    #db에 저장
    df5.write.jdbc(url, dbtable, "append", properties={"driver": driver, "user": user, "password": password})
