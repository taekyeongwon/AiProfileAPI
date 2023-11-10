import os, subprocess
from scripts.utils import path, util

#5.1 Model Config
v2 = False  # @param {type:"boolean"}
v_parameterization = False  # @param {type:"boolean"}
project_name = "chillout_1000"  # @param {type:"string"}
pretrained_model_name_or_path = path.model_dir  # @param {type:"string"}
vae = ""  # @param {type:"string"}
output_dir = path.output_dir  # @param {'type':'string'}
train_data_dir = path.train_data_dir

#5.2 Dataset Config
dataset_repeats = 20  # @param {type:"number"}
in_json = path.latents_file  # @param {type:"string"}
resolution = "512,512" # @param ["512,512", "768,768"]
keep_tokens = 0  # @param {type:"number"}

#5.3 LoRA and Optimizer Config
# @markdown ### LoRA Config:
network_category = "LoRA"  # @param ["LoRA", "LoCon", "LoCon_Lycoris", "LoHa"]

# @markdown Recommended values:

# @markdown | network_category | network_dim | network_alpha | conv_dim | conv_alpha |
# @markdown | :---: | :---: | :---: | :---: | :---: |
# @markdown | LoRA | 32 | 1 | - | - |
# @markdown | LoCon | 16 | 8 | 8 | 1 |
# @markdown | LoHa | 8 | 4 | 4 | 1 |

# @markdown - Note that `dropout` and `cp_decomposition` are not available in this notebook.

# @markdown `conv_dim` and `conv_alpha` are needed to train `LoCon` and `LoHa`; skip them if you are training normal `LoRA`. However, when in doubt, set `dim = alpha`.
conv_dim = 32  # @param {'type':'number'}
conv_alpha = 16  # @param {'type':'number'}
# @markdown It's recommended not to set `network_dim` and `network_alpha` higher than 64, especially for `LoHa`.
# @markdown If you want to use a higher value for `dim` or `alpha`, consider using a higher learning rate, as models with higher dimensions tend to learn faster.
network_dim = 32  # @param {'type':'number'}
network_alpha = 16  # @param {'type':'number'}
# @markdown You can specify this field for resume training.
network_weight = ""  # @param {'type':'string'}
network_module = "lycoris.kohya" if network_category in ["LoHa", "LoCon_Lycoris"] else "networks.lora"
network_args = "" if network_category == "LoRA" else [
    f"conv_dim={conv_dim}", f"conv_alpha={conv_alpha}",
    ]
# @markdown ### <br>Optimizer Config:
# @markdown `NEW` Gamma for reducing the weight of high-loss timesteps. Lower numbers have a stronger effect. The paper recommends 5. Read the paper [here](https://arxiv.org/abs/2303.09556).
min_snr_gamma = -1 #@param {type:"number"}
# @markdown `AdamW8bit` was the old `--use_8bit_adam`.
optimizer_type = "AdamW8bit"  # @param ["AdamW", "AdamW8bit", "Lion", "SGDNesterov", "SGDNesterov8bit", "DAdaptation", "AdaFactor"]
# @markdown Additional arguments for optimizer, e.g: `["decouple=True","weight_decay=0.6"]`
optimizer_args = ""  # @param {'type':'string'}
# @markdown Set `unet_lr` to `1.0` if you use `DAdaptation` optimizer, because it's a [free learning rate](https://github.com/facebookresearch/dadaptation) algorithm.
# @markdown However, it is recommended to set `text_encoder_lr = 0.5 * unet_lr`.
# @markdown Also, you don't need to specify `learning_rate` value if both `unet_lr` and `text_encoder_lr` are defined.
train_unet = True  # @param {'type':'boolean'}
unet_lr = 1e-4  # @param {'type':'number'}
train_text_encoder = True  # @param {'type':'boolean'}
text_encoder_lr = 5e-5  # @param {'type':'number'}
lr_scheduler = "constant"  # @param ["linear", "cosine", "cosine_with_restarts", "polynomial", "constant", "constant_with_warmup", "adafactor"] {allow-input: false}
lr_warmup_steps = 0  # @param {'type':'number'}
# @markdown You can define `num_cycles` value for `cosine_with_restarts` or `power` value for `polynomial` in the field below.
lr_scheduler_num_cycles = 0  # @param {'type':'number'}
lr_scheduler_power = 0  # @param {'type':'number'}

if network_category == "LoHa":
    network_args.append("algo=loha")
elif network_category == "LoCon_Lycoris":
    network_args.append("algo=lora")

