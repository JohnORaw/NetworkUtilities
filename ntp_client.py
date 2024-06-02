'''
NTPClient by: JOR
Simple test of NTP server
Alpha: 30APR24
'''
import ntplib
from time import ctime

ntpServer = "ie.pool.ntp.org"

ntp = ntplib.NTPClient()
ntpResponse = ntp.request(ntpServer)

if (ntpResponse):
   print(f"NTP Time: {ctime(ntpResponse.tx_time)}")
   print(f"Precision: {ntpResponse.precision}")
   print(f"Version: {ntpResponse.version}")
   print(f"Offset: {ntpResponse.offset}")
   print(f"Root delay: {ntpResponse.root_delay}")
   print(f"Root dispersion: {ntpResponse.root_dispersion}")
   print(f"Delay: {ntpResponse.delay}")
   print(f"Leap: {ntpResponse.leap}")
   print(f"Stratum of NTP server: {ntpResponse.stratum}")
