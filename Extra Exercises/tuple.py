# tuple → [] = collection which is ordered and unchangeable, used to group together related data

student = ("Trevi", 36, "male")

print(student.count("Trevi"))
print(student.count(36))
print(student.count("iverT"))
print(student.index("male"))

for x in student:
    print(x)

if "Trevi" in student:
    print("Keep Pounding!")
