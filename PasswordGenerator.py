import random

upper_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letter=upper_letter.lower()
digits="0123456789"

upper,lower,nums=True,True,True

all=""
if upper:
    all +=upper_letter
if lower:
    all +=lower_letter
if nums:
    all +=digits

length=15

password="".join(random.sample(all,length))
print(password)