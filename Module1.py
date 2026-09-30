# module 1

def student_details():
    print("enter name")
    n = input()
    print("enter course")
    c = input()
    print("enter year")
    y = input()
    return n,c,y

def get_income():
    print("pocket money")
    p = float(input())
    print("scholarship")
    s = float(input())
    print("job money")
    j = float(input())
    t = p+s+j
    print("total income",t)
    return p,s,j,t
