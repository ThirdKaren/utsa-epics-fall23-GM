import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    # Sort the image files to ensure sequential renaming
    image_files.sort()

    # Rename images sequentially
    for i, old_name in enumerate(image_files, start=1):
        extension = os.path.splitext(old_name)[1]
        new_name = f"german_{i:03d}{extension}"
        new_path = os.path.join(folder_path, new_name)

        counter = 1
        while os.path.exists(new_path):
            new_name = f"german{i:03d}_{counter:02d}{extension}"
            new_path = os.path.join(folder_path, new_name)
            counter += 1
        
        old_path = os.path.join(folder_path, old_name)
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\germa\\OneDrive\\Phtos"  # Replace with your folder path
    rename_images(folder_path)