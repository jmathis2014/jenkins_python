#!/usr/bin/python -B -W all

#-----------------------------------------------------------------------------#
# U N I T T E S T  I N F O R M A T I O N #
#-----------------------------------------------------------------------------#
#
# NAME:  
# DATE: 8
# CREATOR: 
#
# DESCRIPTION:
#
# VERSION: 
#
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
# M O D U L E S #
#-----------------------------------------------------------------------------#
import unittest


#-----------------------------------------------------------------------------#
# C U S T O M  M O D U L E S #
#-----------------------------------------------------------------------------#
from mymath import mymath

#-----------------------------------------------------------------------------#
# C O N S T A N T  V A R I A B L E S #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
# C L A S S E S #
#-----------------------------------------------------------------------------#

class testMyMath(unittest.TestCase):

    def test_add(self):
        my_math = mymath.mymath()
        self.assertEqual(my_math.add(1, 1), 2)
        self.assertEqual(my_math.add(1, 3), 4)

    def test_subtract(self):
        my_math = mymath.mymath()
        self.assertEqual(my_math.subtract(2, 2), 0)

if __name__ == '__main__':
    os.chdir("../")
    unittest.main()

