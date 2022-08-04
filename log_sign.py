import json
print("press 1 for signup!!!")
print("press 2 for login!!!")
start=int(input("press the button:-"))
if start==1:
    username=input("create username:-")
    password1=input("create password:-")
    digit,special,lower,upper=0,0,0,0
    if len(password1)>=6:
        for i in password1:
            if(i.isupper()):
                upper=1
            if (i.islower()):
                lower=1
            if (i.isdigit()):
                digit=1
            if(i=="@" or i=="$" or i=="&" or "%"):
                special=1
        total=upper+lower+digit+special
        if total!=4:
            print("please use atleast one capital letter ,small letter,one digit and one special character:- ")
        else:
            password2=input("confirm password:-")
            if password1!=password2:
                print("password dont match, restart")
            else:
                gender=input("enter your gender male or female")
                bio=input("enter your bio")
                dob=input("enter a dob")
                dic={}
                l=[]
                dic['name']=username
                dic['password']=password1
                dic['gender']=gender
                dic['bio']=bio
                dic['dob']=dob

                l.append(dic)
                c=json.dumps(l,indent=4)
                f2=open("database.json","a")
                f2.writelines(c)
                f2.close()
            print("cong")
    else:
        print("your password length is too short")
else:
    if start==2:
        print("log in")
        username1=input("enter a username")
        pasword3=input("enter your password")
        confirm_password=input("enter your confirm password")
        digit,special,lower,upper=0,0,0,0
        if len(pasword3)>=8:
            for i in pasword3:
                if(i.isupper()):
                    upper=1
                if (i.islower()):
                    lower=1
                if (i.isdigit()):
                    digit=1
                if(i=="@" or i=="$" or i=="&" or "%"):
                    special=1
            t=upper+lower+digit+special
            if t==4:
                print("logged in sucessfully")
            else:
                print("your password is wrong")
        else:
            print("login error")
            with open("database.json","a") as h:
                json.dump("f",h,indent=4)
    else:
        print("you are out of the game")