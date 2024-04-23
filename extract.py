import zipfile,os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def extract_and_append_zip_part(part_num, zip_filename_prefix, num_parts):
    with open(f"{zip_filename_prefix}.{part_num:03d}", 'rb') as part_file:
        return part_file.read()

def extract_multi_part_zip(zip_filename_prefix, num_parts):
    with ThreadPoolExecutor(max_workers=num_parts) as executor:
        part_contents = list(executor.map(lambda part_num: extract_and_append_zip_part(part_num, zip_filename_prefix, num_parts), range(1, num_parts + 1)))

    with open(zip_filename_prefix, 'wb') as combined_zip_file:
        for part_content in part_contents:
            combined_zip_file.write(part_content)

    with zipfile.ZipFile(zip_filename_prefix, 'r') as zip_ref:
        total_files = len(zip_ref.infolist())
        with tqdm(total=total_files, desc="Extracting") as pbar:
            for file_info in zip_ref.infolist():
                zip_ref.extract(file_info, path=None)
                pbar.update(1)

    os.remove(zip_filename_prefix)

    print(f"Extracted contents from {zip_filename_prefix}")

zip_filename_prefix = 'TryOn.zip'
num_parts = 10

extract_multi_part_zip(zip_filename_prefix, num_parts)
