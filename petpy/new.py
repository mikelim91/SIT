import petpy
import os
import pandas as pd
import urllib.request
import urllib.error
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

key = os.getenv('PETFINDER_KEY')
secret = os.getenv('PETFINDER_SECRET_KEY')

pf = petpy.Petfinder(key=key, secret=secret)

# animal_types = pf.animal_types()

# for animal in animal_types['types']:
#     print(animal['name'], '\n', animal['coats'])
    
# dogs = pf.animal_types('dog')
# print(dogs['type']['coats'])
# print(dogs['type']['colors'])


# dog_breeds = pf.breeds('dog', return_df=True)['dog breeds'].tolist()



# dog_breeds = pf.breeds('dog')


# pool = ThreadPool(processes=8)

# def get_dog_breeds(dog):
#     breeds = pf.pet_find('US', animal='dog', breed=dog, count=500, pages=3, return_df=True)
#     return(breeds)

# dogs = pool.map(get_dog_breeds, dog_breeds) 
# pool.close()
# pool.join()

# dogs = pd.concat(dogs)

# def get_dog_breeds(dog):
#     all_breeds = []
#     for page in range(1, 4):  # Looping through 3 pages as an example
#         try:
#             breeds_page = pf.animals(animal_type='dog', breed=dog, location='US', limit=100, page=page, return_df=True)
#             all_breeds.append(breeds_page)
#         except Exception as e:
#             print(f"Failed to retrieve breeds for {dog} on page {page} due to {e}")
#     return pd.concat(all_breeds, ignore_index=True) if all_breeds else pd.DataFrame()



import petpy
import os
import pandas as pd

# Initialize Petfinder with your API keys
key = os.getenv('PETFINDER_KEY')
secret = os.getenv('PETFINDER_SECRET_KEY')
pf = petpy.Petfinder(key=key, secret=secret)

# Fetch a list of dog breeds from the Petfinder API
dog_breeds = pf.breeds('dog')['breeds']  # Assuming 'breeds' is the correct key

# Function to fetch data for a given dog breed
def get_dog_breeds(dog):
    all_breeds = []
    for page in range(1, 4):  # Here we are paginating manually through 3 pages
        try:
            # Fetch a page of results for the given dog breed
            breeds_page = pf.animals(animal_type='dog', gender='female', status='adoptable', location='Seattle, WA', distance=10, results_per_page=50, pages=2, return_df=True)
            if breeds_page.empty:
                break  # If no results, exit the loop
            all_breeds.append(breeds_page)
        except Exception as e:
            print(f"Failed to retrieve breeds for {dog} on page {page} due to {e}")
            break  # If there's an error, exit the loop
    return pd.concat(all_breeds, ignore_index=True) if all_breeds else pd.DataFrame()

# Create a thread pool and map the function across all dog breeds
pool = ThreadPool(processes=8)
dogs = pool.map(get_dog_breeds, dog_breeds)
pool.close()
pool.join()

# Concatenate all the DataFrames into a single DataFrame
dogs_df = pd.concat(dogs, ignore_index=True)
print(pd.DataFrame(dogs_df.head()))
print(dogs_df.columns)






# import time

# def get_dog_breeds(dog):
#     all_breeds = []
#     for page in range(1, 4):  # Paginating manually through 3 pages
#         attempt = 0
#         while attempt < 3:  # Try to fetch each page up to 3 times
#             try:
#                 breeds_page = pf.animals(animal_type='dog', breed=dog, location='US', results_per_page=100, page=page, return_df=True)
#                 if breeds_page.empty:
#                     break  # If no results, exit the loop
#                 all_breeds.append(breeds_page)
#                 break  # Successful fetch, exit retry loop
#             except Exception as e:
#                 print(f"Attempt {attempt + 1}: Failed to retrieve breeds for {dog} on page {page} due to {e}")
#                 time.sleep(5)  # Wait 5 seconds before retrying
#                 attempt += 1
#     return pd.concat(all_breeds, ignore_index=True) if all_breeds else pd.DataFrame()



# # Fetch a list of dog breeds from the Petfinder API
# dog_breeds = pf.breeds('dog')['breeds']  # Assuming 'breeds' is the correct key


# # Create a thread pool and map the function across all dog breeds
# pool = ThreadPool(processes=8)
# dogs = pool.map(get_dog_breeds, dog_breeds)
# pool.close()
# pool.join()

# # Concatenate all the DataFrames into a single DataFrame
# dogs_df = pd.concat(dogs, ignore_index=True)
# # print(dogs_df.head())
