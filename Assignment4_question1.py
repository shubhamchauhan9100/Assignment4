"""
Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
sample input: 10
sample output: 35
"""
sample=int(input("Enter sample input:"))
data=lambda sample:25+sample
print("sample output:",data(sample))