from bs4 import BeautifulSoup
import pprint as pp #prints complex data structures with nice indentations
import urllib.request


page = 'path/to/source.html'
soup = BeautifulSoup(open(page), "lxml") #lxml is a third party parser used to make sense of HTML Tags in python. Its advantage is speed.

#in every headword we need to extract the content 
headings = soup.find_all('div', class_='headword') #find every such divs and return a list of markups for all the head word classes
#Generally: headings = soup.find_all('div', {'class', 'headword'} )

#All info
all_info = []

for head in headings:
	word = head.find('a').text.strip() #we need to extract the word which is in the anchor tag of the div
	pronunciation = head.find_next_sibling('div', class_='pron').text.strip() #the next is pron which is the next div.It will return its markup 
	audio_url = head.find('source',{'type':'audio/mpeg'}).get('src') #we take advantage of beautiful soup and get the src directly
	
	mp3file = urllib.request.urlopen(audio_url)
	local_url = 'path/to/store/audio/{}.mp3'.format(word) 
	print ("Fetching {} ... ".format(audio_url))

	with open(local_url,'w+') as aout:
		while True:
			data = mp3file.read(4096) #4 kilo btyes
			if data:
				aout.write('data')
			else:
				break

	all_info.append( (str(word), str(pronunciation), audio_url, local_url) )

pp.pprint(all_info, indent=4)

#print [w for w,p,a,l in all_info]
