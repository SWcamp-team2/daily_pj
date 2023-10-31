import os
import glob
from PIL import Image
import os

def rename_images(directory_path, new_prefix):
    # Get a list of image files in the specified directory
    image_files = glob.glob(os.path.join(directory_path, '*.jpg'))  # Change the pattern as needed

    # Iterate through the image files and rename them
    for i, old_path in enumerate(image_files):
        # Create a new file name based on the prefix and index
        new_name = f"{new_prefix}_{i+1}.jpg"

        # Construct the new path
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)


def convert_png_to_jpg(png_path, jpg_path):
    # Open the PNG image
    with Image.open(png_path) as img:
        # Convert and save as JPG
        img.convert("RGB").save(jpg_path, "JPEG")

if __name__ == "__main__":
    # Specify the directory path and new prefix
    directory_path = os.getcwd() + "/dataset/normal/"
    new_prefix = "normal"

    # Call the function to rename images
    rename_images(directory_path, new_prefix)