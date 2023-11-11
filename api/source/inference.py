from scripts import generate_image

try:
    generate_image.execute()
except Exception as e:
    print(e)
else:
    print("\ngenerate image done.")

