import shutil
import os

# Original template file ka naam
template = "A1.html"

# 1 se 146 tak loop chalayein
for i in range(1, 147):
    new_filename = f"A{i}.html"
    # A1.html ko copy karke naya naam dein
    shutil.copy(template, new_filename)
    print(f"{new_filename} ban gayi!")

print("Saari 146 files successfully ban gayi hain.")
