# given an 64bit number N and position p which will be from [0-63]
# write a function that given N and p
# returns N with the pth bit toggled

def toggleBit(N, p):
	return 0


class ToggleBitTest(unittest.TestCase):

  def test_one_step(self):
  	# N = 1 = 00001
  	# p = 0
  	self.assertEqual(toggleBit(1,0), 0)

  def test_two_step(self):
  	# N = 1 = 00001
  	# p = 1
  	self.assertEqual(toggleBit(1,1), 3)


if __name__ == '__main__':
    unittest.main()


