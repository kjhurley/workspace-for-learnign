import guide.guide_model
import guide.htsp_interface
import logging

EPG_DUMP="/home/khurley/workspace/newmystuff/src/robot_utils/epg.dump"

def read_from_epg_dump(filename):
    msg_list=[]
    with open(filename) as a_file:
        for line in a_file.readlines():
            msg_list+=[eval(line)]
    return msg_list


class bdd_tests:
    """ support functionality for behaviour driven tests
    
    These methods are used by the robot tests
    """
    GUIDE=None
    def __init__(self):
        logging.debug("bdd_tests.__init__")
        self._status = 'uninitialised'
        self.guide = self.__class__.GUIDE
        if self.guide is not None:
            self._status = 'initialised'
 
    @classmethod
    def populate_guide(cls, epg_dump_file=EPG_DUMP):
        """ use an epg dump to fill the guide """
        logging.debug("bdd_tests.populate_guide()")
        if cls.GUIDE is None:
            cls.GUIDE=guide.guide_model.Guide()
            htsp_msgs=read_from_epg_dump(epg_dump_file)
            for msg in htsp_msgs:
                if 'method' in msg:
                    if 'channelAdd' == msg['method']:
                        cls.GUIDE.add_a_channel(
                            guide.htsp_interface.HtspInterface.channel(msg))
                        logging.debug("adding "+str(msg))
                    elif 'eventAdd' == msg['method']:
                        try:
                            cls.GUIDE.add_a_programme(
                                    guide.htsp_interface.HtspInterface.programme(msg))
                            logging.debug("adding "+str(msg))
                        except guide.htsp_interface.ConversionError:
                            logging.info("no description in %s"%str(msg))
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
            logging.error("listing for "+str(name,
                ["%d: %s"%(show.start,show.title) for show in self.guide.listing(channel_name=name)]))
        

    def is_on_next_plus_1_on_channel_named(self, name, title):
        found_title=self.guide.next_plus_1(channel_name=name).title
        try:
            assert title == found_title, "%s != %s"%(found_title ,title)
        except AssertionError:
            logging.error("listing for %s: %s"%(name,
                ["%d: %s"%(show.start,show.title) for show in self.guide.listing(channel_name=name)]))
        
    def is_on_now_on_channel_named(self, name, title):
        found_title=self.guide.listing(channel_name=name)[0].title
        assert title == found_title, "%s != %s"%(found_title ,title)
        
    def is_not_on_now_on_channel_number(self, number, title):
        found_title = self.guide.listing(channel_number=number)[0].title
        assert title != found_title,"%s == %s"%(found_title,title)
        
    def is_status(self, expected_status):
        assert self._status == expected_status, "%s != %s"%(self._status, expected_status)

if __name__ == '__main__':
    bdd_tests.populate_guide()
    inst=bdd_tests()
    print "\n".join(["%d: %s"%(p.start,p.title) for p in inst.guide.listing(channel_number=1)])