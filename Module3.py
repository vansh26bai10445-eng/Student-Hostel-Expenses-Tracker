#module 3 for budget

def calc_balance(x,y):
    ans = x-y
    return ans

def show_report(n,c,y,i,e,b):
    print("name =",n)
    print("course =",c)
    print("year =",y)
    print("income =",i)
    print("expense =",e)
    if(b>0):
        print("saving =",b)
    if(b==0):
        print("bal is 0")
    if(b<0):
        print("loss =",b*-1)

def suggestions(f,e,m,b):
    if(e>1500):
        print("ent more")
    if(f>3000):
        print("food more")
    if(m>500):
        print("mobile more")
    if(b<0):
        print("over spending")
    else:
        print("ok this month")

def save_record(n,c,i,e,b):
    f=open("budget_record.txt","a")
    f.write(n+"\n")
    f.write(c+"\n")
    f.write(str(i)+"\n")
    f.write(str(e)+"\n")
    f.write(str(b)+"\n")
    f.close()
    print("saved")
