# 실습 - FastAPI 및 Docker 배포

이 프로젝트는 FastAPI를 사용하여 간단한 REST API 서버를 구축하고, JSON 파일(`courses.json`)을 활용하여 수강 기록 데이터를 읽고 수정하는 실습 과제입니다. 
이번 단계에서는 작성된 애플리케이션을 **Docker 컨테이너화**하여 **AWS Learner Lab EC2 환경에 배포**하는 구성을 포함합니다.

## 주요 기능
- **GET /courses**: `courses.json` 파일에 저장된 모든 수강 기록 리스트를 반환합니다.
- **POST /courses**: 새로운 수강 과목 정보를 받아 기존 JSON 리스트에 추가하고 파일에 저장합니다.
- **오류 처리**: Pydantic 모델을 사용하여 잘못된 데이터 형식이 들어와도 서버가 종료되지 않고 422 에러 응답을 보냅니다.
- **Docker 컨테이너화**: `Dockerfile` 및 `docker-compose.yml`을 사용하여 독립된 컨테이너 환경에서 안정적으로 실행됩니다.
- **자동 재시작**: EC2 인스턴스가 재부팅되거나 서비스가 멈췄을 때 자동으로 다시 실행되도록 `restart: always` 정책이 적용되어 있습니다.

## 프로젝트 구조
- **main.py**: FastAPI 서버 로직 및 API 엔드포인트 구현
- **courses.json**: 수강 기록 데이터가 저장되는 JSON 파일
- **requirements.txt**: 프로젝트 의존성 파이썬 패키지 목록
- **Dockerfile**: FastAPI 앱을 Docker 이미지로 빌드하기 위한 설정 파일
- **docker-compose.yml**: 외부 포트(80) 매핑 및 컨테이너 실행 옵션 설정 파일
- **.gitignore**: 불필요한 파일의 Git 업로드를 방지하는 설정 파일
- **README.md**: 프로젝트 설명 문서

## 실행 방법

### 방법 1. Docker Compose를 이용한 실행 (AWS EC2 환경 - 배포용)
프로젝트 루트 디렉토리에서 아래 명령어를 입력하여 백그라운드에서 Docker 이미지를 빌드하고 컨테이너를 실행합니다.
```bash
cd EC2_Docker
sudo docker-compose up -d --build
```
**접속 확인**: 실행이 완료되면 브라우저를 열고 http://34.237.195.172/courses 주소(포트 80)로 접근하여 서비스가 열리는지 확인합니다.

### 방법 2. 로컬 환경에서 직접 실행 (테스트용)
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
**접속 확인**: 실행이 완료되면 http://127.0.0.1:8000/courses 주소로 접근합니다.

## API 테스트 (Postman)
- GET /courses: 전체 데이터 조회
- POST /courses: 새 데이터 추가
- Body (JSON, raw):

```json
{
    "course_name": "오픈소스소프트웨어실습",
    "year": "2026",
    "semester": "1",
    "grade": "A+" 
}
```
