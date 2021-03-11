

class w6

def __init__(self, url_list)
    pass

def downloaded(url,filename) #raises NotFoundException when url returns 404
    pass

def __iter__(self):
    return self

def __next__(self):
    if random.choice(["go","go","go","go","stop"]) == "stop":
        raise StopIteration
