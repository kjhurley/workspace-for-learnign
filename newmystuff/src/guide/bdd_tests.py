import guide_model
import bdd_test_lib.utils
import sys
import logging

class bdd_tests:
    GUIDE=None
    def __init__(self):
        logging.debug("bdd_tests.__init__")
        self._status = 'uninitialised'
        self.guide = self.__class__.GUIDE
        if self.guide is not None:
            self._status = 'initialised'
 
    @classmethod
    def populate_guide(cls):
        logging.debug("bdd_tests.populate_guide()")
        if cls.GUIDE is None:
            cls.GUIDE=guide_model.Guide()
            htsp_msgs=bdd_test_lib.utils.read_from_epg_dump("bdd_test_lib/epg.dump")
            for msg in htsp_msgs:
                if 'method' in msg:
                    if 'channelAdd' == msg['method']:
                        cls.GUIDE.add_a_channel(msg)
                        logging.debug("adding "+str(msg))
                    elif 'eventAdd' == msg['method']:
                        cls.GUIDE.add_a_programme(msg)
                        logging.debug("adding "+str(msg))
        assert len(cls.GUIDE._channel_info)>0

    def is_on_now_on_channel_number(self, number, title):
        on_now=self.guide.now(channel_number=number)
        assert title == on_now.title, "%s != %s"%(on_now.title ,title)

    def is_on_next_on_channel_number(self, number, title):
        on_next=self.guide.next(channel_number=number)
        assert title == on_next.title, "%s != %s"%(on_next.title ,title)

    def is_on_next_on_channel_named(self, name, title):
        on_next=self.guide.next(channel_name=name)
        try:
            assert title == on_next.title, "%s != %s"%(on_next.title ,title)
        except AssertionError:
            logging.error("listing for "+str(name,["%d: %s"%(show.start,show.title) for show in self.guide.listing(channel_name=name)]))
        

    def is_on_next_plus_1_on_channel_named(self, name, title):
        on_next_1=self.guide.next_plus_1(channel_name=name)
        try:
            assert title == on_next_1.title, "%s != %s"%(on_next_1.title ,title)
        except AssertionError:
            logging.error("listing for "+str(name,["%d: %s"%(show.start,show.title) for show in self.guide.listing(channel_name=name)]))
        
    def is_on_now_on_channel_named(self, name, title):
        assert title == self.guide.listing(channel_name=name)[0].title, "%s != %s"%(self.guide.listing(channel_name=name)[0].title ,title)
        
    def is_not_on_now_on_channel_number(self, number, title):
        assert title != self.guide.listing(channel_number=number)[0].title, "%s == %s"%(self.guide.listing(channel_number=number)[0].title ,title)
        
    def is_status(self, expected_status):
        assert self._status == expected_status, "%s != %s"%(self._status, expected_status)
