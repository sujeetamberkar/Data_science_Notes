import os, sys
from os.path import dirname, join, abspath

# Adding the parent directory to sys.path
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from payment import payment_details

def course():
    print("This is my course details")

payment_details.payment()
