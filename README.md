<h1 align="center">$\bf{\large{\color{#0aba16} Nahc \ ShoppingMall }}$</h1>
<h3 align="center">
    Nahc 쇼핑몰 사이트
</h3>
<p align="center">
   Python Flask Framework를 이용한 쇼핑몰 사이트
</p>

<br>

<blockquote>
  <p dir="auto">
     <strong> Python Flask Framework를 이용한 쇼핑몰 사이트 </strong> <br>
     <strong> 개발 기간 : 2023.08.01 ~ 2023.09.27 </strong> <br>
  </p>
</blockquote>

<br>

### 프로젝트 소개
해당 프로젝트는 쇼핑몰 프로그램으로, <br>
네이버의 검색 API를 통해 여러 종류의 상품에 대한 쇼핑몰 사이트이다. <br>
기본적인 상품 데이터는 네이버의 API를 이용했으며, SQLite에 이관하여 사용하였다. <br>
장바구니, 리뷰, 결제, 즐겨찾기, 구매목록 확인 등의 기능을 제공하는 쇼핑몰 서비스이다.

<br> 

### 개발 환경
<p>$\bf{\large{\color{#0aba16} FrontEnd \ : HTML / CSS / JavaScript}}$</p>
<p>$\bf{\large{\color{#0aba16} BackEnd \ : Python / SQLite }}$</p>
<p>$\bf{\large{\color{#0aba16} Framework \ : Flask }}$</p>
<p>$\bf{\large{\color{#0aba16} Framework \ Main \  Dependency}}$</p>

- [x] Flask_Sqlalchemy
- [x] Flask_Login

<br>

### 데이터 및 API
- <p>$\bf{\large{\color{#0aba16} Naver \ API  }}$</p>
  
  - Naver API를 실제 상품 데이터를 획득
    
- <p>$\bf{\large{\color{#0aba16} Kakao \ API  }}$</p>
  
  - Kakao API를 통해 카카오페이 결제 및 주소에 대한 지도 제공


<br>

### 페이지 및 서비스 기능

- <p>$\bf{\large{\color{#0aba16} 메인화면 \ 및 \ 대표 \ 상품 \ UI }}$</p>


   #### 기능
     * 쇼핑몰에 대한 메인 화면
     * 대표 상품, 인기 상품, 평점 순으로 쇼핑 아이템 나열
     * 상품에 대한 검색 기능 제공
   #### 핵심 기술
     * Naver 검색 API
     * 쇼핑 상품 데이터 (DBMS)
     * 리뷰 점수 및 구매 수에 따른 정렬 알고리즘
     * 사용자 입력에 따른 검색 알고리즘
   #### 사용자 인터페이스
     * 기본 메인 화면 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/0a7543b7-1218-499b-963a-0d3c48fdf65b"/>
       </p>

     * 상품 검색 결과 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/796e47a3-31aa-4a68-99d4-c581525ee659"/>
       </p>
       
     * 평점 순 상품 나열 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/a7253c9f-4be0-4b04-9d0c-45a9cb7f9f10"/>
       </p>

<br>

- <p>$\bf{\large{\color{#0aba16} 상품 \ 상세 \ 정보 \ 및 \ 결제 \ 기능 }}$</p>

   #### 기능
     * 상품에 대한 상세 정보 및 사용자 리뷰 제공
     * Kakao API를 이용한 카카오페이 결제 기능
     * Kakao API를 이용한 지도 제공 및 주소 검색
   #### 핵심 기술
     * Kakao API
     * 쇼핑 상품 데이터 (DBMS)
     * Kakao Map / Daum PostCode
   #### 사용자 UI
     * 상품 상세 정보 UI <br>
       <p align="left">
         <img src="https://github.com/user-attachments/assets/03fc10fb-4d12-4822-8073-ecc5d511d098"/>
       </p>

     * 상품 구매 배송지 확인 및 결제 관련 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/da86b975-c299-47c8-9fec-162bd541a7a8"/>
       </p>

     * 배송지 수정 및 지도 화면 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/f7551dba-8523-4644-bcfb-b0d33a64df36"/>
       </p>
       
     * Kakao 결제 및 결제 완료 화면 UI
       <p align="left">
         <img width="30%" height="300px" src="https://github.com/user-attachments/assets/e1f09ff9-56cc-4655-9a58-435382eee949"/>
         <img width="60%" height="300px" src="https://github.com/user-attachments/assets/c5e1733f-e2be-4aff-a4ac-9f9ca475285c"/>
       </p>

<br>

- <p>$\bf{\large{\color{#0aba16} 장바구니 \ 즐겨찾기 \ 구매목록 확인 \ 기능 }}$</p>

   #### 기능
     * 장바구니 기능 및 즐겨찾기 서비스 기능
     * 사용자가 구매한 목록 확인 가능
     * 구매한 상품에 대한 리뷰 쓰기 기능
   #### 핵심 기술
     * Kakao API
     * 카카오페이를 통한 추가 결제 기능
     * 사용자 구매목록 및 리뷰 데이터 (DBMS)
   #### 사용자 UI
     * 사용자 구매목록 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/a31426ee-4225-4b48-984d-68ee12fec42f"/>
       </p>
     * 사용자 즐겨찾기 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/798adedc-3825-42c5-a41e-e1dc9b4942cc"/>
       </p>
     * 사용자 장바구니 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/b8b40f62-de74-422b-a6be-7e522026736f"/>
       </p>

### 아키텍쳐
#### 디렉터리 구조
```
```
