'''
Take password fron user
using lens statement
state the varible used to enter password 
analyze the lenght 
analyze the categories (strenght) when password is greater than 10
when password is greater than 8 print(very weak)
when password is  equal to 8 print(weak) 
when password is equal to 8 & 16 print(strong)
whwn password is less than or equal to 16 print(very strong) 
'''


password =int(input("lenght of password"))
password_lenght = len(password)


if (password_lenght < 8):
    print ('very weak')
  
if (password_length == 8):
    print('weak')

if (password_lenght > 8 and password > 16):
    print ('strong')

if (password_lenght > 16):
    print ('very strong')

