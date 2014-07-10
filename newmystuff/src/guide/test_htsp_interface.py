'''
Created on 10 Jul 2014

@author: khurley
'''
import unittest

import htsp_interface
import mock

class Test(unittest.TestCase):


    def test_create_a_programme(self):
        event_msg={'title':'Title','description':'Details', 'start':100}
        prog=htsp_interface.HtspInterface.programe(event_msg)
        self.assertEqual(prog.start, 101)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_create_a_programme']
    unittest.main()