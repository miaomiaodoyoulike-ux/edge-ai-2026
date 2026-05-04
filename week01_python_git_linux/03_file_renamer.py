#统一加前缀day01_
files = ["report.txt", "data.csv", "notes.md", "image.png", "code.py"]#创建一个文件名列表
print("Original Filenams: ")
for name in files:
    print(name)
print("_"*20)
print("Renamed Filenames:")
for name in files:
    new_name = "day01_" + name
    print(f"{name}->{new_name}")

