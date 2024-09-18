#!/usr/bin/env python3
import random
variable = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
variablen = "0123456789"
longitud = int(input("ingrese la longitud de la contraseña: "))
contraseña = ""
for i in range(longitud):
	contraseña = contraseña + random.choice(variable)

print(contraseña)
