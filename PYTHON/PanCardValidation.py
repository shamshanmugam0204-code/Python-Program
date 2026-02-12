def title(): 
    print("\n\t\t\t     Pan Card Validation") 
    print("\n\t\t\t\t\t\t\tDone by: S.Shamkumar") 
    pan1() 
def pan1(): 
    global p1 
    p1=input("\n\n>>Enter Characters (between AAA to AAZ): ") 
    if len(p1)!=0: 
        if len(p1)==3: 
             if p1[0]=='A' and p1[1]=='A' or p1[0]=='a' and p1[1]=='a' and p1[2].isalpha(): 
                 pan2() 
             else: 
                  print("\n\t\tInput should be between AAA to AAZ") 
                  pan1() 
        else: 
            print("\n\t\tInput Must Contian 3 char") 
            pan1() 
    else: 
         print("\n\t\tNull Input Not Accept") 
         pan1()             
def pan2(): 
    global p2 
    p2=input("\n\n>>Enter the Type of User from (1 to 10):") 
    if len(p2)!=0: 
        if p2.isdigit(): 
            if int(p2)>=1 and int(p2)<=10: 
                pan_2() 
            else: 
                print("\n\t\tInput other than between 1 to 10 will not accept") 
                pan2() 
        else: 
            print("\n\t\tInput Must Be Number") 
            pan2()     
    else: 
        print("\n\t\tNull Input  Not Accept") 
        pan2()        
def pan_2(): 
    global A,p0 
    p0=int(p2) 
    if (p0==1): 
        A="P" 
    elif (p0==2): 
        A="C" 
    elif(p0==3): 
        A="H" 
    elif(p0==4): 
        A="A" 
    elif(p0==5): 
        A="B" 
    elif(p0==6): 
        A="G" 
    elif(p0==7): 
        A="J" 
    elif(p0==8): 
        A="L" 
    elif(p0==9): 
        A="F" 
    elif (p0==10): 
        A="T" 
    pan3()     
def pan3(): 
    global p3 
    p3=input("\n\n>>Enter your Name                      : ") 
    if len(p3)!=0: 
        if p3.isalpha(): 
            if p3=="sham": 
                pan4() 
            else: 
                print("\n\t\tEnter Correct Input ") 
                pan3() 
        else: 
            print("\n\t\tThe given input is wrong enter your correct name") 
            pan3() 
    else: 
        print("\n\t\tNull input will not accept") 
        pan3() 
def pan4(): 
    global p4 
    p4=input("\n\n>>Enter your PAN Card no.(0001 to 9999): ") 
    if len(p4)!=0: 
        if len(p4)==4: 
            if p4.isdigit(): 
                if p4>='0001' and p4<='9999': 
                    pan5() 
                else: 
                    print("\n\t\tInput other than between 0001 to 9999 will not accept") 
                    pan4() 
            else: 
                print("\n\t\tThe Input Must Be Number") 
                pan4() 
        else: 
            print("\n\t\tInput must be 4 digit") 
            pan4() 
    else: 
        print("\n\t\tNull input will not accept") 
        pan4() 
def pan5(): 
    global p5 
    p5=input("\n\n>>Enter Last Character of your PAN Card: ") 
    if len(p5)!=0: 
        if len(p5)==1: 
            if p5.isalpha(): 
                correct() 
            else: 
                print("\n\t\tThe input should be alphabet") 
                pan5() 
        else: 
            print("\n\t\tThe given input must be 1 char") 
            pan5() 
    else: 
        print("\n\t\tNull input will not accept") 
        pan5() 
def correct():  
    print("\n\n\t      Entered the pan card "+p1.upper()+A+p3[0].upper()+p4+p5.upper()+" is Valid...!!!") 
    print("\n\n\t\t            Program Over....!!!!") 
    print("\n\t\t        ==========================") 
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
 
 OUTPUT 
 