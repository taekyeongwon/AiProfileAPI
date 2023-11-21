import os, subprocess
from scripts.utils import path, util

def set_config():
    train_data_dir = path.train_data_dir
    # @markdown Merge tags and/or captions exist in `train_data_dir` into one metadata JSON file, which will be used as the input for the bucketing section.
    metadata = path.metadata_file
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
    return config

def execute():
    print("\ncreate metadata file.....-------------------------------------------------\n")
    args = util.train(set_config())
    final_args = f"python3 merge_dd_tags_to_metadata.py {args}"
    os.chdir(path.finetune_dir)
    try:
        os.system(final_args)
        #subprocess.run(final_args, shell=True, check=True)
    except Exception as e:
        raise Exception('create metadata error !!!', e)
