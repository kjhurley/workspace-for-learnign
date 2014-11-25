'''
Created on 10 Jul 2014

@author: khurley
'''

import guide.guide_model
import exceptions
import logging

class ConversionError(exceptions.Exception):
    pass

class HtspInterface(object):
    '''
    Wrapper around interactions between model objects and tvheadend
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @classmethod
    def channel(cls, event_msg):
        return guide.guide_model.Channel(channel_id=event_msg['channelId'], 
                     name=event_msg['channelName'], 
                     number=event_msg['channelNumber'])
    
    @classmethod
    def programme(cls,event_msg):
        if 'description' in event_msg:
            return guide.guide_model.Programme(start_time=event_msg["start"],   
                   title=event_msg["title"], 
                   details=event_msg["description"],
                   channel_id=event_msg["channelId"])
        else:
            logging.debug( "no description in "+str(event_msg))
            raise ConversionError("cannot create programme from input - no description present")
        
    @classmethod
    def recording(cls, event_msg):
        "def __init__(self, programme, recorded=True, watched=False, file_path=None):"
        event_msg['channelId']=event_msg['channel']
        new_prog=cls.programme(event_msg)
        logging.warn(event_msg)
        if event_msg['state'] == 'completed':
            return guide.guide_model.Recording(new_prog, recorded=True,watched=False,file_path=event_msg['path'])
        else:
            return guide.guide_model.Recording(new_prog,recorded=False)
        