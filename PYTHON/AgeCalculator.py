import re 
def title(): 
    print("\n\t\t\t     Data Birth Validation") 
    print("\n\t\t\t\t\t\t\tDone by: S.Shamkumar") 
    dob() 
def dob(): 
    global a 
    a=input("\n\n-->Enter The Data Of Birith:") 
    if len(a)!=0: 
        if len(a)==10: 
            if a[2]=='/'and a[5]=='/': 
                if re.match(r"^\d{2}[/]\d{2}[/]\d{4}$",a): 
                    correct()    
                else: 
                    print("\n\t\tIt is Valid") 
                    dob() 
            else: 
               print("\n\t\tThe Symbol Should Mention Or Use In Correct Place ") 
               dob() 
        else: 
            print("\n\t\tThe Input Not Be Less Then or Greater Then 10") 
            dob() 
    else: 
        print("\n\t\tNull Input Will Not Accept") 
        dob() 
def correct(): 
    global bd,bm,by 
    bd=int(a[0:2]) 
    bm=int(a[3:5]) 
    by=int(a[6:10]) 
    if bd>=1 and bd<=31: 
        if bm>=1 and bm<=12: 
            if by>=1950 and by<=2024: 
                today() 
            else: 
                print("\n\t\tYear Must Greater then 1950 less then 2024") 
                dob() 
        else: 
            print("\n\t\tMonth Must greater then 1 and less then 12") 
            dob() 
    else: 
        print("\n\t\tDate Must greater then 1 and less then 31") 
        dob()         
def today(): 
    global b 
    b=input("\n\n-->Enter Today Day: ") 
    if len(b)!=0: 
        if len(b)==10: 
            if b[2]=='/'and b[5]=='/': 
                if re.match(r"^\d{2}[/]\d{2}[/]\d{4}$",b): 
                    use()    
                else: 
                    print("\n\t\tIt is Valid") 
                    today() 
            else: 
               print("\n\t\tThe Symbol Should Mention Or Use In Correct Place ") 
               today() 
        else: 
            print("\n\t\tThe Input Not Be Less Then or Greater Then 10") 
            today() 
    else: 
        print("\n\t\tNull Input Will Not Accept") 
        today() 
def use(): 
    global td,tm,ty 
    td=int(b[0:2]) 
    tm=int(b[3:5]) 
    ty=int(b[6:10]) 
    if td>=1 and td<=31: 
        if tm>=1 and tm<=12: 
            if ty==2026: 
                daycheck()                 
            else: 
                print("\n\t\tYear Must Be only 2026") 
                today() 
        else: 
            print("\n\t\tMonth Must greater then 1 and less then 12") 
            today() 
    else: 
        print("\n\t\tDate Must greater then 1 and less then 31") 
        today() 
def daycheck(): 
    global day 
    if td>bd: 
        day=td-bd 
        moncheck() 
    else:#bd<td: 
        day=bd-td 
        moncheck() 
def moncheck(): 
     global mon 
     if tm>bm: 
        mon=tm-bm 
        yearcheck() 
     else: 
         mon=bm-tm 
         yearcheck() 
def yearcheck(): 
    global yer 
    yer=ty-by 
    Age() 
def Age(): 
    print(day,'days',mon,'months',yer,'years') 
    print("\n\n\t\t\t  Program Over...!!!") 
    print("\n\t\t     ============================") 
    yesno() 
def yesno(): 
    b=input("\n\n>>Do you want run again (y/n):") 
    if len(b)!=0: 
        if len(b)==1: 
            if (b[0]=='y'or b[0]=='y')or(b[0]=='n'or b[0]=='N'): 
                if b[0]=='y' or b[0]=='Y': 
                        title() 
                else: 
                    print("\n\n\t\t\t\tThank You") 
            else: 
                print("\n\t\tInput Must Only Be (y/n)") 
                yesno() 
        else: 
            print("\n\t\tIt Must Be only 1 char Number") 
            yesno() 
    else:         
        print("\n\t\tIt is Null Input") 
        yesno() 
title()