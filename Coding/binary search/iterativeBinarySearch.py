__author__ = 'lindam'

mylist = [2,3,5,6,7,8,10,12,15] #list must be sorted
target = 8


searchlist = mylist
found = False
tooshort = False

while not found and not tooshort:
    mid = len(searchlist)//2 # double slash gives an integer divide
    if  target == searchlist[mid]:
        found = True
    elif target<searchlist[mid]:
        searchlist = searchlist[:mid]
    elif target>searchlist[mid]:
        searchlist = searchlist[mid:]
    if len(searchlist)==1:
        tooshort = True


print(found)


