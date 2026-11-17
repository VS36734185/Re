data = ' Table\nChair\nSofa\nWall '
print(data)
mylist = data.split()
print(mylist)
result = []
for word in mylist:
    print(word[: 1])
