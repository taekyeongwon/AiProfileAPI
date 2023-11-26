import os, subprocess
from typing import List
from fastapi import UploadFile
import time
from scripts.errors import exceptions as ex

def upload_file(files: List[UploadFile], user_id: str):
    path = set_environ(user_id) #각 프로세스 별 환경변수 세팅용
    makedirs(path['USER_DIR'])
    upload_dir = path['TRAIN_DATA_DIR']  # 이미지를 저장할 서버 경로

    for index, file in enumerate(files):
        content = file.file.read() #todo : 여러 사진 읽어와서 유효한지 검사, else에서 바로 raise하지 말고 어떤 파일들이 유효하지 않은지를 전달해야 함.
        if check_validate(content):
            filename = f"{user_id} ({index}).jpg"
            with open(os.path.join(upload_dir, filename), "wb") as fp:
                fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)
        else:
            raise ex.InvalidImageException()

    tmp_env = os.environ
    for key, value in path.items():
        tmp_env[key] = value
    
    return tmp_env

def set_environ(user_id):
    root_dir = "/root/AiProfileAPI"
    repo_dir = root_dir + "/api"
    user_dir = repo_dir + f"/user/{user_id}"
    config_dir = repo_dir + "/config_finetune"
    custom_tag = f"sks {user_id}"

    path = {
            'USER_ID' : user_id,
            'ROOT_DIR' : root_dir,
            'REPO_DIR' : repo_dir,
            'USER_DIR' : user_dir,
            'CONFIG_DIR' : config_dir,
            'FINETUNE_DIR' : root_dir + "/finetune",

            'CUSTOM_TAG': custom_tag,

            'ACCELERATE_CONFIG' : config_dir + "/config.yaml",
            #dataset_config = config_dir + "/dataset_config.toml"
            #'PROMPT_FILE' : config_dir + "/prompts.txt",
            'PROMPT' : f"{custom_tag}, 1girl, solo, ultra-detailed, close-up, straight on, face focus, looking at viewer, short hair, bangs, simple background, shirt, black hair, white background, brown eyes, black eyes, lips, portrait, realistic",
            #'PROMPT' : f"1girl",
            'NG_PROMPT' : "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, nsfw",

            'MODEL_DIR' : repo_dir + "/pretrained_model/chilloutmix_v10.ckpt",
            #'MODEL_DIR' : "runwayml/stable-diffusion-v1-5",

            'CONFIG_FILE' : user_dir + "/config_file.toml",
            'TRAIN_DATA_DIR' : user_dir + "/train_data_dir",
            'METADATA_FILE' : user_dir + "/meta_clean.json",
            'LATENTS_FILE' : user_dir + "/meta_lat.json",
            #trained model output dir
            'OUTPUT_DIR' : user_dir + "/output_dir",
            'LOG_DIR' : user_dir + "/logs",
            #inference image output dir
            'RESULT_DIR' : user_dir + "/result"
        }
    return path

def makedirs(user_dir):
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
        os.makedirs(user_dir + "/train_data_dir")
        os.makedirs(user_dir + "/output_dir")
        os.makedirs(user_dir + "/logs")
        os.makedirs(user_dir + "/result")

def check_validate(file):   #사진에 얼굴이 제대로 나왔는지 확인. 이미지 리사이징
    return False

