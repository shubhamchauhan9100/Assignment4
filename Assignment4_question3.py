"""
Write a Python program to square the elements of a list using map() function.
Sample List: [4, 5, 2, 9]
Square the elements of the list:
[16, 25, 4, 81]
"""
def values():
    lst=[]
    entermore="y"
    while(entermore=="y"):
        num=int(input("enter a no. in lst\n"))
        lst.append(num)
        entermore=input("Do you want to enter more no. in list?  y/n \n")
    return lst

def sq(lst):
    return lst**2

lst=values()
print("sample list:",lst)
data=list(map(sq,lst))
print("Square the elements of the list:\n",data)