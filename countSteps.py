# 9.1
# count the number of steps it takes to climb
# up n stairs where steps can be taken 
# 1,2,3 steps at a time

import unittest

def count_steps(n):
	if n==0:
		return 1
	elif n < 0:
		return 0
	else:
		return count_steps(n-1) + count_steps(n-2) + count_steps(n-3)

def count_steps_dynamic(n):

	def cs_helper(n, seen):
		if n==0:
			return 1
		elif n < 0:
			return 0
		elif n in seen:
			return seen[n]
		else:
			seen[n] = cs_helper(n-1, seen) + cs_helper(n-2, seen) + cs_helper(n-3, seen)
			return seen[n]

	seen = {0:1}
	return cs_helper(n, seen)


class TestCountSteps(unittest.TestCase):

  def test_one_step(self):
  	self.assertEqual(count_steps_dynamic(1), 1)

  def test_two_step(self):
  	# steps = 2 => (1,1) (2)
  	self.assertEqual(count_steps_dynamic(2), 2)

  def test_three_step(self):
  	# steps = 3 => (1,1,1), (1,2), (2,1), (3)
  	self.assertEqual(count_steps_dynamic(3), 4)


  def test_four_step(self):
  	# steps = 3 => 
  	# (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2), (3,1), (1,3)
  	self.assertEqual(count_steps(4), 7)

if __name__ == '__main__':
    unittest.main()


