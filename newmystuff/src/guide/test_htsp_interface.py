'''
Created on 10 Jul 2014

@author: khurley
'''
import unittest

import htsp_interface
import mock

class TestConversionFromHTSP(unittest.TestCase):
    def test_create_a_programme(self):
        with mock.patch('guide_model.Programme') as mocked:
            mocked.side_effect = Exception("boom")
            event_msg={'title':'Title','description':'Details', 'start':100}
            prog=htsp_interface.HtspInterface.programme(event_msg)
            self.assertEqual(prog.start, 100)
            mocked.assert_called_once()
            
    def test_create_a_channel(self):
        event_msg={'channelName':'BBC One', "channelId":99, "channelNumber":1}
        chan=htsp_interface.HtspInterface.channel(event_msg)
        self.assertEqual(chan.name,"BBC One", "channel names dont match")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_create_a_programme']
    unittest.main()