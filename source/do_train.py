import os
import subprocess
from datetime import datetime
import path

now = datetime.now()

accelerate_conf = {
    "config_file" : path.accelerate_config,
    "num_cpu_threads_per_process" : 1,
}

train_conf = {
    "dataset_config" : path.dataset_config,
    "config_file" : path.config_file
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
    print("\ndo train start.....-------------------------------------------------\n")
    accelerate_args = train(accelerate_conf)
    train_args = train(train_conf)
    final_args = f"accelerate launch {accelerate_args} train_network.py {train_args}"
    os.chdir(path.repo_dir)
    print(f"train_network.py execute time :: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        subprocess.run(final_args, shell=True, check=True)
    except:
        raise Exception('training error !!!')
