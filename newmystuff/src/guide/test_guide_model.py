import guide_model
import unittest

class GuideTests(unittest.TestCase):
    def test_add_a_channel(self):
        input_1_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_1_from_htsp)
        self.assertEqual(g.channel(7).name, "4Music")
        
    def test_two_channels(self):
        input_1_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_1_from_htsp)
        self.assertEqual(g.channel(7).name, "4Music")
        input_2_from_htsp={'eventId': 116108, 'tags': [1, 2, 3], 'nextEventId': 116110, 'channelId': 8, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': 'More4', 'method': 'channelAdd'}
        g.add_a_channel(input_2_from_htsp)
        self.assertEqual(g.channel(8).name, "More4")

    def test_add_a_programme(self):
        input_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_from_htsp)
        more_input_from_htsp={'eventId': 116107, 'serieslinkId': 76020, 'contentType': 96, 'description': "It's the pop world cup and today's match is the quarter final between Rihanna and Lady Gaga. This could go either way. It's time to decide which stand you'll be seated in!", 'title': 'Pop World Cup: Rihanna v Lady Gaga', 'nextEventId': 116109, 
                              'channelId': 7, 'stop': 1404492000, 'episodeId': 116108, 'start': 1404489600, 'method': 'eventAdd'}
        g.add_a_programme(more_input_from_htsp)
        self.assertEqual(g.channel(7).listing[0].title,'Pop World Cup: Rihanna v Lady Gaga')
        self.assertEqual(g.listing(channel_id=7)[0].start,1404489600)
        
    def test_get_a_programme_from_listing_by_freeview_channel(self):
        input_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_from_htsp)
        more_input_from_htsp={'eventId': 116107, 'serieslinkId': 76020, 'contentType': 96, 'description': "It's the pop world cup and today's match is the quarter final between Rihanna and Lady Gaga. This could go either way. It's time to decide which stand you'll be seated in!", 'title': 'Pop World Cup: Rihanna v Lady Gaga', 'nextEventId': 116109, 
                              'channelId': 7, 'stop': 1404492000, 'episodeId': 116108, 'start': 1404489600, 'method': 'eventAdd'}
        g.add_a_programme(more_input_from_htsp)
        self.assertEqual(g.channel(channel_id=7).listing[0].title,'Pop World Cup: Rihanna v Lady Gaga')
        self.assertEqual(g.listing(channel_number=18)[0].start,1404489600)
        
    def test_add_two_programmes_on_same_channel(self):
        input_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_from_htsp)
        more_input_from_htsp={'eventId': 116107, 'serieslinkId': 76020, 'contentType': 96, 'description': "It's the pop world cup and today's match is the quarter final between Rihanna and Lady Gaga. This could go either way. It's time to decide which stand you'll be seated in!", 'title': 'Pop World Cup: Rihanna v Lady Gaga', 'nextEventId': 116109, 
                              'channelId': 7, 'stop': 1404492000, 'episodeId': 116108, 'start': 1404489600, 'method': 'eventAdd'}
        g.add_a_programme(more_input_from_htsp)
        self.assertEqual(g.listing(channel_id=7)[0].title,'Pop World Cup: Rihanna v Lady Gaga')
        another_show_from_htsp={'eventId': 116108, 'serieslinkId': 76001, 'contentType': 96,
                                 'description': "It isn't the pop world cup and tomorrrow's match is the final between Madonna and Bob Dylan. This could go either way. It's time to decide which stand you'll be seated in!", 
                                 'title': 'Pop World Cup: Madonna v Bob Dylan', 'nextEventId': 116109, 
                                 'channelId': 7, 'stop': 1404498000, 'episodeId': 116200, 'start': 1404489700, 'method': 'eventAdd'}
        g.add_a_programme(another_show_from_htsp)
        self.assertEqual(g.listing(channel_id=7)[1].title,'Pop World Cup: Madonna v Bob Dylan')
        self.assertEqual(g.listing(channel_id=7)[1].start,1404489700)
        
    def test_add_two_programmes_on_two_different_channels(self):
        input_1_from_htsp={'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'}
        g=guide_model.Guide()
        g.add_a_channel(input_1_from_htsp)
        self.assertEqual(g.channel(7).name, "4Music")
        input_2_from_htsp={'eventId': 116108, 'tags': [1, 2, 3], 'nextEventId': 116110, 'channelId': 8, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': 'More4', 'method': 'channelAdd'}
        g.add_a_channel(input_2_from_htsp)
        self.assertEqual(g.channel(8).name, "More4")
        more_input_from_htsp={'eventId': 116107, 'serieslinkId': 76020, 'contentType': 96, 
                              'description': "It's the pop world cup and today's match is the quarter final between Rihanna and Lady Gaga. This could go either way. It's time to decide which stand you'll be seated in!", 'title': 'Pop World Cup: Rihanna v Lady Gaga', 
                              'nextEventId': 116109, 'channelId': 7, 'stop': 1404492000, 
                              'episodeId': 116108, 'start': 1404489600, 'method': 'eventAdd'}
        g.add_a_programme(more_input_from_htsp)
        # first show is on channel id 7
        self.assertEqual(g.listing(channel_id=7)[0].title,'Pop World Cup: Rihanna v Lady Gaga')
        another_show_from_htsp={'eventId': 116108, 'serieslinkId': 76001, 'contentType': 96,
                                 'description': "It isn't the pop world cup and tomorrrow's match is the final between Madonna and Bob Dylan. This could go either way. It's time to decide which stand you'll be seated in!", 
                                 'title': 'Pop World Cup: Madonna v Bob Dylan', 'nextEventId': 116109, 
                                 'channelId': 8, 'stop': 1404498000, 'episodeId': 116200, 'start': 1404489700, 'method': 'eventAdd'}
        g.add_a_programme(another_show_from_htsp)
        # second one is on channel id 8
        self.assertEqual(g.listing(channel_name="More4")[0].title,'Pop World Cup: Madonna v Bob Dylan')
        
        self.assertEqual(g.channel(8).listing[0].title,
                         g.listing(channel_name="More4")[0].title)

    def test_add_four_programmes_on_two_different_channels_in_chronological_order(self):
        
        g=guide_model.Guide()
        g.add_a_channel({'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 7, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': '4Music', 'method': 'channelAdd'})
        self.assertEqual(g.channel(7).name, "4Music")
        
        
        g.add_a_programme({'eventId': 116107, 'serieslinkId': 76020, 'contentType': 96, 
                              'description': "It's the pop world cup and today's match is the quarter final between Rihanna and Lady Gaga. This could go either way. It's time to decide which stand you'll be seated in!", 'title': 'Pop World Cup: Rihanna v Lady Gaga', 
                              'nextEventId': 116109, 'channelId': 7, 'stop': 1404492000, 
                              'episodeId': 116108, 'start': 1404489600, 'method': 'eventAdd'})
        g.add_a_programme({'eventId': 116114, 'serieslinkId': 76020, 'contentType': 96, 
                              'description': "It's the pop world cup and today's match is the semi final between Rihanna and Lady Gaga. This could go either way. It's time to decide which stand you'll be seated in!", 'title': 'Pop World Cup: Rihanna v Lady Gaga', 
                              'nextEventId': 116115, 'channelId': 7, 'stop': 1404493200, 
                              'episodeId': 116110, 'start': 1404492000, 'method': 'eventAdd'})

        # first show is on channel id 7
        self.assertEqual(g.listing(channel_id=7)[0].title,'Pop World Cup: Rihanna v Lady Gaga')
        
        g.add_a_channel({'eventId': 116107, 'tags': [1, 2, 3], 'nextEventId': 116109, 'channelId': 8, 'channelNumber': 18, 'services': [{'type': 'SDTV', 'name': 'DiBcom 7000PC/West: 722,000 kHz/4Music'}], 'channelName': 'More4', 'method': 'channelAdd'})
        self.assertEqual(g.channel(8).name, "More4")
 
        g.add_a_programme({'eventId': 116108, 'serieslinkId': 76001, 'contentType': 96,
                                 'description': "It isn't the pop world cup and tomorrrow's match is the final between Madonna and Bob Dylan. This could go either way. It's time to decide which stand you'll be seated in!", 
                                 'title': 'Pop World Cup: Madonna v Bob Dylan', 'nextEventId': 116109, 
                                 'channelId': 8, 'stop': 1404498000, 'episodeId': 116200, 'start': 1404489700, 'method': 'eventAdd'})
        g.add_a_programme({'eventId': 116116, 'serieslinkId': 76001, 'contentType': 96,
                                 'description': "It isn't the pop world cup and tomorrrow's match is the final between Madonna and Bob Dylan. This could go either way. It's time to decide which stand you'll be seated in!", 
                                 'title': 'Pop World Cup: Barry White v Rod Stewart', 'nextEventId': 116117, 
                                 'channelId': 8, 'stop': 1404500000, 'episodeId': 116200, 'start': 1404499000, 'method': 'eventAdd'})
        # second one is on channel id 8
        self.assertEqual(g.listing(channel_name="More4")[0].title,'Pop World Cup: Madonna v Bob Dylan')
        self.assertEqual(g.listing(channel_name="More4")[1].title,'Pop World Cup: Barry White v Rod Stewart')
        
        self.assertEqual(g.channel(8).listing[0].title,
                         g.listing(channel_name="More4")[0].title)
        
class ChannelTest(unittest.TestCase):
    def test_programmes_are_added_in_chronological_order(self):
        c=guide_model.Channel(8,name="More4",number=18 )
        # args are start time, title, details ...
        p0=guide_model.Programme(0,"first show","nonsense")
        p1=guide_model.Programme(1,"second show","more nonsense")
        p2=guide_model.Programme(2,"third show","the worst nonsense")
        p3=guide_model.Programme(3,"fourth show","excessive nonsense")
        c.add_programme(p1)
        c.add_programme(p3)
        c.add_programme(p2)
        c.add_programme(p0)
                
        self.assertEqual(c.listing[0].title,"first show")
        self.assertEqual(c.listing[1].title,"second show")
        self.assertEqual(c.listing[2].title,"third show")
        self.assertEqual(c.listing[3].title,"fourth show")

class ChannelInfoTests(unittest.TestCase):
    def test_create_a_channel(self):
        c=guide_model.Channel(8,name="More4",number=18 )
        self.assertEqual(c.name, "More4")
        self.assertEqual(c.number, 18)