import json
import shutil
import os

# 1. JSON data load karein
with open('data.json', 'r') as f:
    articles = json.load(f)

# 2. Template file load karein (A1.html jismein placeholders hon)
with open('A1.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 3. 146 files generate karne ka loop
for i, article in enumerate(articles):
    file_num = i + 1
    new_filename = f"A{file_num}.html"
    
    # Image sequence ka logic (1 se 16 ka cycle)
    img_num = (i % 16) + 1
    image_name = f"A{img_num}.png"
    
    # Template mein content replace karna
    # Dhyan rahe: A1.html mein {{TITLE}} aur {{IMAGE_SRC}} likha hona chahiye
    new_content = template.replace('{{TITLE}}', article['title'])
    new_content = new_content.replace('{{IMAGE_SRC}}', image_name)
    
    # Nayi file save karein
    with open(new_filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"File {new_filename} ban gayi jisme image hai: {image_name}")

print("Saari 146 files successfully process ho gayi hain!")
