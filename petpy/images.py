import petpy
import os
import pandas as pd
import urllib.request
import urllib.error
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

key = os.getenv('PETFINDER_KEY')
pf = petpy.Petfinder(key)

dog_breeds = pf.breed_list('dog', return_df=True)[' breeds'].tolist()

