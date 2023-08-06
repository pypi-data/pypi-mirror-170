# Installation
Install the package from PyPi with `pip3 install redisgetapi`.  
# Usage 
The redis-get-api package comes handy when you want to use api endpoints that have restricted rate limits. It does  
exactly that by enforcing rate limits while preserving persistence in the local redis database for the required time limit.  
For instance if you are building upon twitter, and you intend to search tweets, you are only allowed say 450 requests within any
15 minutes (900 seconds) interval. This package will fetch the first result and cache it for the next 15 minutes when you are not allowed to hit the twitter API  
directly.  
## Requirements and parameters
You must install redis to use this application. You can use the application as a commandline interface for testing purposes, or within your scipt. The default parameters for redis host and port are 'localhost' and 6379 respectively. The other parameters are  
the url to be fetched and the expiry in seconds.

## Specific use case
Let the parameters be:
```
url = 'http://some/url/with/{your_api_key}/and/some/end_point/'
port = 6379 # unless you have your redis-server in a different port, this is the default
host = localhost
expiry = 300 # this is 5 minutes in seconds
```  

Call the application as follows

```
from redisgetapi.fetch import RedisEndPoint, cli_call, script_call # there are more functions there
```
Then you can define the function in your script as follows:  

```
def NgrokUrl(url,host,port,expire):
	return script_call(url,host,port,expire)

print(NgrokUrl(url,host,port,expire))
```

NB: The default variable in which redisgetapi is holding the response is 'res'  