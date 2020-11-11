import pyshorteners
#website=input("Enter the website name")
url = input("Enter your url")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your shorted is -->", s)