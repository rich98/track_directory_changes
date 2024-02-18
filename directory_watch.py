import os
import hashlib

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def monitor_changes(directory_path):
    hashes = {}
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_hash = calculate_md5(file_path)
            if file_path not in hashes:
                hashes[file_path] = file_hash
            elif hashes[file_path] != file_hash:
                print(f"File {file_path} has been modified.")
                hashes[file_path] = file_hash

monitor_changes('YOUR_DIRECTORY_PATH')
