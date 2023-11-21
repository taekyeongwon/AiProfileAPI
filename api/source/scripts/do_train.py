import os, subprocess
from datetime import datetime
from scripts.utils import path, util

def execute():
    print("\ndo train start.....-------------------------------------------------\n")
    now = datetime.now()
    accelerate_conf = {
            "config_file" : path.accelerate_config,
            "num_cpu_threads_per_process": 1,
    }
    train_conf = {
            #"dataset_config" : path.dataset_config,
            "config_file" : path.config_file
    }
    accelerate_args = util.train(accelerate_conf)
    train_args = util.train(train_conf)
    final_args = f"accelerate launch {accelerate_args} train_network.py {train_args}"
    os.chdir(path.root_dir)
    print(f"train_network.py execute time :: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        os.system(final_args)
        #subprocess.run(final_args, shell=True, check=True)
    except Exception as e:
        raise Exception('training error !!!', e)
