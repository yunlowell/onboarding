# django, middleware, JWT 의 개념 정리 TIL
https://velog.io/@dbsdbf95/Django%EC%99%80-Middleware-%EB%B0%8F-JWT-%EA%B0%9C%EB%85%90-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0

# Onboarding Project
Onboarding은 사용자 인증 시스템을 관리하고, JWT(JSON Web Token)를 사용하여 로그인 및 인증을 처리하는 Django 프로젝트입니다. 이 프로젝트는 API 문서화 도구인 Swagger UI를 사용하여, API를 테스트하고 문서화하는 기능을 제공합니다.

---

## 🛠️ 기술 스택
- Backend: Django, Django REST Framework
- uthentication: JWT (JSON Web Token)
- Frontend: Swagger UI (API 문서화 및 테스트)
- Database: SQLite
- 웹 서버: Gunicorn, Nginx (배포 환경)

## ⚙️ 설치 방법
**1️⃣ 프로젝트 클론**
```bash
git clone https://github.com/your-username/onboarding.git
```

**2️⃣ 가상 환경 설정**
프로젝트의 루트 디렉토리에서 가상 환경을 생성합니다.

```bash
python3 -m venv venv
source venv/bin/activate # Mac
source venv\Scripts\activate # Window
pip install -r requirements.txt
```
**3️⃣ 의존성 설치**
필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

**4️⃣ 개발 서버 실행**
개발 서버를 실행합니다.

```bash
python manage.py runserver
```

## ✅ 사용법
1. 로그인 API
POST /login/: 사용자가 로그인할 수 있는 API입니다. username과 password를 전달하여 JWT 토큰을 발급받습니다.
![](https://velog.velcdn.com/images/dbsdbf95/post/2d89a4c2-b0be-4019-8988-301e093973d1/image.png)

2. 회원가입 API
POST /signup/: 새 사용자를 생성하는 API입니다. username, password, nickname을 포함한 정보를 전달하여 회원가입을 진행합니다.
![](https://velog.velcdn.com/images/dbsdbf95/post/bf2b436e-b923-4b59-901e-0b3b578c06de/image.png)

3. Swagger UI
GET /swagger/: Swagger UI를 통해 API 문서와 테스트 기능을 제공합니다. API 엔드포인트 및 요청/응답을 시각적으로 확인할 수 있습니다.
API 문서
Swagger UI에서 제공되는 API 문서에서 API 요청과 응답 형식을 확인할 수 있습니다. /swagger/ 엔드포인트를 통해 Swagger UI에 접속할 수 있습니다.
![](https://velog.velcdn.com/images/dbsdbf95/post/e5d9c5ed-7fe4-496a-89f2-3a424679e277/image.png)

4.pytest
회원가입과 로그인 API의 정상 동작을 확인했습니다. 이를 위해 pytest와 APIClient를 사용하여 HTTP 요청을 보냈고, 그에 대한 응답을 확인했습니다.
![](https://velog.velcdn.com/images/dbsdbf95/post/06c8d2e6-e043-49ad-9eaf-6a15debe4065/image.png)
