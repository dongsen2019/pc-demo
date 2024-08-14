import requests

s = ["218.95.37.251:25160", "221.131.165.71:27063","36.151.195.43:40346","122.232.237.78:17880","171.41.151.195:22718","58.208.171.18:18668","219.150.218.21:25221","122.239.136.122:22167","221.131.165.73:27438","218.95.37.135:40320","222.89.70.65:25024","219.150.218.53:40230","223.113.54.130:27439","221.131.165.73:27255","218.95.37.135:40042","125.87.81.38:23629","218.95.37.135:40259","221.229.212.173:25144","223.113.54.130:27018","221.234.29.186:22438","219.150.218.21:25030","219.150.218.53:40594","36.151.195.43:40021","223.113.54.130:27168","36.151.195.43:40075","114.106.134.165:18963","218.95.37.251:25061","223.113.54.130:27315","221.229.212.170:40502","36.151.195.43:40858","219.150.218.53:40250","223.113.54.130:27365","182.106.136.210:25154","221.131.165.73:27415","221.131.165.71:27115","223.113.54.130:27214","36.40.195.51:18552","221.131.165.73:27099","221.229.212.172:25044","218.95.37.135:40373","221.229.212.173:25237","219.150.218.53:40274","36.151.195.43:40136","223.113.54.130:27066","221.131.165.73:27158","115.211.23.53:23504","221.131.165.73:27475","223.113.54.130:27423","221.229.212.170:40607","219.150.218.53:40276","114.229.220.53:16864","182.106.136.210:25005","183.143.250.37:21975","123.180.168.141:22462","223.113.54.130:27165","223.113.54.130:27391","36.151.195.15:25117","36.151.195.43:40655","223.113.54.130:27271","221.131.165.73:27398","223.113.54.130:27299","221.131.165.73:27322","223.113.54.130:27468","122.239.186.184:16840","119.102.42.74:15112","123.180.169.9:18233","125.117.34.176:23499","36.40.194.60:18438","111.224.11.64:17162","122.242.100.170:21740","117.86.77.191:19061","219.150.218.21:25002","219.150.218.53:40156","123.160.10.195:25090","125.105.224.119:17046","122.232.237.190:17482","221.131.165.73:27155","114.106.171.74:16188","221.131.165.73:27219","221.131.165.73:27374","221.229.212.174:25199","221.234.31.66:22584","221.131.165.71:27067","221.131.165.71:27027","221.131.165.73:27176","222.89.70.171:25003","218.95.37.161:25035","221.131.165.73:27327","221.131.165.73:27583","221.229.212.170:40530","223.113.54.130:27306","221.131.165.73:27195","221.229.212.172:25202","219.150.218.53:40342","49.84.24.143:23213","116.208.197.250:18619","218.95.37.11:25086","36.151.195.15:25197","218.95.37.135:40265","223.113.54.130:27478","221.229.212.174:25003","221.131.165.73:27311","115.207.101.186:21822","110.184.178.252:17707","219.150.218.53:40190","223.113.54.130:27463","221.229.212.172:25065","125.105.226.209:23382","218.95.37.135:40272","36.151.195.15:25173","125.105.229.109:16545","221.131.165.73:27205","218.95.37.11:25001","218.95.37.161:25031","221.131.165.73:27371","223.113.54.130:27418","218.95.37.135:40238","123.160.10.195:25039","106.122.238.207:16298","114.218.152.88:18546","116.208.206.81:15775","36.151.195.43:40232","171.41.149.29:17374","36.151.195.43:40625","222.89.70.171:25243","223.113.54.130:27316","221.131.165.73:27138","223.113.54.130:27201","218.95.37.135:40173","218.95.37.11:25170","221.227.196.205:20090","221.234.29.96:16577","221.131.165.73:27286","36.151.195.43:40178","218.95.37.135:40130","221.229.212.170:40018","219.150.218.53:40087","221.229.212.170:40286","223.113.54.130:27137","221.229.212.172:25206","36.151.195.43:40713","221.229.212.173:25196","221.229.212.174:25002","36.151.195.43:40023","221.229.212.170:40219","219.150.218.53:40581","219.150.218.21:25223","119.102.40.96:17725","218.95.37.11:25234","223.113.54.130:27130","219.150.218.53:40066","221.229.212.172:25170","122.232.236.243:15638","42.51.45.30:18940","122.239.149.140:15446","218.95.37.135:40408","221.131.165.71:27347","222.89.70.171:25098","218.95.37.135:40315","180.121.190.169:19096","36.151.195.43:40163","36.151.195.15:25082","182.106.136.210:25017","223.113.54.130:27415","218.95.37.251:25094","218.95.37.135:40340","122.232.106.104:22788","221.229.212.170:40137","36.151.195.43:40372","223.113.54.130:27269","123.160.10.195:25002","221.229.212.171:25173","222.89.70.171:25001","218.95.37.251:25235","221.131.165.73:27315","182.106.136.210:25180","223.113.54.130:27331","218.95.37.135:40456","221.131.165.73:27302","180.121.145.245:18075","110.188.37.118:19651","125.113.130.206:22559","221.131.165.73:27115","221.229.212.170:40136","221.229.212.174:25127","221.131.165.71:27267","221.131.165.73:27424","218.95.37.251:25091","218.95.37.11:25192","223.113.54.130:27244","219.150.218.53:40777","221.229.212.171:25192","223.245.213.116:16043","218.95.37.135:40439","219.150.218.53:40123","221.229.212.170:40058","221.229.212.170:40617","221.229.212.172:25039","219.150.218.53:40164","218.95.37.251:25026"]
c = len(s)

# for i in s:
#     proxy = {
#         "https": "http://d3392397682:ebxl5k5p@{ip}".format(ip=i)
#     }
resp = requests.get("http://localhost:8000/view_study/", timeout=5)
print(resp.text)





