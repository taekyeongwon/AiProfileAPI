import os, subprocess
from util import path, util


train_data_dir = path.train_dir
# @markdown Merge tags and/or captions exist in `train_data_dir` into one metadata JSON file, which will be used as the input for the bucketing section.
metadata = path.config_dir + "/meta_clean.json"
# @markdown Use `recursive` option to process subfolders as well
recursive = False
# @markdown Use `clean_caption` option to clean such as duplicate tags, `women` to `girl`, etc
clean_caption = False

config = {
    "_train_data_dir": train_data_dir,
    "_out_json": metadata,
    "recursive": recursive,
    "full_path": recursive,
}

def execute():
    print("\ncreate metadata file.....-------------------------------------------------\n")
    args = util.train(config)
    final_args = f"python3 merge_dd_tags_to_metadata.py {args}"
    os.chdir(path.finetune_dir)
    try:
        subprocess.run(final_args, shell=True, check=True)
    except:
        raise Exception('create metadata error !!!')
