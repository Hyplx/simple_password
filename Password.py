import time

username = input("User: ")
password = input("Pass: ")

time.sleep(.25)


if username == 'Name' and password == 'Pass':
    print('Welcome' ,username)
    

else:
    print('Login failed')
