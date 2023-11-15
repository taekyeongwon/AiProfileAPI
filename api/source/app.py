import os, subprocess, shutil
from distutils.dir_util import copy_tree

user_id = "test"
root_dir = "/root/AiProfileAPI"
repo_dir = root_dir + "/api"
user_dir = repo_dir + f"/tmp/{user_id}"
config_dir = repo_dir + "/config_finetune"

path = {
        'USER_ID' : user_id,
        'ROOT_DIR' : root_dir,
        'REPO_DIR' : repo_dir,
        'USER_DIR' : user_dir,
        'CONFIG_DIR' : config_dir,
        'FINETUNE_DIR' : root_dir + "/finetune",

        'ACCELERATE_CONFIG' : config_dir + "/config.yaml",
        'CONFIG_FILE' : config_dir + "/config_file.toml",
        #dataset_config = config_dir + "/dataset_config.toml"
        'PROMPT_FILE' : config_dir + "/prompts.txt",

        'MODEL_DIR' : repo_dir + "/pretrained_model/chilloutmix_NiPrunedFp16Fix.safetensors",
        #model_dir = "runwayml/stable-diffusion-v1-5"

        'TRAIN_DATA_DIR' : user_dir + "/train_data_dir",
        'METADATA_FILE' : user_dir + "/meta_clean.json",
        'LATENTS_FILE' : user_dir + "/meta_lat.json",
        #trained model output dir
        'OUTPUT_DIR' : user_dir + "/output_dir",
        'LOG_DIR' : user_dir + "/logs",
        #inference image output dir
        'RESULT_DIR' : user_dir + "/result"
}
for key, value in path.items():
    os.environ[key] = value

if not os.path.exists(user_dir):
    os.makedirs(user_dir)
    os.makedirs(path['TRAIN_DATA_DIR'])
    os.makedirs(path['OUTPUT_DIR'])
    os.makedirs(path['LOG_DIR'])
    os.makedirs(path['RESULT_DIR'])
    copy_tree(path['REPO_DIR']+"/train_data_dir/", path['TRAIN_DATA_DIR'])

try:
    subprocess.run("python3 training.py", shell=True, check=True, env=os.environ)
    subprocess.run("python3 inference.py", shell=True, check=True, env=os.environ)
except Exception as e:
    print(e)
else:
    print("all done.")
