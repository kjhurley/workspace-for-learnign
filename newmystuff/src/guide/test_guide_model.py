import guide_model
import unittest

class TestCase(unittest.TestCase):
    def test_add_a_channel(self):
        input_1_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_1_from_htsp)
        self.assertEqual(g.channelName(7), "4Music")
        input_2_from_htsp={'eventId': 116108, 'tags': [1, 2, 3], 'nextEventId': 116110, 'channelId': 8, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': 'More4', 'method': 'channelAdd'}
        g.add_a_channel(input_2_from_htsp)
        self.assertEqual(g.channelName(8), "More4")

    def test_add_a_programme(self):
        input_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_from_htsp)
        more_input_from_htsp={'eventId': 116107, 'serieslinkId': 76020, 'contentType': 96, 'description': "It's the pop world cup and today's match is the quarter final between Rihanna and Lady Gaga. This could go either way. It's time to decide which stand you'll be seated in!", 'title': 'Pop World Cup: Rihanna v Lady Gaga', 'nextEventId': 116109, 'channelId': 7, 'stop': 1404492000, 'episodeId': 116108, 'start': 1404489600, 'method': 'eventAdd'}
        g.add_a_programme(more_input_from_htsp)
        self.assertEqual(g.listing(8)[0]['title'],'Pop World Cup: Rihanna v Lady Gaga')
        
