import unittest as test
import main


class TestMain(test.TestCase):
    def testReg(self):
        '''Test reg'''
        name = "Yasser"
        result = main.sayHello(name)
        self.assertEqual(result , "Yasser")
test.main()