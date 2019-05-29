import random
from BaseAI_3 import BaseAI
import time
from Grid_3 import *
import math

inf = float('inf')
max_depth = 100
empty_w, mono_w, smooth_w, max_w, corner_w = 0.4, 0.35, 0.35, 0.05, 0.05

class PlayerAI(BaseAI):
	def __init__(self):
		self.start = 0.0
		self.time_out = False
	
	def maximize(self, grid, alpha, beta, depth, max_depth):
		# Base case for time out
		if self.timeout():
			return None, -inf
		# Base case for IDS depth limit
		if depth > max_depth:
			return None, self.heuristic(grid)
		
		maxChild, maxUtility = None, -inf
		availableMoves = grid.getAvailableMoves()

		for child, child_grid in availableMoves:
			utility = self.chance(child_grid, alpha, beta, depth, max_depth)

			if utility > maxUtility:
				maxChild, maxUtility = child, utility
			
			if maxUtility >= beta:
				break
			
			if maxUtility > alpha:
				alpha = maxUtility
		
		return maxChild, maxUtility
	

	def chance(self, grid, alpha, beta, depth, max_depth):
		return 0.9 * self.minimize(grid, alpha, beta, depth+1, max_depth, 2) + \
			   0.1 * self.minimize(grid, alpha, beta, depth+1, max_depth, 4)
	
	def minimize(self, grid, alpha, beta, depth, max_depth, tile):
		# Base case for time out
		if self.timeout():
			return inf
		# Base case for IDS depth limit
		if depth > max_depth:
			return self.heuristic(grid)

		minUtility = inf
		empty_cells = grid.getAvailableCells()

		for cell in empty_cells:
			child_grid = grid.clone()
			child_grid.setCellValue(cell, tile)

			_ , utility = self.maximize(child_grid, alpha, beta, depth+1, max_depth)

			if utility < minUtility:
				minUtility = utility
			
			if minUtility <= alpha:
				break
			
			if minUtility < beta:
				beta = minUtility
		
		return minUtility

	
	def getMove(self, grid):
		self.start = time.clock()
		self.time_out = False
		result = None
		# IDS
		for max_d in range(max_depth):
			maxChild, _ = self.maximize(grid, -inf, inf, 0, max_d)
			if self.time_out:
				break
			elif maxChild != None:
				result = maxChild
		
		return result


	def timeout(self):
		if self.time_out:
			return True
		elif time.clock() - self.start >= 0.2:
			self.time_out = True
			return True
		else:
			return False
	

	'''
	I use 5 heuristics: number of empty cells, monotonicity, smoothness, 
	whether maxTile is on the corner or not, and maxTile value. I will derive the 
	5 heuristics in one function(a single while loop) to save calculation time compared to 
	derive the heuristics separately
	'''
	def mono(self, i, row, incre, grid):
		if row and incre:
			return grid.getCellValue((i,0)) <= grid.getCellValue((i,1)) and grid.getCellValue((i,1)) <= grid.getCellValue((i,2))\
				and grid.getCellValue((i,2)) <= grid.getCellValue((i,3))
		elif row and not incre:
			return grid.getCellValue((i,0)) >= grid.getCellValue((i,1)) and grid.getCellValue((i,1)) >= grid.getCellValue((i,2))\
				and grid.getCellValue((i,2)) >= grid.getCellValue((i,3))
		elif not row and incre:
			return grid.getCellValue((0,i)) <= grid.getCellValue((1,i)) and grid.getCellValue((1,i)) <= grid.getCellValue((2,i))\
				and grid.getCellValue((2,i)) <= grid.getCellValue((3,i))
		else:
			return grid.getCellValue((0,i)) >= grid.getCellValue((1,i)) and grid.getCellValue((1,i)) >= grid.getCellValue((2,i))\
				and grid.getCellValue((2,i)) >= grid.getCellValue((3,i))

	def heuristic(self, grid):
		empty_cells = 0 # try to maximize
		lrinc, lrdec, udinc, uddec = 0, 0, 0, 0 # try to maximize
		smooth = 0 # try to maximize
		smooth_total = 0
		max_tile = 0 # try to maximize
		max_corner = 0 # try to maximize

		for i in range(grid.size):
			if self.mono(i, True, True, grid):
				lrinc += 1
			if self.mono(i, True, False, grid):
				lrdec += 1
			if self.mono(i, False, True, grid):
				udinc += 1
			if self.mono(i, False, False, grid):
				uddec += 1

			for j in range(grid.size):
				if j < grid.size-1 and grid.getCellValue((i,j)) != 0:
					smooth_total += 1
					if grid.getCellValue((i, j+1)) - grid.getCellValue((i, j)) == 0:
						smooth += 1

				if i < grid.size-1 and grid.getCellValue((i,j)) != 0:
					smooth_total += 1
					if grid.getCellValue((i+1, j)) - grid.getCellValue((i, j)) == 0:
						smooth += 1
					
				if grid.getCellValue((i, j)) > max_tile:
					max_tile = grid.getCellValue((i, j))
				if grid.getCellValue((i,j)) == 0:
					empty_cells += 1

		empty_cells = float(empty_cells) / 15
		mono = float(max(lrinc, lrdec) + max(udinc, uddec)) / 8
		smooth = float(smooth) / smooth_total if smooth_total != 0 else 0
		corners = [(0,0), (0,3), (3,0), (3,3)]
		for corner in corners:
			if grid.getCellValue(corner) == max_tile:
				max_corner = 1
		max_tile = math.log2(max_tile)/math.log2(4096)
		return empty_w * empty_cells + mono_w * mono + \
			smooth_w * smooth + max_w * max_tile + corner_w * max_corner


	
