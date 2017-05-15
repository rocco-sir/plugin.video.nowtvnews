import xbmcgui
import xbmcplugin
import xbmcaddon
import requests
import simplejson

addon = xbmcaddon.Addon()

url = "https://hkt-mobile-api.nowtv.now.com/09/1/getLiveURL"

# 331 Now Live
payload331 = "{\"channelno\":\"331\",\"mode\":\"prod\",\"audioCode\":\"\",\"format\":\"HLS\",\"callerReferenceNo\":\"20140702122500\"}"
# 332 Now News
payload332 = "{\"channelno\":\"332\",\"mode\":\"prod\",\"audioCode\":\"\",\"format\":\"HLS\",\"callerReferenceNo\":\"20140702122500\"}"

headers = {
    'cache-control': "no-cache",
    'user-agent': "NNC/1607081705 CFNetwork/711.1.12 Darwin/14.0.0" 
    }

response331 = requests.request("POST", url, data=payload331, headers=headers)
response332 = requests.request("POST", url, data=payload332, headers=headers)

#print(response.text)
parsed_data331 = simplejson.loads(response331.text)
parsed_data332 = simplejson.loads(response332.text)

#username = parsed_data['responseCode']
url331 = parsed_data331['asset']['hls']['adaptive'][0]
url332 = parsed_data332['asset']['hls']['adaptive'][0]

item332 = xbmcgui.ListItem('Now TV News 332')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url332 , item332, isFolder=0)

item331 = xbmcgui.ListItem('Now TV Live 331')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url331 , item331, isFolder=0)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

