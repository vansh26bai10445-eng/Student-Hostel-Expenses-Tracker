# module 2

def get_expenses():
    print("food expense")
    f = float(input())
    print("books")
    b = float(input())
    print("travel")
    tr = float(input())
    print("mobile")
    m = float(input())
    print("entertainment")
    e = float(input())
    print("other")
    o = float(input())
    tot = f+b+tr+m+e+o
    print("total expense",tot)
    return f,b,tr,m,e,o,tot

def extra_expense(o,tot):
    print("extra expense? yes or no")
    x = input()
    if x=="yes":
        print("enter amount")
        a = float(input())
        print("reason")
        r = input()
        o = o+a
        tot = tot+a
        print("added")
    return o,tot
