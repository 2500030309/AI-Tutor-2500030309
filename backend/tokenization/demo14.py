
n=int(input("Enter number of entries: "))

student = {}
for i in range(n):
    key=input("Enter key: ")
    Value=input("Enter value: ")
    student[key]=Value

print(student)