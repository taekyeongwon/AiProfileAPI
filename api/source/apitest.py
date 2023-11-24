from fastapi import FastAPI, UploadFile, BackgroundTasks
import os, subprocess

api = FastAPI()

import FileController
from typing import List


@api.post("/upload/{user_id}")
async def upload_photo(files: List[UploadFile], user_id: str, background_tasks: BackgroundTasks):
    tmp_env = FileController.upload_file(files, user_id)
    #background_tasks.add_task(test)
    return {"tmp_env": tmp_env}

@api.get('/random_number')
def random_no():
    import random
    val_random_number = random.randint(1, 10)

    return val_random_number

@api.post("/photo")
async def upload_photo(file: UploadFile):
    UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로

    content = await file.read()
    filename = f"test.jpg"
    with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
        fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)

    return {"filename": filename}

# 사진 다운로드
@api.get("/download/photo/{user_id}")
async def download_photo(user_id: str):
    img_url = f"/root/AiProfileAPI/api/tmp/{user_id}/result/"
    file_list = os.listdir(img_url)
    file_list_jpg = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png")]

    return file_list_jpg
