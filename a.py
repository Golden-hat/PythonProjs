import numpy as np

SpawnDisty = [1, 2, 3, 4]
height = 4
def randy(type):
    if SpawnDisty[type]>= height:
        rval = np.random.randint(0, 11, 10)
    return rval
def val():
    rval = np.random.randint(0, 10, 10)
    return rval

print (randy(3))
print (randy(3))
print (randy(3))
print (randy(3))

print (val())
print (val())
print (val())
print (val())
print (val())
