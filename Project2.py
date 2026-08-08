# random password generator

import random, string

pswd_len=12
charValue=string.ascii_letters + string.digits +string.punctuation

#list comprehension [func for i in range(n)]

a="".join([random.choice(charValue) for i in range(pswd_len)])

# pswd=""
# for i in range(pswd_len):
#     pswd+=random.choice(charValue)

#print(f"your random password is: '{pswd}'")
print(f"your random password is: '{a}'")