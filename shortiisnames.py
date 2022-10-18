import requests
import string
import copy
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="url to test (example: https://www.domain.com/folder/)", required=True)

args=parser.parse_args()

urlPrefix = args.url
urlSufix = "*~1.*/.aspx"
myArray=[]
tmpArray=[]

def TestURL(urlToTest):
	try:
		req = requests.get(urlToTest)
		if req.status_code == 200:
			#print("- " + urlToTest)
			return True
	except:
		print("(err) " + urlToTest)


for i in range(6):
	tmpArray = copy.copy(myArray)
	myArray = []
	for charToTest in string.ascii_lowercase+string.digits:
		if i == 0:
			urlToTest = urlPrefix + charToTest + urlSufix
			if TestURL(urlToTest)==True:
				myArray.append(charToTest)
		else:
			for charArreglo in tmpArray:
				urlToTest = urlPrefix + charArreglo + charToTest + urlSufix
				if TestURL(urlToTest)==True:
					myArray.append(charArreglo + charToTest)
					if i == 5:
						print(urlToTest)

print("Done!")

