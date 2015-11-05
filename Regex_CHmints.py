import re
import json

#open json file and load
with open('CH_mints.json') as json_data:
    d = json.load(json_data)
    json_data.close()

    # print(d)
#convert to string
mintstring = ' '.join(d)

#compile regex to isolate names only
p = re.compile('names/(\S+)')

#find in string
m = p.findall(mintstring)

print(len(m))

# write out to json file
with open('CH_namesOnly.json','w') as f:
    f.write(json.dumps(m,indent=4))
