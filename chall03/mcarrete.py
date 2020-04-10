#!/usr/bin/env python

import sys

def snailArray(argv):
	i = 0
	top_side = len(argv) - 1
	side = len(argv) - 1
	j = 1
	while i <= top_side and j <= side:
		for i in range(j - 1, side):
			print(argv[j][i] + ",", end = " ")
		i +=  1
		for k in range(i, top_side):
			print(argv[k + 1][side] + ",", end = " ")
		j -= 1
		if i <= top_side:
			for k in range(side, j):
				print(argv[top_side][k] + ",", end = " ")
		top_side -= 1
		if j <= side:
			for k in range(top_side, i - 1, -1):
				print(argv[k][j] + ",", end = " ")
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

