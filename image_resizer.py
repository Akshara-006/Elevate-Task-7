import os
from PIL import Image

input_folder = r'C:\Users\Lenovo\OneDrive\Pictures\Screenshots'            
output_folder = 'resized_images'  
target_size = (800, 600)           
output_format = 'JPEG'            

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.' + output_format.lower())

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size)
                resized_img.convert('RGB').save(output_path, output_format)
                print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")