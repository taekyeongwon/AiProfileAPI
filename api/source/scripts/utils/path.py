import os

root_dir = os.getenv("ROOT_DIR")
repo_dir = os.getenv("REPO_DIR")
user_dir = os.getenv("USER_DIR")
config_dir = os.getenv("CONFIG_DIR")
finetune_dir = os.getenv("FINETUNE_DIR")

accelerate_config = os.getenv("ACCELERATE_CONFIG")
config_file = os.getenv("CONFIG_FILE")
#dataset_config = config_dir + "/dataset_config.toml"
prompt_file = os.getenv("PROMPT_FILE")

model_dir = os.getenv("MODEL_DIR")
#model_dir = "runwayml/stable-diffusion-v1-5"

train_data_dir = os.getenv("TRAIN_DATA_DIR")
metadata_file = os.getenv("METADATA_FILE")
latents_file = os.getenv("LATENTS_FILE")
#trained model output dir
output_dir = os.getenv("OUTPUT_DIR")
log_dir = os.getenv("LOG_DIR")
#inference image output dir
result_dir = os.getenv("RESULT_DIR")
