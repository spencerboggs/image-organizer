import os
from PIL import Image

def rename_and_convert_images(folder_path):
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    output_folder = os.path.join(folder_path, "converted_images")
    os.makedirs(output_folder, exist_ok=True)

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    files.sort(key=lambda f: os.path.getctime(os.path.join(folder_path, f)))

    image_count = 1

    for file_name in files:
        input_path = os.path.join(folder_path, file_name)
        ext = os.path.splitext(file_name)[1].lower()

        if ext in ['.png', '.jpg', '.jpeg']:
            new_file_name = f"image{image_count}.png"
            output_path = os.path.join(output_folder, new_file_name)

            if ext in ['.jpg', '.jpeg']:
                try:
                    with Image.open(input_path) as img:
                        img.convert('RGBA').save(output_path, 'PNG')
                        print(f"Converted and renamed: {file_name} -> {new_file_name}")
                except Exception as e:
                    print(f"Error converting {file_name}: {e}")
            else:
                try:
                    os.rename(input_path, output_path)
                    print(f"Renamed: {file_name} -> {new_file_name}")
                except Exception as e:
                    print(f"Error renaming {file_name}: {e}")

            image_count += 1

    print("Processing complete. Check the 'converted_images' folder for results.")

folder_path = input("Enter the path to the folder containing images: ")
rename_and_convert_images(folder_path)
