Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("enter the character:")
enter the character:e
>>> if (a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U"):
    print("The character is vowel")
else:
    print("the character is consonants")

    
The character is vowel
>>> a=int(input("enter the no of days:"))
enter the no of days:10
>>> if a<=5:
    b=a*2
    print("total fees",b)
elif a>=6 and a<=10:
    c=a*3
    print("total fees",c)
elif a>=11 and a<=15:
    d=a*4
    print("total fees",d)
else:
    e=a*5
    print("total fees",e)

    
total fees 30
>>> a=int(input("enter the number:"))
enter the number:3
>>> if a%2!=0:
    print("WEIRD")
elif a%2==0:
    if a==2 or a==3 or a==4 or a==5:
        print("NOT WEIRD")
    elif a>20:
        print("NOT WEIRD")

        
WEIRD
>>> 