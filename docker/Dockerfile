FROM nvidia/cuda:11.8.0-base-ubuntu22.04
LABEL maintainer="tkw3351@gmail.com"
LABEL version="1.0.1"

# 기본 패키지 설치와 필요한 패키지만 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip vim \
    libgl1-mesa-glx libglib2.0-0 && \
    ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 캐싱 이용하기 위해 먼저 다운로드
RUN pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --index-url https://download.pytorch.org/whl/cu118
RUN pip install xformers==0.0.20

#학습 스크립트 복사
RUN mkdir -p /root/AiProfileAPI
WORKDIR /root/AiProfileAPI/
COPY ../requirements.txt .
COPY ../setup.py .

#의존성 설치. COPY 레이어에서 수정이 발생되면 캐시 동작 안하고 아래 작업 수행
RUN pip install --upgrade -r requirements.txt

# 사용하지 않는 라이브러리와 파일 정리
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# 불필요한 캐시 및 로그 파일 제거
RUN rm -rf /var/log/* /var/cache/apt/* /root/.cache