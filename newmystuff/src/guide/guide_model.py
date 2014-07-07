""" A model for EPG Guide

Channels is a dict with key per channel
Each channel has a listing - a list of programmes in time order

{
   BBC 1 : [9am: news, 10am: daytime, ...
   BBC 2 : [9:15am : sport, 9:45am: furnture ...]
}

although the keys are actually 'channel id' and the times are seconds since 1970


"""


class Guide:
    """ a guide holds information about whats on - it consists of channels """
    def __init__(self):
        self._channelInfo={}
        
    def add_a_channel(self, new_channel_info):
        """ add a channel using info from tv head end """
        self._channelInfo[new_channel_info['channelId']]=new_channel_info['channelName']

    def channelName(self, channel_id):
        """ identify the name of the given channel """
        return self._channelInfo[channel_id]
    
    def add_a_programme(self, new_programme_info):
        """ add a single show (on a given channel) """
        
    def listing(self, channel_id):