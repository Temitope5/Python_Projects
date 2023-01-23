import random

when= ['A few years ago','Yesterday','Last night','Two months ago','A long time ago','On 6th May']
what = ['a cat', 'a dog', 'an elephant', 'a sheep', 'a puppy', 'a kitten']
name= ['Taiwo','Sandra', 'Julia','Emily','Edward','Joe']
residence= ['Lagos', 'Abuja','Kano', 'Bayelsa', 'Katsina', 'Jos']
went = ['cinema','mall','seminar', 'museum','party']
happened= ['made a lot of friends', 'Ate a burger','solved a mystery','found the missing item','met the missing dad','dicovered a gold spot']

print(random.choice(when) + ', ' + random.choice(what)+ ' that lived in ' + random.choice(residence)+ ', went to the ' + random.choice(went)+ ' and '+ random.choice(happened))
