"""
Write a Python program to triple all numbers of a given list of integers. Use Python map.
sample list: [1, 2, 3, 4, 5, 6, 7]
Triple of list numbers:
[3, 6, 9, 12, 15, 18, 21]
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
    return lst*3

lst=values()
print("sample list:",lst)
data=list(map(sq,lst))
print("sample output:",data)