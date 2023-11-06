import os, subprocess
from util import path, util

v2 = False  # @param{type:"boolean"}
train_data_dir = path.train_dir
model_dir = path.model_dir  # @param {'type' : 'string'}
input_json = path.metadata_file  # @param {'type' : 'string'}
output_json = path.latents_file  # @param {'type' : 'string'}
batch_size = 1  # @param {'type':'integer'}
max_data_loader_n_workers = 2  # @param {'type':'integer'}
max_resolution = "512,512"  # @param ["512,512", "640,640", "768,768"] {allow-input: false}
mixed_precision = "no"  # @param ["no", "fp16", "bf16"] {allow-input: false}
flip_aug = False  # @param{type:"boolean"}
#@markdown Use the `recursive` option to process subfolders as well
recursive = False #@param {type:"boolean"}

config = {
    "_train_data_dir": train_data_dir,
    "_in_json": input_json,
    "_out_json": output_json,
    "_model_name_or_path": model_dir,
    "recursive": recursive,
    "full_path": recursive,
    "v2": v2,
    "flip_aug": flip_aug,
    "min_bucket_reso": 320 if max_resolution != "512,512" else 256,
    "max_bucket_reso": 1280 if max_resolution != "512,512" else 1024,
    "batch_size": batch_size,
    "max_data_loader_n_workers": max_data_loader_n_workers,
    "max_resolution": max_resolution,
    "mixed_precision": mixed_precision,
}

def execute():
    print("\nprepare buckets and latents.....-------------------------------------------------\n")
    args = util.train(config)
    final_args = f"python3 prepare_buckets_latents.py {args}"
    os.chdir(path.finetune_dir)
    try:
        subprocess.run(final_args, shell=True, check=True)
    except:
        raise Exception('prepare buckets and latents error !!!')
