
import re
import collections
texts = ['John likes to watch movies. Mary likes too.',
   'John also likes to watch football games.',
   'Nepal country of Asia lying along the southern slopes of the Himalayan mountain ranges.', 
   'It is a landlocked country located between India to the east south and west and the Tibet Autonomous Region of China to the north.',
   'Its territory extends roughly 500 miles (800 kilometres) from east to west and 90 to 150 miles from north to south.',
   'The capital is Kathmandu.']								 	#Give your desired text of many lines...

bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
            for txt in texts]

print(bagsofwords[0]) 										#checking here
print(bagsofwords[1])
sumbags = sum(bagsofwords, collections.Counter())

print (sumbags) 										#check here with different text inputs
