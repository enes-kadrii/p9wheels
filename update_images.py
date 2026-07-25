import os
import re

dir_path = '.'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. replace 'images22/f0...' with 'images/...' (since all new JPGs are in assets/images)
    new_content = re.sub(r'images22/f0?(\d+)\.png', r'images/\1.jpg', content)
    
    # 2. replace 'images/f...' with 'images/...'
    new_content = re.sub(r'images/f0?(\d+)\.png', r'images/\1.jpg', new_content)
    
    # 3. replace any raw 'f01.png' in gallery.html array
    new_content = re.sub(r'["\']f0?(\d+)\.png["\']', r'"\1.jpg"', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk(dir_path):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.js'):
            process_file(os.path.join(root, file))

print("Done")
