

def insertion_sort(tlist):
    for index in range(1, len(tlist)):
		currentValue = tlist[index]
		position = index       
		while position > 0 and tlist[position-1] > currentValue:	  
		    tlist[position] = tlist[position-1]		   
		    position = position-1
		    tlist[position] = currentValue
tlist = [54,26,92,12,4,76,34,20]
insertion_sort(tlist)
print(tlist)

