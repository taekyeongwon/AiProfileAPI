import os

root_dir = "/root/"
repo_dir = os.path.join(root_dir, "AiProfileAPI")
finetune_dir = repo_dir + "/finetune"
train_dir = repo_dir + "/train_dir"

accelerate_config = repo_dir + "/config/config.yaml"
config_file = repo_dir + "/config/config_file.toml"
dataset_config = repo_dir + "/config/dataset_config.toml"
