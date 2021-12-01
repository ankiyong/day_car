# Machine Learning 기반 서비스 구축 프로젝트
#### 1.Project

- 중고차 가격 정보 제공 서비스

#### 2. Description

- Machine Learning과 Meta Search 기반의 중고차 가격 정보 제공 서비스 웹 페이지 구현

#### 3. Role

- 중고차 데이터 크롤링
- 데이터 전처리
- DB구축
- 데이터 파이프라인 자동화
- 웹 페이지 구축
- AWS개발환경 구축
- 웹 페이지 배포

#### 4. Skill

<img src="README.assets/Python-Symbol.png" alt="image-20211201154258931" width="100"/> ![image-20211201154456902](README.assets/image-20211201154456902.png)![image-20211201154451673](README.assets/image-20211201154451673.png)    ![image-20211201154445748](README.assets/image-20211201154445748.png)![image-20211201154439609](README.assets/image-20211201154439609.png)

​     ![image-20211201154434847](README.assets/image-20211201154434847.png)          ![image-20211201154427757](README.assets/image-20211201154427757.png)         ![image-20211201154419520](README.assets/image-20211201154419520.png)    <img src="README.assets/image-20211201154311071.png" alt="image-20211201154311071" style="zoom: 67%;" />    ![image-20211201154401086](README.assets/image-20211201154401086.png)    

#### 5. Outputs

1. 차량 가격 예측(판매) / 매물 정보 검색(구매) 페이지

<img src="README.assets/gif.gif" alt="gif" width="475" /> <img src="README.assets/buy.gif" alt="buy" width="475" />

 [Dashboard](dashboard\index.html) 

2. 데이터 파이프라인

   1. 수집

      - BeautifulSoup을 사용하여 encar,kcar 사이트의 중고차 정보와 차량 관련 뉴스 데이터 크롤링<img src="README.assets/수집.png" alt="gif" width="500" />

   2. 저장

      - Raw데이터 DB구축

      ![DB](README.assets/DB.png)

      

   3. 전처리

      - Python에서 Spark session을 사용하여 학습데이터 셋으로 가공

        ![image-20211201174645562](README.assets/image-20211201174645562.png)

   4. 적재

      - Hadoop 

   5. 

      - 

      

      

      

      

      

      

      

      

      

      

      

      
