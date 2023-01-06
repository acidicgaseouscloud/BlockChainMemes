# converting list to file
def WriteListTxt(list, name):
    text = '\n'.join(list)
    f = open(name, 'x') 
    f.write(text)
    f.close()
    
# This is the column with the link for 
# the media of the post not the post itself

ImageURLS = Mdf["image_file"].tolist() 

WriteListTxt(ImageURLS, "CryptoMemes.txt")

# Getting the memes via terminal
## navigate to where you want to store 
## the images and run:
### wget -i CryptoMemes.txt
## Make sure the file containing the urls
## is also in the same folder

# Checking which files were downloaded
## images will be saved by their name as 
## mentioned in their url (eg - .../imagename.png)

filepaths = []

for filepath in glob('FolderWhereImagesAreStored/*'): 
    filepaths.append(splitext(basename(filepath))[0])

FoundOrNot = [] # storing download check results

counter = -1 # count starts from 0

for url in ImageURLS:
    counter+=1
    for filepath in filepaths:
        if filepath in url:  
            FoundOrNot.append(counter)
            
# adding to dataframe
## 

numOfItems = # number would be excel index number for the last item - 2
            
count = [i for i in range(numOfItems)]

Downloaded = []

for number in count: 
    if number in FoundOrNot:
        Downloaded.append('yes')
    else:
        Downloaded.append('no')
        
Mdf['Downloaded'] = Downloaded      

Mdf.to_csv("Downloaded.csv")
