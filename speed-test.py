from speedtest import Speedtest
from sys import argv
from pprint import pprint
from datetime import datetime

class Speed_Data:
    def __init__(self, download_speed, upload_speed, Speedtest_server):
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        self.ts = datetime.now()
        self.Speedtest_server = Speedtest_server

def get_speed(source_ip):
    s = Speedtest(source_address = source_ip)
    s.get_best_server()
    download_speed = s.download()
    upload_speed = s.upload()
    pprint(s)
    print(type(s))
    Data = Speed_Data(download_speed, upload_speed, s)
    print(Data.download_speed, Data.upload_speed)
    return

if __name__ == '__main__':
    iface = argv[1] 
    get_speed(iface)


    '''{'cc': 'US',
     'country': 'United States',
     'd': 20.27510183716219,
     'host': 'speedtest.byu.edu:8080',
     'id': '4793',
     'lat': '40.2444',
     'latency': 15.582,
     'lon': '-111.6608',
     'name': 'Provo, UT',
     'sponsor': 'Brigham Young University',
     'url': 'http://speedtest.byu.edu/speedtest/upload.php',
     'url2': 'http://speedtest1.byu.edu/speedtest/upload.php'}'''


