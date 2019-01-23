import os
from subprocess import Popen

p=os.popen('cmd')
print (p.read())