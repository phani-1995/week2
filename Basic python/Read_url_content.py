import urllib.request
#Get the connection to the url using urllib
weburl=urllib.request.urlopen("https://www.nasa.gov/news/releases/latest/index.html")

#Get the result code and print it
print("The result code is: " + str(weburl.getcode()))

#Read the data from the url and print it
data=weburl.read()
print(data)