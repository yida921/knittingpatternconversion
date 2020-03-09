import unittest
import conversions as conv

"""
closechecks from knitting on the net
// in the round
Rows 1-4: *p3, k3; rep from *
Rows 5-8: *k3, p3; rep from *
"""

closechecksitrstart = "r1-4: *p3, k3*\nr5-8: *k3, p3*"
closechecksflat = 'r1: *p3, k3*\nr2: *k3, p3*\nr3: *p3, k3*\nr4: *k3, p3*\nr5: *k3, p3*\nr6: *p3, k3*\nr7: *k3, p3*\nr8: *p3, k3*'

closechecksitr = "r1: *p3, k3*\nr2: *p3, k3*\nr3: *p3, k3*\nr4: *p3, k3*\nr5: *k3, p3*\nr6: *k3, p3*\nr7: *k3, p3*\nr8: *k3, p3*"

prefix = 'testpatterns/'

def readfile(filename):
    with open(filename) as f:
        data='\n'.join(line.rstrip() for line in f)
    return data

oldshalevariationflat = readfile(prefix+'oldshalevariationflat.txt')
oldshalevariationitr = readfile(prefix+'oldshalevariationitr.txt')
#estonianleafitr = readfile(prefix+'estonianleafitr.txt')
#estonianleafflat = readfile(prefix+'estonianleafflat.txt')
sailingflat = readfile(prefix+'sailingflat.txt')
sailingitr = readfile(prefix+'sailingitr.txt')

oldshaleitr = 'r1: k1\nr2: k1\nr3: *p2tog3, yo, k16, p2tog3*\nr4: k1'
oldshaleflat = 'r1: k1\nr2: p1\nr3: *p2tog3, yo, k16, p2tog3*\nr4: p1'


class TestConversions(unittest.TestCase):

    def test_closechecksintheroundtoflat(self):
        self.assertEqual(closechecksflat, conv.itrtoflat(closechecksitrstart))
        self.assertEqual(closechecksitr, conv.flattoitr(closechecksflat))

    def test_oldshalevariation(self):
        self.assertEqual(oldshaleitr, conv.flattoitr(oldshalevariationflat))
        self.assertEqual(oldshaleflat, conv.itrtoflat(oldshalevariationitr))

    def test_sailing(self):
        self.assertEqual(sailingitr, conv.flattoitr(sailingflat))
        self.assertEqual(sailingflat, conv.itrtoflat(sailingitr))

if __name__ == '__main__':
    unittest.main()
