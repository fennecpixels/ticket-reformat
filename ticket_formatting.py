import re
original = input("What is the file you want reformatted? ").strip()
with open(original,'r') as f:
    lines = f.readlines()
with open(f"OUTPUT_{original}.txt",'a+') as f:
    for line in lines:
        x = re.sub(r'\[\d{4} \w{3} \d{2} \d{2}:{1}\d{2}:{1}\d{2}\] ',"",line)
        x = re.sub(r' \(\d{18}\):{1}',":",x)
        if x != line:
            f.write(x)
        else:
            f.write(line)

print(f"{original} has been reformatted.")