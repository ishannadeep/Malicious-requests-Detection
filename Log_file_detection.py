import re
path = '/Log.txt'
log_file = open(path,'r')
Lg=log_file.readlines()
for x in Lg:
 tab = re.compile(r'\s')
 Tab_Arr= tab.findall(x)
 IP=Tab_Arr[0]
 Date_1=Tab_Arr[1]
 Request_1=Tab_Arr[2]
 url_1=Tab_Arr[6]
 malicious=Request_1.compile(r'/(\.|(%|%25)2E)(\.|(%|%25)2E)(\/|(%|%25)2F|\\|(%|%25)5C)/i
')
 if malicious:
  print(Malicious request found!)