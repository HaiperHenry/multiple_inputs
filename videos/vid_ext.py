import shutil
import os

def duplicate_and_suffix_mp4_files(directory, suffixes):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and filename.endswith(".mp4"):
            # Get the file's extension
            name, file_extension = os.path.splitext(filename)

            # Create copies with the specified suffixes
            for i, suffix in enumerate(suffixes, 1):
                new_filename = f"{name}{suffix}{file_extension}"
                shutil.copy(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Copy {i} of {filename}: {new_filename}")

if __name__ == "__main__":
    directory = "."  # Current directory
    suffixes = ["_TM", "_SM", "_SME", "_SMEF", "_BM", "_BME", "_BMEF"]

    duplicate_and_suffix_mp4_files(directory, suffixes)