#5.4 Training Config
lowram = False  # @param {type:"boolean"}
enable_sample_prompt = False  # @param {type:"boolean"}
sampler = "ddim"  # @param ["ddim", "pndm", "lms", "euler", "euler_a", "heun", "dpm_2", "dpm_2_a", "dpmsolver","dpmsolver++", "dpmsingle", "k_lms", "k_euler", "k_euler_a", "k_dpm_2", "k_dpm_2_a"]
noise_offset = 0.0  # @param {type:"number"}
num_epochs = 5  # @param {type:"number"}
train_batch_size = 1  # @param {type:"number"}
mixed_precision = "fp16"  # @param ["no","fp16","bf16"] {allow-input: false}
save_precision = "fp16"  # @param ["float", "fp16", "bf16"] {allow-input: false}
save_n_epochs_type = "save_every_n_epochs"  # @param ["save_every_n_epochs", "save_n_epoch_ratio"] {allow-input: false}
save_n_epochs_type_value = 1  # @param {type:"number"}
save_model_as = "safetensors"  # @param ["ckpt", "pt", "safetensors"] {allow-input: false}
max_token_length = 225  # @param {type:"number"}
clip_skip = 2  # @param {type:"number"}
gradient_checkpointing = False  # @param {type:"boolean"}
gradient_accumulation_steps = 1  # @param {type:"number"}
seed = -1  # @param {type:"number"}
logging_dir = path.log_dir
prior_loss_weight = 1.0

#5.1
def model_config():
    global project_name
    global output_dir
    global train_data_dir

    project_name += ""  # @param {type:"string"}
    output_dir = path.output_dir + ""  # @param {'type':'string'}
    train_data_dir = path.train_data_dir + ""

    print("Project Name: ", project_name)
    print("Model Version: Stable Diffusion V1.x") if not v2 else ""
    print("Model Version: Stable Diffusion V2.x") if v2 and not v_parameterization else ""
    print("Model Version: Stable Diffusion V2.x 768v") if v2 and v_parameterization else ""
    print(
        "Pretrained Model Path: ", pretrained_model_name_or_path
    ) if pretrained_model_name_or_path else print("No Pretrained Model path specified.")
    print("VAE Path: ", vae) if vae else print("No VAE path specified.")
    print("Output Path: ", output_dir)

#5.2
import toml
import glob

def dataset_config():
# @markdown This notebook support multi-folder training but not designed for multi-concept training. You can use [Kohya LoRA Dreambooth](https://github.com/Linaqruf/kohya-trainer/blob/main/kohya-LoRA-dreambooth.ipynb), or add an activation word for each train folder under `4.2.3. Custom Caption/Tag (Optional)` instead.
    global in_json
    in_json = path.latents_file  # @param {type:"string"}

#5.3
def lora_config():
    print("- LoRA Config:")
    print(f"  - Min-SNR Weighting: {min_snr_gamma}") if not min_snr_gamma == -1 else ""
    print(f"  - Loading network module: {network_module}")
    if not network_category == "LoRA":
        print(f"  - network args: {network_args}")
    print(f"  - {network_module} linear_dim set to: {network_dim}")
    print(f"  - {network_module} linear_alpha set to: {network_alpha}")
    if not network_category == "LoRA":
        print(f"  - {network_module} conv_dim set to: {conv_dim}")
        print(f"  - {network_module} conv_alpha set to: {conv_alpha}")

    global network_weight
    if not network_weight:
        print("  - No LoRA weight loaded.")
    else:
        if os.path.exists(network_weight):
            print(f"  - Loading LoRA weight: {network_weight}")
        else:
            print(f"  - {network_weight} does not exist.")
            network_weight = ""

    print("- Optimizer Config:")
    print(f"  - Additional network category: {network_category}")
    print(f"  - Using {optimizer_type} as Optimizer")
    if optimizer_args:
        print(f"  - Optimizer Args: {optimizer_args}")
    if train_unet and train_text_encoder:
        print("  - Train UNet and Text Encoder")
        print(f"    - UNet learning rate: {unet_lr}")
        print(f"    - Text encoder learning rate: {text_encoder_lr}")
    if train_unet and not train_text_encoder:
        print("  - Train UNet only")
        print(f"    - UNet learning rate: {unet_lr}")
    if train_text_encoder and not train_unet:
        print("  - Train Text Encoder only")
        print(f"    - Text encoder learning rate: {text_encoder_lr}")
    print(f"  - Learning rate warmup steps: {lr_warmup_steps}")
    print(f"  - Learning rate Scheduler: {lr_scheduler}")
    if lr_scheduler == "cosine_with_restarts":
        print(f"  - lr_scheduler_num_cycles: {lr_scheduler_num_cycles}")
    elif lr_scheduler == "polynomial":
        print(f"  - lr_scheduler_power: {lr_scheduler_power}")

