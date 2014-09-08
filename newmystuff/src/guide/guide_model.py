""" A model for EPG Guide

Channels is a dict with key per channel
Each channel has a listing - a list of broadcasts (airings of programmes) in time order

{
   BBC 1 : [9am: news, 10am: daytime, ...
   BBC 2 : [9:15am : sport, 9:45am: furnture ...]
}

although the keys are actually 'channel id' and the times are seconds since 1970

Users specify one off timers to record or smart-timers to record multiple connected broadcasts

Recorded broadcasts can be used to find related ones


"""

import logging

class Recording:
    """ a recorded programme """
    def is_watched(self):
        pass
    
    def recorded_by(self):
        """ returns the search object that triggered the recording """
        pass
    
    def info(self):
        """ programme info of the original broadcast """
        pass

class Programme:
    """ holds information on a single broadcast entity
    
      start_time - when the broadcast commenced
      title - what it's called
      details - whatever description was supplied by the guide
      channel_id - id of channel it was recorded on
      """
    def __init__(self, start_time, title, details, channel_id):
        self.start=start_time
        self.title=title
        self.details=details  
        self.cid = channel_id

    def record(self):
        """ user requests to record this programme """
        pass
    
    def like_this(self):
        """ used to find other programmes like this one """
        pass

    @classmethod
    def from_htsp(cls,event_msg):
        if 'description' in event_msg:
            return cls(start_time=event_msg["start"],   
                   title=event_msg["title"], 
                   details=event_msg["description"])
        else:
            logging.debug( "no description in "+str(event_msg))
            raise RuntimeError("cannot create programme from input - no description present")


class Channel:
    """ knows about channels - their names, channel id etc 
    
        channel_id - a unique number for the channel used internally
        channel_name - what the broadcaster calls the channel e.g. BBC One
        channel_number - e.g. freeview channel
        
        channel also presents an iterator interface for iterating over the listing
    """
    def __init__(self, channel_id, name, number):
        self.cid = channel_id
        self.name=name
        self.number=number
        self.listing=[]

    def __repr__(self):
        return "(%d) %s - %d"%(self.cid, self.name, self.number)
    
    def htsp_add_programme_event(self, event_msg):
        try:
            self.listing+=[Programme.from_htsp(event_msg)]
        except RuntimeError:
            #logging.debug("couldn't add a programme")
            pass
    
    
    def add_programme(self, programme):
        """ insert programme into the listing in chronological order """
        self.listing+=[programme]
        if ( len(self.listing)>1 and 
               not programme.start > self.listing[-2].start):
            self.listing.sort(lambda x,y: 
                    cmp(x.start,y.start))                    

class Guide:
    """ a guide holds information about whats on - it consists of channels """
    def __init__(self):
        self._channel_info={}
        self._channels={} # key by channelId
        
    def add_a_channel(self, new_channel):
        """ add a channel to the guide """
        new_id=new_channel.cid
        self._channel_info[new_id] = new_channel
        self._channels[new_id]=[]

    def channel(self, channel_id):
        """ identify the name of the given channel """
        return self._channel_info[channel_id]
    
    def add_a_programme(self, new_programme):
        """ add a single show (on a given channel) """
        channel_id=new_programme.cid
        try:
            self._channel_info[channel_id].add_programme(new_programme)
            self._channels[channel_id]+=[]
        except RuntimeError:
            #logging.info("missing stuff!")
            pass    
        
        
    def now(self, **kwargs):
        """ what's on now on specified channel 
        
            channel specified by id, name or freeview number
        """
        return self.listing(**kwargs)[0]
    
    def next(self, **kwargs):
        """ what's on next on specified channel 
        
            channel specified by id, name or freeview number
        """
        return self.listing(**kwargs)[1]
    
    def next_plus_1(self, **kwargs):
        """ what's on next plus one on specified channel 
        
            channel specified by id, name or freeview number
        """
        return self.listing(**kwargs)[2]
    
    def listing(self, **kwargs):
        """ listing can be searched using channel name, id or number 
        
        What's returned is a list of programmes on that channel.
        """
        if "channel_id" in kwargs:
            return self._channel_info[kwargs['channel_id']].listing
        elif "channel_name" in kwargs:
            for chan_id in self._channel_info:
                if self._channel_info[chan_id].name==kwargs['channel_name']:
                    return self._channel_info[chan_id].listing
            raise IndexError("name %s not found in %s"%(
                  kwargs['channel_name'], self._channel_info))
                    
            return self._channels[kwargs['channel_name']]
        elif "channel_number" in kwargs:
            number=int(kwargs['channel_number'])
            for chan_id in self._channel_info:
                if int(self._channel_info[chan_id].number) == number:
                    return self._channel_info[chan_id].listing
            raise IndexError("number %d not found in %s"%(
                             number, self._channel_info))
            

def populate_guide():
    pass

