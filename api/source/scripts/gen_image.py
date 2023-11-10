import os, subprocess
from scripts.utils import path, util

# @markdown ### LoRA Config
# @markdown Currently, `LoHa` and `LoCon_Lycoris` are not supported. Please run `Portable Web UI` instead
network_weight = path.output_dir + "/chillout_1000.safetensors"  # @param {'type':'string'}
network_mul = 0.7  # @param {type:"slider", min:-1, max:2, step:0.05}
network_module = "networks.lora"
network_args = ""

# @markdown ### <br> General Config
v2 = False  # @param {type:"boolean"}
v_parameterization = False  # @param {type:"boolean"}
#prompt = "tiu, 1girl, solo, looking at viewer, short hair, bangs, simple background, shirt, black hair, white background, brown eyes, jewelry, earrings, black eyes, lips, black shirt, traditional media, portrait, realistic"  # @param {type: "string"}
#negative = "low quality, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"  # @param {type: "string"}
model = path.model_dir # @param {type: "string"}
vae = ""  # @param {type: "string"}
outdir = path.result_dir  # @param {type: "string"}
scale = 7  # @param {type: "slider", min: 1, max: 40}
sampler = "ddim"  # @param ["ddim", "pndm", "lms", "euler", "euler_a", "heun", "dpm_2", "dpm_2_a", "dpmsolver","dpmsolver++", "dpmsingle", "k_lms", "k_euler", "k_euler_a", "k_dpm_2", "k_dpm_2_a"]
steps = 28  # @param {type: "slider", min: 1, max: 100}
precision = "fp16"  # @param ["fp16", "bf16"] {allow-input: false}
width = 512  # @param {type: "integer"}
height = 512  # @param {type: "integer"}
images_per_prompt = 4  # @param {type: "integer"}
batch_size = 4  # @param {type: "integer"}
clip_skip = 2  # @param {type: "slider", min: 1, max: 40}
seed = -1  # @param {type: "integer"}

#final_prompt = f"{prompt} --n {negative}"
final_prompt = path.prompt_file

config = {
    "v2": v2,
    "v_parameterization": v_parameterization,
    "network_module": network_module,
    "network_weight": network_weight,
    "network_mul": float(network_mul),
    "network_args": eval(network_args) if network_args else None,
    "ckpt": model,
    "outdir": outdir,
    #"xformers": True,
    "vae": vae if vae else None,
    #"fp16": True,
    "bf16": True,
    "W": width,
    "H": height,
    "seed": seed if seed > 0 else None,
    "scale": scale,
    "sampler": sampler,
    "steps": steps,
    "max_embeddings_multiples": 3,
    "batch_size": batch_size,
    "images_per_prompt": images_per_prompt,
    "clip_skip": clip_skip if not v2 else None,
    #"prompt": final_prompt,
    "from_file": final_prompt
}

def execute():
    print("\nimage infernece start.....-----------------------------------------------\n")
    args = util.train(config)
    final_args = f"python3 gen_img_diffusers.py {args}"
    os.chdir(path.root_dir)
    try:
        subprocess.run(final_args, shell=True, check=True)
    except Exception as e:
        raise Exception('image inference error !!!', e)
