## While
connected = False

i = 0
while not connected:
    i += 1
    print('Not Connected')
    if i >= 5:
        connected = True

else:
    print('Connected')



connected = False
tries = 0

while tries < 9:
    tries += 1
    print('Not Connected')
    if connected:
        break

else:
    print('Connection Failed')

## Function (def)
def f(x):  # Bazgashti --> Return
    return x + 1

def addition(x, y):
    return x + y

def connect():  # Bazgashti Nist
    print('Connected To Server. . .')


addition(5, 4)