#5.4
def training_config():
    global logging_dir
    logging_dir = path.log_dir

    config = {
        "model_arguments": {
            "v2": v2,
            "v_parameterization": v_parameterization if v2 and v_parameterization else False,
            "pretrained_model_name_or_path": pretrained_model_name_or_path,
            "vae": vae,
        },
        "additional_network_arguments": {
            "no_metadata": False,
            "unet_lr": float(unet_lr) if train_unet else None,
            "text_encoder_lr": float(text_encoder_lr) if train_text_encoder else None,
            "network_weights": network_weight,
            "network_module": network_module,
            "network_dim": network_dim,
            "network_alpha": network_alpha,
            "network_args": network_args,
            "network_train_unet_only": True if train_unet and not train_text_encoder else False,
            "network_train_text_encoder_only": True if train_text_encoder and not train_unet else False,
            "training_comment": None,
        },
        "optimizer_arguments": {
            "min_snr_gamma": min_snr_gamma if not min_snr_gamma == -1 else None,
            "optimizer_type": optimizer_type,
            "learning_rate": unet_lr,
            "max_grad_norm": 1.0,
            "optimizer_args": eval(optimizer_args) if optimizer_args else None,
            "lr_scheduler": lr_scheduler,
            "lr_warmup_steps": lr_warmup_steps,
            "lr_scheduler_num_cycles": lr_scheduler_num_cycles if lr_scheduler == "cosine_with_restarts" else None,
            "lr_scheduler_power": lr_scheduler_power if lr_scheduler == "polynomial" else None,
        },
        "dataset_arguments": {
            "debug_dataset": False,
            "in_json": in_json,
            "train_data_dir": train_data_dir,
            "dataset_repeats": dataset_repeats,
            "shuffle_caption": True,
            "keep_tokens": keep_tokens,
            "resolution": resolution,
            "caption_dropout_rate": 0,
            "caption_tag_dropout_rate": 0,
            "caption_dropout_every_n_epochs": 0,
            "color_aug": False,
            "face_crop_aug_range": None,
            "token_warmup_min": 1,
            "token_warmup_step": 0,
        },
        "training_arguments": {
            "output_dir": output_dir,
            "output_name": project_name,
            "save_precision": save_precision,
            "save_every_n_epochs": save_n_epochs_type_value if save_n_epochs_type == "save_every_n_epochs" else None,
            "save_n_epoch_ratio": save_n_epochs_type_value if save_n_epochs_type == "save_n_epoch_ratio" else None,
            "save_last_n_epochs": None,
            "save_state": None,
            "save_last_n_epochs_state": None,
            "resume": None,
            "train_batch_size": train_batch_size,
            "max_token_length": 225,
            "mem_eff_attn": False,
            "xformers": True,
            "max_train_epochs": num_epochs,
            "max_data_loader_n_workers": 8,
            "persistent_data_loader_workers": True,
            "seed": seed if seed > 0 else None,
            "gradient_checkpointing": gradient_checkpointing,
            "gradient_accumulation_steps": gradient_accumulation_steps,
            "mixed_precision": mixed_precision,
            "clip_skip": clip_skip if not v2 else None,
            "logging_dir": logging_dir,
            "log_prefix": project_name,
            "noise_offset": noise_offset if noise_offset > 0 else None,
            "lowram": lowram,
        },
        "sample_prompt_arguments": {
            "sample_every_n_steps": None,
            "sample_every_n_epochs": 1 if enable_sample_prompt else 999999,
            "sample_sampler": sampler,
        },
        "saving_arguments": {
            "save_model_as": save_model_as
        },
    }

    for key in config:
        if isinstance(config[key], dict):
            for sub_key in config[key]:
                if config[key][sub_key] == "":
                    config[key][sub_key] = None
        elif config[key] == "":
            config[key] = None

    return toml.dumps(config)

def write_file(filename, contents):
    with open(filename, "w") as f:
        f.write(contents)

def execute():
    print("\ncreate config file.....-------------------------------------------------\n")
    try:
        model_config()
        dataset_config()
        lora_config()
        config_str = training_config()
        write_file(path.config_file, config_str)
        print(config_str)
    except Exception as e:
        raise Exception('create config file error !!!', e)
