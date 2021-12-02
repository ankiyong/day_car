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

<img src="README.assets/image-20211202173833048.png" alt="image-20211202173833048" style="zoom:50%;float:left;" />

#### 5. Outputs

1. Django를 사용하여 구현한 실제 웹 페이지*(차량 가격 예측(판매) / 매물 정보 검색(구매) 페이지)*

   [http://day-car.com](https://ankiyong.github.io/resume/#)

<img src="README.assets/gif.gif" alt="gif" width="475" /> <img src="README.assets/buy.gif" alt="buy" width="475" />



2. 데이터 파이프라인

   1. 수집

      - BeautifulSoup을 사용하여 encar,kcar 사이트의 중고차 정보와 차량 관련 뉴스 데이터 크롤링<img src="README.assets/수집.png" alt="gif" width="500" />

   2. 저장

      - Raw데이터 DB구축(추후 매물정보 제공에 사용)

        ![DB](README.assets/DB.png)

        

      - 적재

        - Hadoop에 Raw 데이터 csv파일 적재

      - 전처리

        - Python에서 Spark session을 사용하여 Hadoop에 적재된 csv를 불러와 학습데이터로 가공

          ![image-20211201174645562](README.assets/image-20211201174645562.png)

          

      - 적재 및 저장

        - 학습데이터 csv파일을 Hadoop에 적재 및 Mysql에 학습데이터 DB구축

          ![data](README.assets/data.png)

      - 최종 ERD

        - 상단 2개 테이블은 컬럼명이 같지만 향후 

          업체별 검색기능 도입을 위해 테이블을 분리함

        <img src="README.assets/ERD.png" alt="ERD" style="height:600px;float:left" />

        

        

        

        

   3. Dashboard

      - 수집한 데이터로 dashboard를 만들어 시각화 진행

      ![dash](README.assets/dash.png)

      

      

      

      

      

      
