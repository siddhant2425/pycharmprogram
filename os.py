import os

print(os.getcwd())
os.chdir(r"C:\Users\siddh\OneDrive\Desktop\classpractice")
print(os.getcwd())
print(os.listdir())
file=[file for file in os.listdir()if file.startswith('test.py')]
print(file)

with open('test.py')as fp:
    print(fp.read())