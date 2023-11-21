import os, subprocess
from scripts.utils import path, util

tagger_conf = {
    "batch_size" : 2
}

def execute():
    print("\ngenerate tag start.....-----------------------------------------------\n")
    tagger_args = util.train(tagger_conf)
    final_args = f"python3 tag_images_by_wd14_tagger.py {tagger_args} {path.train_data_dir}"
    os.chdir(path.finetune_dir)
    try:
        os.system(final_args)
        #subprocess.run(final_args, shell=True, check=True)
    except Exception as e:
        raise Exception('tag generate error !!!', e)
