# imports
import os
import pandas as pd

# function to acquire mushroom ds
def get_data_csv():
    '''
    Argument: No arguments required
    Actions: 
        1. Checks for the existence of the csv in the current directory
            a. if present:
                i. reads the csv from the current working directory
            b. if not present:
                i. reads csv from url
                ii. saves the csv to the current working directory
    Return: dataframe
    Modules: pandas, os
    '''
    # a variable to hold the xpected or future file name
    filename = 'mushroom.csv'
    
    # if the file is present in the directory 
    if os.path.isfile(filename):
      
        # read the csv and assign it to the variable df
        df = pd.read_csv(filename)
        
        # return the dataframe and exit the funtion
        return df
    
    # if the file is not in the current working directory,
    else:
        
        # use the env.py function to get the url needed from the db
        url = 'https://storage.googleapis.com/kagglesdsdata/datasets/2885163/4975377/mushroom.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230325%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230325T204548Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=169e617a4c63bb31f448d975a8385635ddf3eb7ab3a5392df629d75be1dd5a977235b12e7f6a2bebbe484c2acb2e1c7efe376d15090df33c7a1d308a8b76d293cc98a1b4bf500c769607330d1ee19fcbff7f291e7d7135d872ba15beb859533e19e6a1a5a0ade1b8be3f160cb0eccc110250a35faf436d647bb9c8bb2b781a0d93356cad7d00c7e1dc1e8a46b7d4ce9108909141fd51941b93755a1c7f31f927c6e48b1f2234f5551ad3563380b8b318a2e722c0da8c5ab99bc8a9790e3536692dce26e0cef0b4c34bf5c4a222fdf83f4be5908fc6ed4c2860636bf781f8afb4eae9b692b0121d71ec4f2567df137ae74fefdccbc1e00f779a506bae073b7169'
        
        # query sql using pandas function
        df = pd.read_csv(url)
        
        # save the dataframe as a csv to the current working directory
        df.to_csv(filename)
        
        # returns the dataframe
        return df
