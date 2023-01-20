'''
An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing.
This Python program creates acronyms
'''

user_input = str(input("Enter a Phrase:" ))
text = user_input.split()
a= " "
for t in text:
    a = a +str(t[0]).upper()
print(a)

# This is another alternative to this problem

user_input=str(input("Enter a Phrase:" ))
text= user_input.split()
first_letters= [word[0].upper()for word in text]
a= "".join(first_letters)
print(a)