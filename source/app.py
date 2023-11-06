import generate_tag
import do_train

try:
    generate_tag.execute()
    do_train.execute()
except Exception as e:
    print(e)
else:
    print("\ntraining done.")
