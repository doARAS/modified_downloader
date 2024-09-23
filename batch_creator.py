import os
import shutil

source_folder = 'meta_info'
target_folder = 'target_folder'

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

batch_size = 50

for i in range(0, len(files), batch_size):
    batch_files = files[i:i + batch_size]
    batch_folder = os.path.join(target_folder, f'batch_{i // batch_size + 1}')
    os.makedirs(batch_folder, exist_ok=True)
    
    for file in batch_files:
        shutil.move(os.path.join(source_folder, file), os.path.join(batch_folder, file))

print("Files have been successfully separated into batches.")
