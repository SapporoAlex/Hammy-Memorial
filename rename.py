import os

def rename_files(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Sort files so numbering is consistent
    files.sort()

    # Loop through and rename
    for i, filename in enumerate(files, start=1):
        # Get file extension
        _, ext = os.path.splitext(filename)
        # Create new name
        new_name = f"hammy{i}{ext.lower()}"
        # Build full paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        print(f"Renaming: {filename} -> {new_name}")
        os.rename(old_path, new_path)

if __name__ == "__main__":
    folder = r"C:\Users\McKinley Alex\Desktop\Programming\JS\hammyMemorial\hammy"  # 🔹 change this to your folder
    rename_files(folder)
