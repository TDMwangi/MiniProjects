from googlesearch import search

query = input("What do you want to search for on google? : ")

for i in search(query, start=0, stop=10):
    print(i)
