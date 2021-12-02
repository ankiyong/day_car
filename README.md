## Machine Learning 기반 중고차 가격 정보 제공 서비스 구축 프로젝트
---
## Description

Machine Learning과 Meta Search 기반의 중고차 가격 정보 제공 서비스 웹 페이지 구현


***
## ***Skill***

<div>
<img src='README.assets/Python-Symbol.png' width=200px >
<img src='README.assets/django.png' width=200px>
<br></br>
<img src='README.assets/BeautifulSoup.png' width=200px>
<img src='README.assets/pandas.jpeg' width=200px>
<br></br>
<br></br>
<img src='README.assets/vmware.jpeg' width=250px>
<img src='README.assets/aws.png' width=150px>
<br></br>
<br></br>
<img src='README.assets/mysql.png' width=200px>
<img src='README.assets/hadoop.png' width=200px>
<br></br>
<img src='README.assets/spark.png' width=200px>
</span>
</div>




## ***Role***
---

- 중고차 데이터 크롤링
- 데이터 전처리 및 가공
- DataBase 구축 및 설계
- 데이터 파이프라인 자동화
- 웹 페이지 구축
- AWS 개발환경 구축
- 웹 페이지 배포

<!-- 문구 수정 좀더 디테일하게 -->




# ***Outputs***

### **1. Django로 구현한 실제 웹 페이지**                   

##### 차량 가격 예측(판매) / 매물 정보 검색(구매) 페이지

<!-- 소소코드 링크 첨부하기 -->
    
[http://day-car.com](https://ankiyong.github.io/resume/#)
    

![README.assets/gif.gif](README.assets/gif.gif)

![README.assets/buy.gif](README.assets/buy.gif)


### **2. Dashboard**

- 수집한 데이터로 dashboard를 만들어 시각화 진행
    
![README.assets/dash.png](README.assets/dash.png)
    
    
    
### **3. 데이터 파이프라인**

**1. 수집**
   - BeautifulSoup을 사용하여 encar,kcar 사이트의 중고차 정보와 차량 관련 뉴스 데이터 크롤링
    ![README.assets/수집.png](README.assets/수집.png)
            
**2. 저장**
- Raw데이터 DB구축(추후 매물정보 제공에 사용)
            
    ![README.assets/DB.png](README.assets/DB.png)
            
    <!--  최종ERD 비교를위해 초기 ERD 첨부해도 좋음 -->
            
**3. 적재**

- Hadoop에 Raw 데이터 csv파일 적재

<!-- hadoop 처리 로직이나 설정관련  -->
  
**4. 전처리**
- Python에서 Spark session을 사용하여 Hadoop에 적재된 csv를 불러와 학습데이터로 가공
            
![README.assets/image-20211201174645562.png](README.assets/image-20211201174645562.png)
            

**5. 적재 및 저장**
- 학습데이터 csv파일을 Hadoop에 적재 및 Mysql에 학습데이터 DB구축
            
![README.assets/data.png](README.assets/data.png)
            
            
**6. 최종 ERD**
- 상단 2개 테이블은 컬럼명이 같지만 향후 업체별 검색기능 도입을 위해 테이블을 분리함
            
![README.assets/ERD.png](README.assets/ERD.png)
