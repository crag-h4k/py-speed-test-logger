from speedtest import Speedtest
from sys import argv

if __name__ == '__main__':
    iface_ip = argv[1]
    outfile = argv[2]
    s = Speedtest(source_address = iface_ip)
    server_info = s.get_best_server()
    s.upload()
    s.download()
    results_dict = s.results.dict()
    
    speed_data = []
    
    for key, value in results_dict.items():
        speed_data.append(str(key) + ': ' + str(value))
    
    stringified = ', '.join(speed_data).replace('{','').replace('}','').replace("'",'').replace('server: ','') + '\n'

    with open(outfile, 'a+') as f:
        f.write(stringified)
