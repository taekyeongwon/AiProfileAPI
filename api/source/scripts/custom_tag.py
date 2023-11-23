import os

# @markdown Add or remove custom tags here. You can refer to this [cheatsheet](https://rentry.org/kohyaminiguide#c-custom-tagscaption) for more information.
extension = ".txt"  # @param [".txt", ".caption"]
custom_tag = os.getenv('CUSTOM_TAG')  # @param {type:"string"}
# @markdown Enable this to append custom tags at the end of lines.
append = False  # @param {type:"boolean"}
# @markdown Enable this if you want to remove captions/tags instead.
remove_tag = False  # @param {type:"boolean"}
recursive = False
image_dir = os.getenv('TRAIN_DATA_DIR')

def read_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def write_file(filename, contents):
    with open(filename, "w") as f:
        f.write(contents)

def process_tags(filename, custom_tag, append, remove_tag):
    contents = read_file(filename)
    tags = [tag.strip() for tag in contents.split(',')]
    custom_tags = [tag.strip() for tag in custom_tag.split(',')]

    for custom_tag in custom_tags:
        custom_tag = custom_tag.replace("_", " ")
        if remove_tag:
            while custom_tag in tags:
                tags.remove(custom_tag)
        else:
            if custom_tag not in tags:
                if append:
                    tags.append(custom_tag)
                else:
                    tags.insert(0, custom_tag)

    contents = ', '.join(tags)
    write_file(filename, contents)
    print(f"custom tag : {contents}")

def process_directory(image_dir, tag, append, remove_tag, recursive):
    for filename in os.listdir(image_dir):
        file_path = os.path.join(image_dir, filename)

        if os.path.isdir(file_path) and recursive:
            process_directory(file_path, tag, append, remove_tag, recursive)
        elif filename.endswith(extension):
            process_tags(file_path, tag, append, remove_tag)

if not any(
    [filename.endswith(extension) for filename in os.listdir(image_dir)]
):
    for filename in os.listdir(image_dir):
        if filename.endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp")):
            open(
                os.path.join(image_dir, filename.split(".")[0] + extension),
                "w",
            ).close()

def execute():
    print("\nappend custom tag.....-------------------------------------------------\n")
    tag = custom_tag

    if custom_tag:
        process_directory(image_dir, tag, append, remove_tag, recursive)

    print("custom tag done.")
