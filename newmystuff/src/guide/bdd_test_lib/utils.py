import pickle
def read_from_epg_dump(filename):
    msg_list=[]
    with open(filename) as a_file:
        for line in a_file.readlines():
            msg_list+=[eval(line)]
    return msg_list

    