import os, sys 

from enrich.customers import get_usecases_in_dir

def get_usecases(): 
    
    thisdir = os.path.abspath(os.path.dirname(__file__))
    return get_usecases_in_dir(thisdir) 
