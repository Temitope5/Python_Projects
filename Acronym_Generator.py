user_input = str(input("Enter a Phrase:" ))
text = user_input.split()
a= " "
for t in text:
    a = a +str(t[0]).upper()
print(a)