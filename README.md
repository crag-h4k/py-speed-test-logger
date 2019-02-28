Quick and dirty script to log internet speed test. 


Use at CLI as follows:

    ~$ python speed-test.py 127.0.0.1 /home/$USER/speed-test-log.csv


or as cronjob every 6 hours:

    0 */6 * * * /opt/miniconda3/bin/python /home/$USER/py-speed-test-logger /speedtest.py 127.0.0.1 /home/$USER/speed-test-log.csv

