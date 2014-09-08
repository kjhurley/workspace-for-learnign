'''
Created on 18 Aug 2014

@author: khurley
'''
import unittest
import mock
import librarian
import library_record
import iplayer_monitor

class Test(unittest.TestCase):


    def setUp(self):
        self.librarian = librarian.Librarian()


    def tearDown(self):
        pass


    def est_look_for_new_files(self):
        info_stream="""blah blah blah"""
        with mock.patch("iplayer_monitor.IPlayerMonitor.read_log") as read_log:
            read_log.return_value=[{'original':'first_file.flv'}]
            with mock.patch("iplayer_monitor.episode_factory") as factory, mock.patch('iplayer_monitor.HorizonEpisode') as horizon_episode:
                self.librarian.look_for_new_files(info_stream)
                self.assertEqual(1,read_log.call_count)
                horizon_episode.title="bananna"
                horizon_episode.tvdb_ok=True
                factory.return_value=horizon_episode
                self.assertEqual(1,factory.call_count)
                self.assertEqual(len(self.librarian.records),1)
                self.assertEqual(self.librarian.records[0].original_file_name,"first_file.flv")
    
    def test_look_for_new_files_duplicates(self):
        info_stream="""blah blah blah"""
        with mock.patch("iplayer_monitor.IPlayerInfoParser.read_log") as read_log:
            read_log.return_value=[{'original':'first_file.flv'},{'original':'first_file.flv'}]
            with mock.patch("iplayer_monitor.episode_factory") as factory, mock.patch('iplayer_monitor.HorizonEpisode') as horizon_episode:
                self.librarian.look_for_new_files(info_stream)
                self.assertEqual(1,read_log.call_count)
                factory.return_value=horizon_episode
                self.assertEqual(1,factory.call_count)
                self.assertEqual(len(self.librarian.records),1)
                self.assertEqual(self.librarian.records[0].original_file_name,"first_file.flv")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_look_for_new_files']
    unittest.main()
