import bs4
from bs4 import BeautifulSoup
import os
import glob


files=glob.glob('data/'+'*.txt')
for file in files:
	with open(file,'rb') as fp:
		soup = BeautifulSoup(fp,"lxml")

	factu=soup.factuality['type']
	#pub=soup.find_all('pubPlace')
	f=open('Result/tag_info/'+os.path.basename(file),"w")

	f.write(os.path.basename(file))
	f.write('\t')    
	f.write(str(factu))
	f.write('\t')
	f.write(str(soup.find('h.author').text))
	f.write('\t')
	f.write(str(soup.find('h.title').text))
	f.write('\t')
	f.write(str(soup.find('date').text))


    
    
    
