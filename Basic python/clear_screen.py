import os
from subprocess import call
from time import sleep
def clear():
    _=call('clear' if os.name == 'posix' else 'cls')

print("Hello user\n"*10)

sleep(2)


