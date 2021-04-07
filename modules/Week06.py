import requests as req

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

class TextComparer():

    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []

    def download(self,url):
        try:
            r = req.get(url)
            r.raise_for_status()
            with open(filename, 'w') as f:
                f.write(r.text)
        except req.exceptions.HTTPError as e:
            print(e.response.text)
        except FileNotFoundError:
            print("File not found, jerk!")
        
    def multi_download(self):
        urls = self.url_list
        with ThreadPoolExecutor(len(urls)) as ex:
            res = ex.map(self.download(), urls)
            #self.filenames = res
    #print(self.filenames)            

        

    
            
            
    def urllist_generator():
        pass

    def avg_vowels(text):
        pass



    def __iter__(self):
        return self

    def __next__(self):
        if random.choice(["go","go","go","go","stop"]) == "stop":
            raise StopIteration
