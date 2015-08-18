
class UserIsADoofusException(Exception):
    def __init__(self, type_of_doofus):
        self.type_of_doofus = type_of_doofus

    def __str__(self):
        return "User is a Doofus of type: {}".format(self.type_of_doofus)


def foo():
    x = 34+4
    raise UserIsADoofusException("can't spell")


try:
    foo()
    i = int(input("first number"))
    j = int(input("second number"))
except Exception as e:  #DON'T DO THIS!!!!
    print("error is '", e, "'")



# try:
#     z = i/j
#     print(z)
# except ZeroDivisionError as e:
#     print(e)