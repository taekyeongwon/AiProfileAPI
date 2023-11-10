from scripts import gen_image

try:
    gen_image.execute()
except Exception as e:
    print(e)
else:
    print("\ngenerate image done.")

