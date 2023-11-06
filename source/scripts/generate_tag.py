import os, subprocess
from util import path, util

tagger_conf = {
    "batch_size" : 2
}

def execute():
    print("\ngenerate tag start.....-----------------------------------------------\n")
    tagger_args = util.train(tagger_conf)
    final_args = f"python3 tag_images_by_wd14_tagger.py {tagger_args} {path.train_dir}"
    os.chdir(path.finetune_dir)
    try:
        subprocess.run(final_args, shell=True, check=True)
    except:
        raise Exception('tag generate error !!!')
