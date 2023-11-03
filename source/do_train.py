import os
import subprocess
from datetime import datetime

now = datetime.now()

root_dir = "/root/"
repo_dir = os.path.join(root_dir, "AiProfileAPI")
accelerate_config = repo_dir + "/config/config.yaml"
config_file = repo_dir + "/config/config_file.toml" #@param {type:'string'}
dataset_config = repo_dir + "/config/dataset_config.toml" #@param {type:'string'}

accelerate_conf = {
    "config_file" : accelerate_config,
    "num_cpu_threads_per_process" : 1,
}

train_conf = {
    "dataset_config" : dataset_config,
    "config_file" : config_file
}

def train(config):
    args = ""
    for k, v in config.items():
        if k.startswith("_"):
            args += f'"{v}" '
        elif isinstance(v, str):
            args += f'--{k}="{v}" '
        elif isinstance(v, bool) and v:
            args += f"--{k} "
        elif isinstance(v, float) and not isinstance(v, bool):
            args += f"--{k}={v} "
        elif isinstance(v, int) and not isinstance(v, bool):
            args += f"--{k}={v} "

    return args

def execute():
    print("do train start.....\n")
    accelerate_args = train(accelerate_conf)
    train_args = train(train_conf)
    final_args = f"accelerate launch {accelerate_args} train_network.py {train_args}"
    os.chdir(repo_dir)
    print(f"train_network.py execute time :: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        subprocess.run(final_args, shell=True, check=True)
    except:
        raise Exception('training error')
