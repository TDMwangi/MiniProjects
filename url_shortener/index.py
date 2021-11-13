import pyshorteners

url = input("Enter the URL: ")

short_url = pyshorteners.Shortener().tinyurl.short(url)

print("Short URL: ", short_url)
