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

### 서비스 기능

- <p>$\bf{\large{\color{#0aba16} 퀴즈 \ 카테고리 \ 설정 \ 및 \ 문제풀이 \ 화면 }}$</p>


   #### 기능
     * 퀴즈에 대한 난이도, 문제 수, 카테고리에 대한 설정 제공
     * 난이도에 따라 차등 점수 부여
     * 사용자 친화적인 인터페이스로 손쉬운 설정 및 문제 풀이 제공
   #### 핵심 기술
     * Trivia API
     * 사용자 랭킹 시스템 데이터 (DBMS)
     * Trivia Data 필터 기능
   #### 사용자 인터페이스
     * 퀴즈 카테고리 설정 메인 화면 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/abf6cb1c-2fa7-440e-8b5d-af44111856b1"/>
       </p>
     * 퀴즈 카테고리 설졍 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/8d126ac0-de46-4fa6-a289-85ec8175e8f2"/>
       </p>
     * 퀴즈 풀이 진행 UI
       <p align="left">
         <img width="45%" height="250px" src="https://github.com/user-attachments/assets/8f4187bb-3d76-4daa-92a4-01bff2ba69be"/>
         <img width="50%" height="250px" src="https://github.com/user-attachments/assets/1008df46-3567-43ac-9d02-6bbf1dcb7e3e"/>
       </p>

<br>

- <p>$\bf{\large{\color{#0aba16} 완료 \ 문제 \ 및 \ 랭킹 \ 확인 }}$</p>

   #### 기능
     * 문제 풀이 완료 후 카테고리 및 총점수, 정답률 확인
     * 자신의 점수를 다른 사용자의 점수와 비교할 수 있는 랭킹 시스템 제공
     * 자신이 틀린 문제 혹은 맞은 문제를 각 문제 번호 별로 확인
   #### 핵심 기술
     * Trivia API
     * 사용자 랭킹 시스템 데이터 (DBMS)
     * 사용자의 문제 정답 여부 추적 알고리즘
   #### 사용자 UI
     * 카테고리 및 통계 요약 UI <br>
       <p align="left">
         <img src="https://github.com/user-attachments/assets/5c53df10-49bc-42f1-accf-fd5a8154f232"/>
       </p>

     * 문제 요약 및 정답 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/5373d711-ab85-4137-b396-0e4612661e0a"/>
       </p>
     * 서비스 사용자 랭킹 시스템 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/58e640da-904a-4e9f-912e-75c39c9b911d"/>
       </p>
       <p align="left">
         <img src="https://github.com/user-attachments/assets/938d1960-e1c8-4acb-9ebb-863054bdab12"/>
       </p>

<br>

- <p>$\bf{\large{\color{#0aba16} 게시판  \ 및 \ 댓글 \ 기능 }}$</p>

   #### 기능
     * 퀴즈에 대한 여러 답을 주고받을 수 있는 커뮤니티 제공
     * 사용자 간 댓글을 통한 소통
     * 퀴즈에 대한 사진 업로드 기능
   #### 핵심 기술
     * 커뮤니티 플랫폼 구축 및 댓글 시스템
     * 파일 업로드 기능
     * 사용자 포스트 및 댓글 데이터 (DBMS)
   #### 사용자 UI
     * 게시판 메인화면 UI <br>
       <p align="left">
         <img src="https://github.com/user-attachments/assets/a5327085-504b-44a7-b13e-823bbed2322b"/>
       </p>
     * 게시판 글 및 댓글 UI
       <p align="left">
         <img src="https://github.com/user-attachments/assets/1a5eb8a6-3d51-4a00-94f4-45f00f96cc04"/>
       </p>
       <p align="left">
         <img src="https://github.com/user-attachments/assets/41efcad5-d33c-46fe-8a01-1a86de2768f3"/>
       </p>

### 아키텍쳐
#### 디렉터리 구조
```
```
