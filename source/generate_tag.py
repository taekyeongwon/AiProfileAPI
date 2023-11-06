import os
import subprocess
import path

tagger_conf = {
    "batch_size" : 2
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
    print("\ngenerate tag start.....-----------------------------------------------\n")
    tagger_args = train(tagger_conf)
    final_args = f"python3 tag_images_by_wd14_tagger.py {tagger_args} {path.train_dir}"
    os.chdir(path.finetune_dir)
    try:
        subprocess.run(final_args, shell=True, check=True)
    except:
        raise Exception('tag generate error !!!')
