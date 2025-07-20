# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 필수 패키지 설치: ping, curl
RUN apt update && \
    apt install -y iputils-ping curl && \
    rm -rf /var/lib/apt/lists/*

# Flask 및 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY . .

# 포트 노출
EXPOSE 5000

# 앱 실행
CMD ["python", "app.py"]
