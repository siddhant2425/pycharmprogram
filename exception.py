


try:
    sjkafjk
    x = 'test.txt'
    open('x', 'r')
    a=10
    b=0
    c=a/b
    print(c)



except (ZeroDivisionError,FileNotFoundError,NameError) as msg:
    print("General errror::",msg)
finally:
    print("Thank you")
