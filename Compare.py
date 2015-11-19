import json
import difflib

matches = [ ]
with open('LJ_dict.json') as json_data_LJ:
    lj = json.load(json_data_LJ)
    json_data_LJ.close()

with open('CH_dict.json') as json_data_CH:
    ch = json.load(json_data_CH)
    json_data_CH.close()

for a_person in lj:

    for someone in ch:

        if a_person['first name'] == someone['first name']:
            if a_person['last name'] == someone['last name']:
                if a_person not in matches:
                    matches.append("LJ:" + " " + a_person['full name'] + "," + "CH:" + " " + someone['full name'])

print(matches)
