import json, re


data = json.loads(input())  # proper way to read the json file

#data = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]
[{'bus_id': 128, 'stop_id': 1, 'stop_name': 'Prospekt Avenue', 'next_stop': 3, 'stop_type': 'S', 'a_time': '08:12'}, {'bus_id': 128, 'stop_id': 3, 'stop_name': 'Elm Street', 'next_stop': 5, 'stop_type': '', 'a_time': '08:19'}, {'bus_id': 128, 'stop_id': 5, 'stop_name': 'Fifth Avenue', 'next_stop': 7, 'stop_type': 'O', 'a_time': '08:25'}, {'bus_id': 128, 'stop_id': 7, 'stop_name': 'Sesame Street', 'next_stop': 0, 'stop_type': 'F', 'a_time': '08:37'}, {'bus_id': 256, 'stop_id': 2, 'stop_name': 'Pilotow Street', 'next_stop': 3, 'stop_type': 'S', 'a_time': '09:20'}, {'bus_id': 256, 'stop_id': 3, 'stop_name': 'Elm Street', 'next_stop': 6, 'stop_type': '', 'a_time': '09:45'}, {'bus_id': 256, 'stop_id': 6, 'stop_name': 'Sunset Boulevard', 'next_stop': 7, 'stop_type': '', 'a_time': '09:59'}, {'bus_id': 256, 'stop_id': 7, 'stop_name': 'Sesame Street', 'next_stop': 0, 'stop_type': 'F', 'a_time': '10:12'}, {'bus_id': 512, 'stop_id': 4, 'stop_name': 'Bourbon Street', 'next_stop': 6, 'stop_type': 'S', 'a_time': '08:13'}, {'bus_id': 512, 'stop_id': 6, 'stop_name': 'Sunset Boulevard', 'next_stop': 0, 'stop_type': 'F', 'a_time': '08:16'}]

def print_report():
    # report function is re-written for the #2 stage just to output and calculate 3 relevant fields
    print(f"Type and required field validation: {stop_name_errors + stop_type_errors + a_time_errors} errors")
    # print(f"bus_id: {bus_id_errors}")
    # print(f"stop_id: {stop_id_errors}")
    print(f"stop_name: {stop_name_errors}")
    # print(f"next_stop: {next_stop_errors}")
    print(f"stop_type: {stop_type_errors}")

    print(f"a_time: {a_time_errors}\n\n")

def print_steps_report():
    for bus in stops_dict:
        print(f"bus_id: {bus} stops {len(stops_dict[bus])}")

def time_format_check(time):
    # implementing regex here to make sure our time has correct 24h format.
    global current_time
    if not isinstance(time, str):
        return False
    if len(time) != 5:
        return False
    else:
        template = r'\A([0-1]\d|2[0-3]):([0-5]\d)$'
        match = re.match(template, time)
        if match:
            current_time = int(a_time[0:2]) * 60 + int(a_time[3:5])
            return True
        else:
            return False
    return True


def bus_id_check(id):
    if not isinstance(id, int) or id == "":
        return False
    return True

def stop_id_check(id):
    if not isinstance(id, int) or id == "":
        return False
    return True

def stop_name_check(name):
    # implementing regex here to check if stop name format is ok
    if not isinstance(name, str) or name == "":
        return False
    else:
        template = r'([A-Z][a-z]+ ?){1,2} {1,2}(Road|Avenue|Boulevard|Street)$'
        match = re.match(template,name)
        return True if match else False

def next_stop_check(stop):
    if not isinstance(stop, int) or stop == "":
        return False
    return True

def stop_type_check(type):
    if not isinstance(type, str):
        return False
    else:
        # making sure that stop_type has 'SOF' or '' format
        template = r'[SOF]?$'
        match = re.match(template, type)
        return True if match else False

# declaring "error" variables
bus_id_errors, stop_id_errors, stop_name_errors, next_stop_errors, stop_type_errors, a_time_errors, total_errors, current_time = 0, 0, 0, 0, 0, 0, 0, 0

stops_dict = [y[x] for y in data for x in y if x == 'bus_id']
stops_dict = list(set(stops_dict)) # set() function used to remove duplicates from the list, list() function used to make list from the set.
stops_dict = dict.fromkeys(stops_dict, [])

for _ in range(len(stops_dict)):
    for bus in stops_dict:
        stops_dict[bus] = [x[y] for x in data for y in x if y == 'stop_name' and x['bus_id'] == bus]

for x in data:
    bus_id = x["bus_id"]
    stop_id = x["stop_id"]
    stop_name = x["stop_name"]
    next_stop = x["next_stop"]
    stop_type = x["stop_type"]
    a_time = x["a_time"]
    # the following line appends stop names into a stops_dict dictionary so we can count all them

    if not bus_id_check(bus_id):
        bus_id_errors += 1
        total_errors += 1

    if not stop_id_check(stop_id):
        stop_id_errors += 1
        total_errors += 1

    if not stop_name_check(stop_name):
        stop_name_errors += 1
        total_errors += 1

    if not next_stop_check(next_stop):
        next_stop_errors += 1
        total_errors += 1

    if not stop_type_check(stop_type):
        stop_type_errors += 1
        total_errors += 1

    if not time_format_check(a_time):
        a_time_errors += 1
        total_errors += 1


print_steps_report()
