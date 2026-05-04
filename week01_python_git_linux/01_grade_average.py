
# 01_grade_average_py
grades = [85,90,78,92,88]
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)
print("Build-in function result:")
print(f"Average: {average:.2f}")#用 f-string 输出变量,print(f"文字 {变量}"),:.2f保留两位小数
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print("-"*20)
total=0
for grade in grades:#注意了，这里要加冒号
    total += grade

average_manual = total/len(grades)
print("Manual loop result:")
print(f"Total: {total}")
print(f"Average: {average_manual:.2f}")