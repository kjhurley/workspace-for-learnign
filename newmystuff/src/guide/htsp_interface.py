'''
Created on 10 Jul 2014

@author: khurley
'''

import guide_model
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
    def programe(cls,event_msg):
        if 'description' in event_msg:
            return guide_model.Programme(start_time=event_msg["start"],   
                   title=event_msg["title"], 
                   details=event_msg["description"])
        else:
            logging.debug( "no description in "+str(event_msg))
            raise ConversionError("cannot create programme from input - no description present")