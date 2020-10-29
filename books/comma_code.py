#
# Comma Code
from typing import List

def commaCode(lst: List[str]) -> str:
	if len(lst) == 1:
		return lst[0]
	newStr = '{}, and {}'.format(', '.join(lst[:-1]), lst[-1])
	return newStr

def test():
	assert commaCode(['apples', 'bananas', 'tofu', 'cats']) == 'apples, bananas, tofu, and cats' 
