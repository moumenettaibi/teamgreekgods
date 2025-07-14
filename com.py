import os
from PIL import Image

# Folder containing your WebP images
input_folder = input("path/to/your/webp_images: ")
output_folder = input("path/to/compressed_images: ")
compression_quality = 80  # Set between 0 (worst) and 100 (best)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.webp'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        with Image.open(input_path) as img:
            img.save(output_path, 'webp', quality=compression_quality, method=6, optimize=True)
        print(f"Compressed: {filename} -> {output_path}")
