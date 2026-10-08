# 파이썬 3.10 경량 이미지 기반
FROM python:3.10-slim

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 후 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 전체 복사
COPY . .

# Gunicorn을 사용하여 8080 포트에서 Flask 앱 구동
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
