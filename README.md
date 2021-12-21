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
