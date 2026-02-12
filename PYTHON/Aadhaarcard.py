def title(): 
        print("\t\t\tAadhaar Card Number Validation") 
        aad() 
def aad(): 
    global a 
    a = input("\nEnter Aadhaar Card Number : ") 
    for i in range(len(a)): 
            if (i==4 or i==9): 
                    continue 
            if  not a[i].isdigit(): 
                    print("\n\t\tInput Must Be Number") 
                    aad()       
    if len(a)==0: 
            print("\n\t\tIt is Null Input") 
            aad() 
    elif len(a)!=14: 
            print("\n\t\tIt Must Be 14th Number") 
            aad() 
    elif a[4]!=' ' or a[9]!=' ': 
            print("\n\t\tInput Must Have Space in 5th and 10th char") 
            aad() 
    elif a[0]=='1'or a[0]=='0': 
            print("\n\t\tThe Input Must Not Start with 1 and 0") 
            aad() 
    print("\n\n->The Given Aadhaar Card Number<< "+a+" >>is correct") 
    print("\n\n\t\t\tProgram Over...!!!") 
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
                    pass 
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