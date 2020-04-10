#!/usr/bin/env python

import sys

def snailArray(argv):
	i = 0
	top_side = len(argv) - 1
	side = len(argv) - 1
	j = 1
	while i <= top_side and j <= side:
		k = j - 1
		while k <= side - 1:
			print(argv[j][k] + ",", end = " ")
			k += 1
		i += 1
		k = i + 1
		while k <= top_side:
			print(argv[k][side - 1] + ",", end = " ")
			k += 1
		side -= 1
		if i <= top_side:
			k = side
			while k <= j:
				print(argv[top_side][k] + ",", end = " ")
				k += 1
		top_side -= 1
		if j <= side:
			k = top_side
			while k < top_side - 1:
				print(argv[k][j] + ",", end = " ")
				k += 1
		j += 1


def main(argv):
	i = 1
	error = "usage: ./mcarrete.py <1-9 squared_rows...>"
	if len(argv) < 2:
		print(error)
		return(error)
	while i < len(argv):
		if len(argv[i]) != (len(argv) - 1) or argv[i].isdigit() == False:
			print (error)
			return error
		i = i + 1
	snailArray(argv)

if __name__ == '__main__':
	main(sys.argv)

