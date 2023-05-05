import random

elements = "+-/*!&$#?=@<>"
password = ""
pass_length = int(input("Şifre uzunluğunuzu girin: "))

for i in range(pass_length):
    password += random.choice(elements)

print(password)
