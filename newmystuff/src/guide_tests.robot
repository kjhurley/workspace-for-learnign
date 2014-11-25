The first set of tests is about building up the list of channels and
programmes on those channels based on the updates coming from
tvheadend.


*** Test Cases ***
Check now showing on channel 18    Is_status                   initialised
     Is on now on channel number   18            Top 50 Collaborations of the 21stC 
     [Tags]   Sunny Day   Listing

Check now showing on More 4        Is_status  initialised
     Is on now on channel named  More 4   Location, Location, Location
     [Tags]   Sunny Day   Listing

Check not showing on channel 18     Is_status                     initialised                  
          Is not on now on channel number   18             New quiz   
          [Tags]                        Sunny Day    Listing  

Check not showing on channel id 48     Is_status                     initialised                  
          Is not on now on channel number   18             New quiz   
          [Tags]                        Sunny Day    Listing  
                                                                                                                        
Check next showing on More 4     Is_status                     initialised                  
          Is on next on channel named   More 4     Location, Location, Location  
          [Tags]                        Sunny Day    Listing  
                                                                                                  
Check next plus 1 showing on More 4     Is_status                     initialised                  
          Is on next plus 1 on channel named   More 4     Help! My House Is Falling Down  
          [Tags]                        Sunny Day    Listing  
                                                                                            
 

*** Setting ***
Library     robot_utils/bdd_tests.py         
                                   

*** Setting ***
Suite Setup      Populate guide       
Suite Teardown                        







