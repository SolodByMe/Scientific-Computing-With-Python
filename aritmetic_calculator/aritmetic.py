from msilib.schema import Error
import numpy as np

def length_checker(s):
    return len(s)

def suma(n1,n2):
    return str(int(n1)+int(n2))

def resta(n1,n2):
    return str(int(n1)-int(n2))
def space_add(s):
    if length_checker(s)==4:
        s = " " + " " + s
        return s
    elif length_checker(s)==3:
        s=" " + " " + " " + s
        return s
    elif length_checker(s)==2:
        s= " " + " " + " "+ " " + s
        return s
    elif length_checker(s)==1:
        s= " " + " " + " " + " " + " "+ s
        return s

def print_bar(length):
    print("-"*length)

def plus_appear(s):
    if s.find("+")>=0:
        return True
    else: return False

def minus_appear(s):
    if s.find("-")>=0:
        return True
    else: return False

def number_checker(number):
    if plus_appear(number):
        while True:
            try: 
                n1_s=number.split("+")[0]
                n2_s=number.split("+")[1]
                n1=int(number.split("+")[0])
                n2=int(number.split("+")[1])
                if (len(n1_s) and len(n2_s))<=4:
                    return True
                else: 
                    print("Error: Numbers cannot be more than four digits")
            except ValueError:
                print("Error: Numbers must only contain digits")
                return False
                break
            
    elif minus_appear(number):
        while True:
            n1=number.split("-")[0]
            try: 
                n1=int(number.split("-")[0])
                n2=int(number.split("-")[1])
                return True
            except ValueError:
                print("Error: Numbers must only contain digits")
                break

def espaciado_suma(s1,s2):
    if len(s1)==len(s2):
        s1="  "+s1
        s2="+ "+s2
        print(s1)
        print(s2)
        print("-"*len(s1))
    elif len(s1)>len(s2):
        aux=len(s1)-len(s2)
        s1="  "+s1
        s2="+ "+" "*aux+s2
        print(s1)
        print(s2)
        print("-"*len(s1))
    elif len(s1)<len(s2):
        aux=len(s2)-len(s1)
        s1="  "+" "*aux+s1
        s2="+ "+s2
        print(s1)
        print(s2)
        print("-"*len(s2))

def espaciado_resta(s1,s2):
    if len(s1)==len(s2):
        s1="  "+s1
        s2="- "+s2
        print(s1)
        print(s2)
        print("-"*len(s1))
    elif len(s1)>len(s2):
        aux=len(s1)-len(s2)
        s1="  "+s1
        s2="- "+" "*aux+s2
        print(s1)
        print(s2)
        print("-"*len(s1))
    elif len(s1)<len(s2):
        s1="  "+" "*(len(s2)-len(s1))+s1
        s2="- "+s2
        print(s1)
        print(s2)
        print("-"*len(s2))

def arithmetic(sum):
    if number_checker(sum)==True:
        if (plus_appear(sum)):
            split=sum.split("+")
            espaciado_suma(split[0],split[1])
            print("  "+suma(split[0],split[1]))
            print("\n")
        elif (minus_appear(sum)):
            split=sum.split("-")
            espaciado_resta(split[0],split[1])
            if(int(split[0])-int(split[1])<0):
                print(" "+resta(split[0],split[1]))
            else:
                print("  "+resta(split[0],split[1]))
            print("\n")
        else:
            print("Error: Operator must be '+' or '-'")

def arithmetic_arranger(lista):
    if len(lista)>5:
        print("Error: Too many problems")
    else:
        for i in range(0,len(lista)):
            arithmetic(lista[i])

arithmetic_arranger(["123-7","324+85","4-623","5-21","9+32"])
    