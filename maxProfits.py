import scipy
import numpy as np
from scipy.optimize import linprog
import unittest

def maxProfits(total_acreage, available_labor_hours, corn_price, oats_price, corn_time, oats_time):
  profit_constraints = [-1*corn_price, -1*oats_price]
  constraint_arrays = [[1, 1], [corn_time, oats_time]]
  inequality_limits = [total_acreage, available_labor_hours]

  x0_bounds = (0, None)
  x1_bounds = (0, None)

  optimized_result = linprog(profit_constraints, A_ub=constraint_arrays, b_ub=inequality_limits, bounds=[x0_bounds, x1_bounds], method='revised simplex')

  return optimized_result.x

maxProfits(240, 320, 40, 30, 2, 1)
maxProfits(300, 380, 70, 45, 3, 1)
maxProfits(180, 420, 65, 55, 3, 2)

#class TestProgram(unittest.TestCase):
  #def test_case_1(self):
    #self.assertEqual(maxProfits(240, 320, 40, 30, 2, 1))
  
  #def test_case_2(self):
    #self.assertEqual(maxProfits(300, 380, 70, 45, 3, 1))

  #def test_case_3(self):
    #self.assertEqual(maxProfits(180, 420, 65, 55, 3, 2))
