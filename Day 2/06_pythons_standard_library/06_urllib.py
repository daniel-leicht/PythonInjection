import urllib

# Retrieve content from a URL:

http_response = urllib.request.urlopen("https://www.bankhapoalim.co.il/")
html = http_response.read()

print(str(html[:500], "utf-8"))