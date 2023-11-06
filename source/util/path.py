import os

root_dir = "/root/"
repo_dir = os.path.join(root_dir, "AiProfileAPI")
finetune_dir = repo_dir + "/finetune"
train_dir = repo_dir + "/train_dir"

config_dir = repo_dir + "/config_finetune"
accelerate_config = config_dir + "/config.yaml"
config_file = config_dir + "/config_file.toml"
dataset_config = config_dir + "/dataset_config.toml"
metadata_file = config_dir + "/meta_clean.json"
latents_file = config_dir + "/meta_lat.json"

model_dir = repo_dir + "/pretrained_model/chilloutmix_NiPrunedFp16Fix.safetensors"

output_dir = repo_dir + "/output_dir"
log_dir = repo_dir + "/logs"
