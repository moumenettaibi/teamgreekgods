import os

def rename_images(folder_path):
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    # List all image files with common extensions
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    files = os.listdir(folder_path)
    images = [f for f in files if f.lower().endswith(image_extensions)]
    images.sort()  # Sort for consistent order

    # Rename images sequentially
    for i, image_name in enumerate(images, start=1):
        new_name = f"press-{i}.png"
        old_path = os.path.join(folder_path, image_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
    print(f"Renamed {len(images)} images in '{folder_path}'.")

if __name__ == "__main__":
    folder = input("Please enter the full path of the folder containing your images: ")
    rename_images(folder)
