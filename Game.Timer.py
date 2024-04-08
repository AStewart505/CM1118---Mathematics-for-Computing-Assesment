import time
import sys

for remaining in range (60,0,-1):
    sys.stdout.write('\r')
    sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\r Time ran out            \n")
sys.stdout.write('\r Try Again?')