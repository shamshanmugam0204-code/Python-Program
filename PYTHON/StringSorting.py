def title(): 
    print("\n\t\t\t     SORTING OF WORDS") 
    print("\n\t\t\t\t\t\t\tDone by: S.Shamkumar") 
    Num() 
def Num(): 
    global S,s 
    S=[] 
    for i in range(5): 
        si=input("\n>> Enter The Number  "+str(i+1)+" :") 
        if len(si)!=0: 
            if si.isalpha(): 
                S.append(si) 
            else: 
                print("\n\t\tOnly Alphabet Will Accept") 
                Num() 
        else: 
            print("\n\t\tNull Input Will Not Accept") 
            Num() 
    print("-"*80)     
    AD() 
def AD(): 
    global ad 
    S.sort() 
    ad=input('\n\n->Enter the type of sorting you wishing to(A/D):') 
    if len(ad)!=0: 
        if len(ad)==1: 
            if ad[0]=='a'or ad[0]=='A' or ad[0]=='d' or ad[0]=='D': 
                 
                if(ad[0]=='a'or ad[0]=='A'): 
                     Sort1() 
                else: 
                    print('\n\n\t\t        |DESCENDING ORDER|') 
                    Sort2()         
            else: 
                print('Input must be either A/D') 
                AD() 
        else: 
            print("\n\t\tIt Must Be 1char ") 
            AD() 
    else: 
        print("\n\t\tNull input will not accept") 
        AD() 
def Sort1(): 
    print('\n\n\t\t        |ASCENDING ORDER|') 
    for i in S: 
        print("<<",i,">>")  
    print("\n\t\t\t Program over..!!!") 
    print("\n\t\t      **********************") 
    yesno() 
def Sort2(): 
    S.reverse() 
    for i in S: 
        print("<<",i,">>") 
    print("\n\t\t\t Program over..!!!") 
    print("\n\t\t      **********************") 
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