import os, subprocess
from fastapi import FastAPI, UploadFile, BackgroundTasks
import FileController

api = FastAPI()

@api.post("/upload/{user_id}")
def upload_photo(files: List[UploadFile], user_id: str, background_tasks: BackgroundTasks):
    try:
        tmp_env = FileController.upload_file()
        background_tasks.add_task(start_train, tmp_env)
    except Exception as e:
        print(e)
        raise HttpException()
    
    return {"tmp_env": tmp_env}

def start_train(tmp_env):
    try:
        subprocess.run("python3 training.py", shell=True, check=True, env=tmp_env)
    except Exception as e:
        print(e)
    else:
        print("train done.")
        start_inference(tmp_env)

def start_inference(tmp_env):
    try:
        subprocess.run("python3 inference.py", shell=True, check=True, env=tmp_env)
    except Exception as e:
        print(e)
    else:
        print("inference done.")
