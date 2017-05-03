import shodan
import sys
from datetime import datetime

SHODAN_API_KEY = raw_input("Enter your Shodan API key: ")
query = raw_input("Enter desired search term e.g. apache: ")


api = shodan.Shodan(SHODAN_API_KEY)

try:
    results = api.search(query)
 
    print 'Results found: %s' % results['total']
    for result in results['matches']:
            print 'IP: %s' % result['ip_str']
            print result['data']
            print ''
except shodan.APIError, e:
        print 'Error: %s' % e
