filename='sample.txt'
with open(filename,'r') as f:
    content=f.read()
    words=content.split()
print(len(words))
