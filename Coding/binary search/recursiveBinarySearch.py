__author__ = 'lindam'


def binarySearch(target,mylist):
    if len(mylist)==0:
        return False
    elif len(mylist)==1:
        if mylist[0] == target:
            return True
        else:
            return False
    #find midpoint
    midpoint=len(mylist)//2
    if mylist[midpoint]==target:
        return True
    elif target<mylist[midpoint]:
        return binarySearch(target,mylist[:midpoint])
    else:
        return binarySearch(target,mylist[midpoint:])

print (binarySearch(7,[-2,-1,0,1,2,3,4,5,6.5,7,8,9,10,11]))
