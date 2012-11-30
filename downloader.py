########################################################
#
#	hacked by: Virendra Rajput
#	Twitter: @bkvirendra
#	Blog: http://virendra.me
#
########################################################

import urllib2, sys, os
from bs4 import BeautifulSoup
from urlparse import urlparse

def downloader(urls, grab_url, foldername):
	if not os.path.exists(foldername):
		print "\""+ foldername + "\" does not exist!"
		os.makedirs(foldername)
		print "Creating \"" + foldername + "\"..." 
	for cover in urls:
		try:
			print "Downloading item " + cover + "..."
			print grab_url + cover
			img = urllib2.urlopen(grab_url + cover)
			output = open(foldername + "/" + cover,'wb')
			output.write(img.read())
			output.close()
			print cover + "... downloaded!!"
		except Exception, e:
			pass
	return

def main(url):
	urls = []
	print "Fetching the page..."
	page = urllib2.urlopen(url).read()
	print "Fetching completed!"
	soup = BeautifulSoup(page)
	print "Grabbing the objects of the page..."
	lis = soup.find_all("li")
	for item in lis:
		urls.append(item.a['href'])
	domain = urlparse(url)
	downloader(urls, url, domain.netloc)
	print "All files have been successfully downloaded!"
	print "\tHack by Virendra Rajput, \n\tFollow me on Twitter @bkvirendra\n\tI Blog at http://virendra.me/"
	return

if __name__ == '__main__':
	main(sys.argv[1])