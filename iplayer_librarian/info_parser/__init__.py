"""

@startuml
start
:restore last state;
note right: Use pickle?
:search latest available file info;
note right: look in iplayer log file and get data from htsp
:compare against last know files;
note right: last know files will be those listed in restored object
while (new file info?) is (found one)
  if (kind of info?) then (iplayer)
    :process iplayer file;
  else (htsp)
    :process htsp file;
  endif
  :build episode;
  :build new filename under xbmc;
  if (store using copy?) then (yes)
    :copy file to new filename;
  elseif (store using move?) then (yes)
    :move file to new filename;
    else (store using link)
     :link file to new filename;
  endif
  :record this file in list of know files;
endwhile (none)
:save current state including all known files;
stop
@enduml

Web Sequence Diagram for scenario...

@startuml
title High Level Librarian

Librarian->Librarian: Look for new files
alt new iplayer file info
Librarian->IPlayerInfoParser: parse (iplayer info)
IPlayerInfoParser->Episode: episode=create(parsed info)
else new tvheadend file bananna
Librarian->ParseHTSPInfo: parse(tvheadend info)
ParseHTSPInfo-> Episode: episode = create(parsed info)
end
Librarian->Episode: suitable_for_tvdb?
alt is suitable for tvdb
Librarian->StoreUsingTVDB: filer = create(episode)
else
Librarian->StoreUsingNfo: filer = create(episode)
end
Librarian->FilingAssistant: put new file in right location(episode, filer)
FilingAssistant->StoringRules: get rule for storing
alt use links
StoringRules->NewFileStoredAsALinkRule: rule = create
else use move
StoringRules->NewFileIsStoredUsingMove: rule = create
else use copy
StoringRules->NewFileIsStoredUsingCopy: rule = create
end
alt using tvdb
FilingAssistant->StoreUsingTVDB: store(rule, episode)
else
FilingAssistant->StoreUsingNfo: store(rule, episode)
end
@enduml


@startuml
title IPlayer Info suitable for Tvdb storing using link
Librarian->Librarian: Look for new files
note over Librarian: found new iplayer file info
Librarian->IPlayerInfoParser: episode, diskfile = parse (fileinfo)
IPlayerInfoParser->FileOnDisk: diskfile = create(fileinfo)
IPlayerInfoParser->IPlayerInfoParser: factory(parsed_info)
note over IPlayerInfoParser: factory identifies file info is for Horizon
IPlayerInfoParser->HorizonEpisode: episode=create(parsed info)
Librarian->HorizonEpisode: suitable_for_tvdb?
Librarian->TVDBFiler: filer = create(diskfile,episode)
Librarian->FilingAssistant: put new file in right location(episode, filer)
FilingAssistant->StoringRules: rule = get rule for storing
note over StoringRules: check current configuration settings
StoringRules->StoreAsALinkRule: rule = create
FilingAssistant->StoreAsALinkRule: store(filer,episode)
StoreAsALinkRule->HorizonEpisode: filename = generate_new_filename()
HorizonEpisode->TVDBFiler: filename = build_filename(episode)
TVDBFiler->HorizonEpisode: show, episode = get_show_and_episode()
TVDBFiler->TVDBAPI: result = search(show, episode)
opt search unsuccessful
TVDBFiler->HorizonEpisode: title, season, episode = get_show_season_and_episode()
TVDBFiler->TVDBApi: result = search(title, season, episode)
end
TVDBFiler-> TVDBFiler:filename = build(result) 
StoreAsALinkRule->StoreAsALinkRule: generate_link(filename)

@enduml


"""