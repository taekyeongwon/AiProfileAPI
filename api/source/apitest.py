from fastapi import FastAPI, UploadFile, BackgroundTasks, Request
import os, subprocess
from fastapi.responses import JSONResponse

api = FastAPI()

import FileController
from typing import List
from scripts.errors.exceptions import APIException
from scripts.errors import exceptions as ex

@api.exception_handler(APIException)
async def custom_exception_handler(request: Request, exception: APIException):
    return JSONResponse(
            status_code=exception.status_code,
            content={"result_code":exception.code, "desc":exception.msg}
    )

@api.post("/upload/{user_id}")
async def upload_photo(files: List[UploadFile], user_id: str, background_tasks: BackgroundTasks):
    try:
        tmp_env = FileController.upload_file(files, user_id)
        #background_tasks.add_task(test)
    except APIException as e:
        raise e

    return {"tmp_env": tmp_env} #todo : 성공으로 떨굴 때도 BaseResponse 규격에 맞춰서 주기. Response 객체랑 같이 JSONResponse 생성하는 함수 만들기

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
