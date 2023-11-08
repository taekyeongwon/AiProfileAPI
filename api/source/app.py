from scripts import generate_tag, create_meta, prepare_buckets_latents, create_config, do_train

try:
    #4. Data Processing
    #4.2.2 Waifu Diffusion 1.4 Tagger V2
    generate_tag.execute()
    #4.3 Create Metadata File
    create_meta.execute()
    #4.4 Bucketing and Latents Caching
    prepare_buckets_latents.execute()

    #5. Training Model
    #5.1 ~ 5.4 Model Config
    create_config.execute()
    #5.5 Start Training
    do_train.execute()
except Exception as e:
    print(e)
else:
    print("\ntraining done.")
