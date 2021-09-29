"""Quiz: len, max, min, and Lists

→ What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)"""

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)])) # 4
print(min([len(a), len(b), len(c)])) # 2

"""
→ What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)"""

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names))) # Albert & Ben & Carol & Donna

"""
→ What would the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)"""

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names)) # ["Albert", "Ben", "Carol", "Donna", "Eugenia"]


