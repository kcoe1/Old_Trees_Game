#timeout test

import sys
import time
pygame_path = "C:\\users\\kcoe2\\appdata\\local\\programs\\python\\python39\\lib\\site-packages"
sys.path.append(pygame_path)


from inputimeout import inputimeout, TimeoutOccurred
try:
    something = inputimeout(prompt='>>', timeout=5)
except TimeoutOccurred:
    something = 'something'
print(something)
time.sleep(3)
