# BlockChain Memes
Project with [Inte Gloerich](https://integloerich.nl/) on Block Chain memetic imaginaries as referenced in the chapter "Speculate — or Else! Blockchain Memes on Survival in Radical Uncertainty" of the [Critical Meme Reader II: Tacticality](https://networkcultures.org/blog/publication/critical-meme-reader-ii-memetic-tacticality/) by the [Institute of Network Cultures](https://networkcultures.org/). 


# Steps

1. Scrape Reddit via [PushShift](https://github.com/pushshift/api) 
2. Make [4CAT](https://4cat.oilab.nl) compatible:
- Make columns it expects
- rename column names to the name it expects that data to be under
4. Get memes from links
5. Use [Google Cloud Vision](https://cloud.google.com/vision/) for captions
- Requires existing set up of Google Cloud Vision
