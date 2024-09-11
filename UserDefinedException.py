class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def print(self):
        print("Exception occured with value:" + self.value)

try:
    raise(MyException("Raising new Exception"))

except MyException as e:
    e.print()