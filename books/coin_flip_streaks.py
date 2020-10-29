#
# Coin Flip Streaks
import random

numberOfStreaks = 0
side = ['H', 'T']
lst = []
for experimentNumber in range(10000):
	lst.append(random.choice(side))
	if lst.count('H') == 6 or lst.count('T') == 6:
		numberOfStreaks += 1

print(lst)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
