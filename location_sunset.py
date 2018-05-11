import plistlib
import os
import requests
import json

send_url_loc = 'http://freegeoip.net/json'
r = requests.get(send_url_loc)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']


# send_url_sunrise = 'https://api.sunrise-sunset.org/json?lat=' + str(lat) + '&lng=' +  str(lon)
# http://api.geonames.org/timezoneJSON?lat=47.01&lng=10.2
send_url_sunrise = 'http://api.geonames.org/timezoneJSON?lat=' + str(lat) + '&lng=' + str(lon) + '&username=markwk'
l = requests.get(send_url_sunrise)
j2 = json.loads(l.text)
sunrise = j2['sunrise']
sunset = j2['sunset']
timezone = j2['timezoneId']

# print timezone
# print sunrise
# print sunset

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

message = "%s" % (sunset)
notify("Sunset Today:", message)
