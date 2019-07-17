import bs4
from bs4 import BeautifulSoup
#import pandas as pd
import os
import glob



#path='/home/james/Desktop/Project/testing/Software/';
#path_out='/home/james/Desktop/Project/testing/Software/tmp/'

files=glob.glob('data/*.txt')

for file in files:
    with open(file,'rb') as fp:
        soup = BeautifulSoup(fp,"lxml")

    p=soup.find_all('p')

    #soup.factuality['type']

    f=open('tmp/'+os.path.basename(file),"w")
    
    for a in p:
        f.write(str(a))


