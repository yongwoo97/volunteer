# 프렌즈
### 봉사 매칭 플랫폼

<hr/>

### 2021-12-21
#### 회원가입 api 구현 완료
##### 공부내용
###### 1. AbstractBaseUser vs AbstractUser
###### 둘의 차이는 칼럼의 차이도 있지만 AbstractBaseUser를 상속할 때는 settings.py에 AUTH_USER_MODEL을 설정해주어야함
###### 그러나 AbstractUser를 상속할 때는 반드시 AUTH_USER_MODEL를 지정해줘야 migrate가 가능
###### 이유는 superuser생성시 필요한 칼럼 수를 AbstractBaseUser는 충족하지 못하기에 설정할 필요가 없었던 것이다

<hr/>

### 2021-12-23
#### 권한에 따른 게시판 수정 및 삭제 기능 구현 완료
##### 공부내용
###### 장고가 클라이언트로 부터 http 요청을 받으면 어떻게 Request 객체로 변환하고 Request.user를 실행하는지 알 수 있음.

<hr/>

### 2021-12-26
#### 이메일 인증 서비스 구현
##### 공부내용
###### 회원가입시 사용자는 is_active = False로 default 세팅으로 권한에 제한되어 있음
###### 인증 이메일은 celery를 사용하여 비동기적 처리
###### 인증을 위한 url은 장고 view에서 activate로 처리

<hr/>

### 2021-12-28
#### 소켓 채팅 시스템 준비
##### 공부내용
###### 기존 rest api방식으로는 실시간 채팅어려움
###### channels라이브러리를 활용하여 api를 구현할 예정

<hr/>

### 2021-12-28
#### 채팅 구현후 확인 완료(내부 시스템으로는 이식 못함)
##### 공부내용
###### 기존 rest api방식으로는 실시간 채팅어려움
###### ASGI 비동기적인 방식으로 장고를 전환
###### 실제 채팅을 구현하여 실현 가능성 파악완료(가능)
###### orm, selected_related(join기능으로 외래키를 서버가 끝날때까지 cache값으로 저장
###### prefetch_related는 selected_related와 동일하나 다대다 관계일 때 사용
