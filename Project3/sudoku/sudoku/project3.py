import os
import sys
from itertools import zip_longest, chain


class Sudoku:
	"""
		Sudoku class, which models a Sudoku game.

		Based on Peter Norvig's Suggested Sudoku setup
	"""

	def __init__(self):
		"""
			Initialize digits, rows, columns, the grid, squares, units, peers, and values.
		"""
		self.digits = '123456789'
		self.rows = 'ABCDEFGHI'
		self.cols = self.digits
		self.grid = dict()
		self.squares = self.cross_product(self.rows, self.cols)
		unitlist = ([self.cross_product(self.rows, c) for c in self.cols] + \
		            [self.cross_product(r, self.cols) for r in self.rows] + \
		            [self.cross_product(rs, cs) for rs in self.chunk(self.rows, 3) for cs in self.chunk(self.cols, 3)])

		# [self.cross_product(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

		# Every square has exactly 3 units - col, row, grid

		self.units = dict((s, [u for u in unitlist if s in u]) for s in self.squares)
		self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)
		self.values = dict((s, self.digits) for s in self.squares)

	@staticmethod
	def cross_product(A, B):
		"""
			Return the cross product of A and B
		"""
		return [a + b for a in A for b in B]

	def chunk(self, iterable, n, fillvalue=None):
		"""
		:param iterable:
		:param n:
		:param fillvalue:
		:return:
		"""
		args = [iter(iterable)] * n
		return zip_longest(*args, fillvalue=fillvalue)

	def __str__(self):
		"""
			Convert the grid into a human-readable string
		"""
		output = ''
		width = 2 + max(len(self.grid[s]) for s in self.squares)
		line = '+'.join(['-' * (width * 3)] * 3)
		for r in self.rows:
			output += (''.join(
				(self.grid[r + c] if self.grid[r + c] not in '0.' else '').center(width) + ('|' if c in '36' else '')
				for c in self.digits)) + "\n"
			if r in 'CF': output += line + "\n"
		return output

	def load_file(self, filename):
		"""
			Load the file into the grid dictionary. Note that keys
			are in the form '[A-I][1-9]' (e.g., 'E5').
		"""
		grid = ''
		with open(filename) as f:
			grid = ''.join(f.readlines())
		grid_values = self.grid_values(grid)
		self.grid = grid_values

	def grid_values(self, grid):
		"""
			Convert grid into a dict of {square: char} with '0' or '.' for empties.
		"""
		chars = [c for c in grid if c in self.digits or c in '0.']
		assert len(chars) == 81
		return dict(zip(self.squares, chars))


	def solve(self):
		"""
			Solve the problem by propagation and backtracking.
		"""
		self.initialize_state()
		return self.search(self.propagate())

	def initialize_state(self):
		"""
		:return: remaining values for each square
		"""
		# Change the domain of the grid if the gird already has a value.
		# This process will enable starting with sqaures that are only empty

		for key, value in self.grid.items():
			if self.grid[key] != '0':
				self.values[key] = self.grid[key]


	def add_constraints(self, key):
		"""
		:param key:
		:return:
		"""

		for peer in self.peers[key]:
			if self.values[key] in self.values[peer]:
				self.values[peer] = self.values[peer].replace(self.values[key], '')


	def is_solved(self):
		"""
		:return: true if values in the domain are all one item
		"""
		return all([len(value) == 1 for key, value in self.values.items()])

	def propagate(self):
		"""
			TODO: Code the Constraint Propagation Technique Here
		"""

		while not self.is_solved():

			for key, value in self.values.items():

				if len(value) == 1:
					self.add_constraints(key)


		return self.values

	def search(self, values):
		"""
			TODO: Code the Backtracking Search Technique Here
		"""

		# Copy the items back to the grid before the grid is printed

		for k, v in self.values.items():
			self.grid[k] = v

		return values


def main():
	s = Sudoku()
	'''
		The loop reads in as many files as you've passed on the command line.
		Example to read two easy files from the command line:
			python project3.py sudoku_easy1.txt sudoku_easy2.txt
	'''
	for x in range(1, len(sys.argv)):
		s.load_file(sys.argv[x])
		print("\n==============================================")
		print(sys.argv[x].center(46))
		print("==============================================\n")
		print(s)
		print("\n----------------------------------------------\n")
		s.solve()
		print(s)


main()
