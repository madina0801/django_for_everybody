import urllib.request

fhand = urllib.request.urlopen('http://127.0.0.1/romeo.text')
for line in fhand:
	print(line.decode().strip())