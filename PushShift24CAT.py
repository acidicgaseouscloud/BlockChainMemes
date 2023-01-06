# intitialise number of items

numOfItems = # number would be excel index number for the last item - 2

# Creating columns

ThreadID = [i for i in range(numOfItems)]
Mdf["id"] = ThreadID
Mdf["thread_id"] = ThreadID
Mdf["author"] = ["anon"]*numOfItems
Mdf["body"] = ["na"]*numOfItems

# Rename columns 

Mdf.rename(columns = {'created_utc':'timestamp', 'title':'subject', 'url':'image_file'}, inplace = True)

Mdf = Mdf.drop(Mdf.columns[0], axis=1)

# convert to csv

Mdf.to_csv("4CATCompatible.csv")
