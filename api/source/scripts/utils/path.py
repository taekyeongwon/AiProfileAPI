import os

root_dir = "/root/AiProfileAPI"
repo_dir = os.path.join(root_dir, "api")
finetune_dir = root_dir + "/finetune"
train_data_dir = repo_dir + "/train_data_dir"

config_dir = repo_dir + "/config_finetune"
accelerate_config = config_dir + "/config.yaml"
config_file = config_dir + "/user/config_file.toml"
#dataset_config = config_dir + "/dataset_config.toml"
metadata_file = config_dir + "/user/meta_clean.json"
latents_file = config_dir + "/user/meta_lat.json"
prompt_file = config_dir + "/prompts.txt"

model_dir = repo_dir + "/pretrained_model/chilloutmix_NiPrunedFp16Fix.safetensors"

#trained model output dir
output_dir = repo_dir + "/output_dir"
log_dir = repo_dir + "/logs"
#inference image output dir
result_dir = repo_dir + "/result"
