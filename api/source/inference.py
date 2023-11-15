from scripts import generate_image

try:
    generate_image.execute()
except Exception as e:
    raise Exception("inference error", e)
else:
    print("\ngenerate image done.")

