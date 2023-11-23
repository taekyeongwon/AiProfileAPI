import os, subprocess
from scripts.utils import path, util

batch_size = 8 #@param {type:'number'}
max_data_loader_n_workers = 2 #@param {type:'number'}
beam_search = True #@param {type:'boolean'}
min_length = 5 #@param {type:"slider", min:0, max:100, step:5.0}
max_length = 75 #@param {type:"slider", min:0, max:100, step:5.0}
#@markdown Use the `recursive` option to process subfolders as well.
recursive = False #@param {type:"boolean"}
#@markdown Debug while captioning, it will print your image file with generated captions.
verbose_logging = True #@param {type:"boolean"}

config = {
    "_train_data_dir" : path.train_data_dir,
    "batch_size" : batch_size,
    "beam_search" : beam_search,
    "min_length" : min_length,
    "max_length" : max_length,
    "debug" : verbose_logging,
    "caption_extension" : ".caption",
    "max_data_loader_n_workers" : max_data_loader_n_workers,
    "recursive" : recursive
}

def execute():
    print("\ngenerate caption start.....-----------------------------------------------\n")
    caption_args = util.train(config)
    final_args = f"python3 make_captions.py {caption_args}"
    os.chdir(path.finetune_dir)
    try:
        subprocess.run(final_args, shell=True, check=True)
    except Exception as e:
        raise Exception('caption generate error !!!', e)
