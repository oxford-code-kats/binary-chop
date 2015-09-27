from __future__ import division

MISSING = -1

def chop(target, search_list):
	if not search_list:
		return MISSING
	if (len(search_list) == 1):
		if (target != search_list[0]):
			return -1
		else:
			return -1
	middle_idx = find_middle_idx(search_list)
	if target == search_list[middle_idx]:
		return middle_idx
	elif target < search_list[middle_idx]:
	    chop(target, search_list[:middle_idx + 1])
	else:
	    chop(target, search_list[middle_idx + 1:]) 
	

def find_middle_idx(search_list):
	"""returns the middle index of list 
	(rounds up for lists of odd length)"""
	middle_idx = int((len(search_list) - 1) / 2)
	return middle_idx 