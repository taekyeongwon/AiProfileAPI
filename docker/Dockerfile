FROM nvidia/cuda:11.8.0-base-ubuntu22.04
LABEL maintainer="tkw3351@gmail.com"
LABEL version="1.0.0"


#파이썬, 편집기, git 설치, timezone 설정
RUN apt-get -y update && apt-get install -y sudo
RUN sudo ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN apt-get -y install python3 python3-pip && apt-get -y install vim && apt-get -y install git

#학습 스크립트 복사
RUN mkdir -p /root/AiProfileAPI
WORKDIR /root/AiProfileAPI
COPY .. .
#RUN git clone https://github.com/taekyeongwon/AiProfileAPI.git

#의존성 설치
RUN pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --index-url https://download.pytorch.org/whl/cu118
RUN pip install --upgrade -r requirements.txt
RUN pip install xformers==0.0.20

#WD14Tagger 의존성 설치
RUN apt-get install -y libgl1-mesa-glx && apt-get install -y libglib2.0-0