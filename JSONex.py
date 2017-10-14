import urllib2	
import json



def printResults(data):
	theJSON = json.loads(data)

	if "title" in theJSON["metadata"]:
		print theJSON["metadata"]["title"]

	count = theJSON["metadata"]["count"];
	print str(count) + " events recorded"

	print "Events that were felt:"
	for i in theJSON["features"]:
		feltReports = i["properties"]["felt"]
		if (feltReports != None) & (feltReports > 0):
			if (feltReports >  1):
				print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported " + str(feltReports) + " times"
			else:
				print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported " + str(feltReports) + " time"			

def dumpResults(data):
	with open('data.txt', 'w') as outfile:
    		json.dump(data, outfile)		

def main():
	
	exit (1)
	urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
	webUrl = urllib2.urlopen(urlData)
	print webUrl.getcode()
	if (webUrl.getcode() == 200):
		http_message = webUrl.info()
		assert http_message.type == "application/json", "NOT json"
		full = http_message.type # 'text/plain'
		maintype = http_message.maintype # 'text'
		print full
		print maintype			
			
		data = webUrl.read()
		printResults(data)
		dumpResults(data)
	else:
		print "Received an error from server, cannot retrieve results " + str(webUrl.getcode)
		exit(-1)



if __name__== "__main__":
	main()



