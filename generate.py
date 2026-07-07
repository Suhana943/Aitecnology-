import os

# फोल्डर बनाएं
os.makedirs("AITecnology_Pages", exist_ok=True)

for i in range(1, 144):
    filename = f"A{i}.html"
    next_page = f"A{i+1}.html" if i < 143 else "#"
    prev_page = f"A{i-1}.html" if i > 1 else "#"
    
    content = f"""<!DOCTYPE html>
<html>
<head><title>Page {i}</title></head>
<body>
    <h1>Yeh hai Page {i}</h1>
    <div class="navigation">
        <a href="{prev_page}">Pichla (Previous)</a> | 
        <a href="index.html">Home</a> | 
        <a href="{next_page}">Agla (Next)</a>
    </div>
</body>
</html>"""
    
    with open(f"AITecnology_Pages/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

print("143 files ban gayi hain!")
