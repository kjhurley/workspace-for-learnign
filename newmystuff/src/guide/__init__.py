""" EPG Guide domain modelling

@startuml
class Recording {
  bool is_watched()
  Search recorded_by()
  Programme info()
}
class Programme {
  void record()
  void like_this()
}
class Channel {
}
Channel o-- "0..*" Programme: listing
Guide o-- "0..*" Channel
class Guide
Archive o-- "0..*" Recording
Recording *-- Programme
Recording o-- "0.." Search
@enduml



@startuml
actor system
system->Guide: create
system->Guide: add_a_channel(details)
Guide->Channel: create(details)
system->Guide: add_a_programme(details)
Guide->Programme: create
system->Guide: add_a_programme
system->Guide: listing (channel_id = 7)
Guide->Channel: get_listing
@enduml

@startuml
actor system
system->Archive: create
system->Programme: prog=create(channel, start time, title, description)
system->Archive: add_recording(prog, recorded)
system->Archive: is_recorded?
@enduml

 """