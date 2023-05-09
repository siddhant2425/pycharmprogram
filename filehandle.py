

with open('testing.txt','w+') as fp:

    fp.write("hi demo for w+")
    fp.seek(0)
    print(fp.tell())
    data=fp.read()
    print(data)
    print(fp.tell())