#We could use this to make sure that the docker file not only installed all the dependencies, but also that everything work
#Only thought to include this because even though I have spades properly installed the spades.py --test fails.

import os

os.system("spades.py --test")

#etc etc
