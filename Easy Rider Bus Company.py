# version with auto-detection of bus numbers
import json
import re

# reading json file from the input and saving in a json format
data = json.loads(input())  # proper way to read the json file

# the below line is for test purposes. pretty handy while testing new features
# data = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]
# [{'bus_id': 128, 'stop_id': 1, 'stop_name': 'Prospekt Avenue', 'next_stop': 3, 'stop_type': 'S', 'a_time': '08:12'}, {'bus_id': 128, 'stop_id': 3, 'stop_name': 'Elm Street', 'next_stop': 5, 'stop_type': '', 'a_time': '08:19'}, {'bus_id': 128, 'stop_id': 5, 'stop_name': 'Fifth Avenue', 'next_stop': 7, 'stop_type': 'O', 'a_time': '08:25'}, {'bus_id': 128, 'stop_id': 7, 'stop_name': 'Sesame Street', 'next_stop': 0, 'stop_type': 'F', 'a_time': '08:37'}, {'bus_id': 256, 'stop_id': 2, 'stop_name': 'Pilotow Street', 'next_stop': 3, 'stop_type': 'S', 'a_time': '09:20'}, {'bus_id': 256, 'stop_id': 3, 'stop_name': 'Elm Street', 'next_stop': 6, 'stop_type': '', 'a_time': '09:45'}, {'bus_id': 256, 'stop_id': 6, 'stop_name': 'Sunset Boulevard', 'next_stop': 7, 'stop_type': '', 'a_time': '09:59'}, {'bus_id': 256, 'stop_id': 7, 'stop_name': 'Sesame Street', 'next_stop': 0, 'stop_type': 'F', 'a_time': '10:12'}, {'bus_id': 512, 'stop_id': 4, 'stop_name': 'Bourbon Street', 'next_stop': 6, 'stop_type': 'S', 'a_time': '08:13'}, {'bus_id': 512, 'stop_id': 6, 'stop_name': 'Sunset Boulevard', 'next_stop': 0, 'stop_type': 'F', 'a_time': '08:16'}]


# declaring functions:
def print_report():
    # report function is re-written for the #2-4 stage just to output and calculate 3 relevant fields
    print(f"Type and required field validation: {stop_name_errors + stop_type_errors + a_time_errors} errors")
    # print(f"bus_id: {bus_id_errors}")
    # print(f"stop_id: {stop_id_errors}")
    print(f"stop_name: {stop_name_errors}")
    # print(f"next_stop: {next_stop_errors}")
    print(f"stop_type: {stop_type_errors}")

    print(f"a_time: {a_time_errors}\n\n")


def print_stops_report():
    # This function prints out the bus_id and number of the stops it has
    for line in stops_dict:
        print(f"bus_id: {line} stops {len(stops_dict[line])}")


def time_format_check(time):
    # implementing regex here to make sure our time has correct 24h format.
    # this function checks whether the time format provided in JSON file is valid.
    # if one of the tests is not passed, the False value is returned.
    if not isinstance(time, str):
        return False
    if len(time) != 5:
        return False
    else:
        # variable current time has been removed. now we use dictionary to check the most recent stop timing for a particular bus
        template = r'\A([0-1]\d|2[0-3]):([0-5]\d)$'
        match = re.match(template, time)

        if match:
            # here can be a function call. or rewriting in 1 line
            return True
        else:
            return False


def time_travel_check():  # data
    # also it checks if the next stop has "later" time than the previous one.
    # if one of the tests is not passed, the False value is returned.
    stops_timing = dict.fromkeys(stops_list, "00:00")
    # make sure that time and bus_id passed to the function together
    errors_dict = dict()
    for x in data:
        line_id = x["bus_id"]
        station = x["stop_name"]
        time = x["a_time"]
        if int(stops_timing[line_id][0:2]) * 60 + int(stops_timing[line_id][3:5]) < int(time[0:2]) * 60 + int(time[3:5]):
            stops_timing[line_id] = time
            pass
        else:
            if line_id not in errors_dict:
                errors_dict[line_id] = station
            else:
                continue
    if len(errors_dict) == 0:
        print("OK")
    else:
        print('Arrival time test:')
        for line in errors_dict:
            print(f'bus_id line {line}: wrong time on station {errors_dict[line]}')
        return False


def bus_id_check(id_):
    # This function checks if bus_id variable format is correct and returns True or False for further processing
    if not isinstance(id_, int) or id_ == "":
        return False
    return True


def stop_id_check(id_):
    # This function checks if stop_id variable format is correct and returns True or False for further processing
    if not isinstance(id_, int) or id_ == "":
        return False
    return True


def stop_name_check(name):
    # implementing regex here to check if stop name format is ok
    # This function checks if stop_name variable format is correct and returns True or False for further processing
    if not isinstance(name, str) or name == "":
        return False
    else:
        template = r'([A-Z][a-z]+ ?){1,2} {1,2}(Road|Avenue|Boulevard|Street)$'
        match = re.match(template, name)
        return True if match else False


def next_stop_check(stop):
    # This function checks if next_stop variable format is correct and returns True or False for further processing
    if not isinstance(stop, int) or stop == "":
        return False
    return True


def stop_type_check(type_):
    # This function checks if stop_type variable format is correct and returns True or False for further processing
    if not isinstance(type_, str):
        return False
    else:
        # making sure that stop_type has 'SOF' or '' format
        template = r'[SOF]?$'
        match = re.match(template, type_)
        return True if match else False


def start_stop_transfer():
    # This function checks if the bus has exactly one start and one final stop
    # also it will either terminate the program and print an error message or it will print out the information regarding the start, finish and transfer stops
    start_stops = dict.fromkeys(stops_list, [])
    finish_stops = dict.fromkeys(stops_list, [])
    transfer_stops = [line['stop_name'] for line in data]
    transfer_stops = [stop for stop in transfer_stops if transfer_stops.count(stop) > 1]
    transfer_stops = sorted(list(set(transfer_stops)))

    for i in stops_list:
        start_stops[i] = [line['stop_name'] for line in data if (line['bus_id'] == i and line['stop_type'] == 'S')]
        finish_stops[i] = [line['stop_name'] for line in data if (line['bus_id'] == i and line['stop_type'] == 'F')]

    for line in start_stops:
        if len(start_stops[line]) == 0:
            print(f'There is no start or end stop for the line: {line}.')
            exit()
    for line in finish_stops:
        if len(finish_stops[line]) == 0:
            print(f'There is no start or end stop for the line: {line}.')
            exit()

    s1 = [x[0] for x in list(start_stops.values())]
    f1 = [x[0] for x in list(finish_stops.values())]
    s1 = sorted(list(set(s1)))
    f1 = sorted(list(set(f1)))

    print(f"""Start stops: {len(s1)} {s1}
Transfer stops: {len(transfer_stops)} {transfer_stops}
Finish stops: {len(f1)} {f1}""")


# Declaring variables:
# declaring "error" variables
bus_id_errors, stop_id_errors, stop_name_errors, next_stop_errors, stop_type_errors, a_time_errors, total_errors = 0, 0, 0, 0, 0, 0, 0

# creating the stops list:
stops_list = [x[y] for x in data for y in x if y == 'bus_id']
stops_list = list(set(stops_list))  # set() function used to remove duplicates from the list, list() function used to make list from the set.
# taking values from stops_list as keys, and empty lists as values arrays for the stop_name values:
stops_dict = dict.fromkeys(stops_list, [])


# assigning stop name values to the stops_dict variable
for _ in range(len(stops_dict)):
    for bus in stops_dict:
        stops_dict[bus] = [line[value] for line in data for value in line if value == 'stop_name' and line['bus_id'] == bus]


# processing json variable data to create the dictionary(without duplicates) with the following information:
# bus_id as a key
# stop_name and stop_type as values in a list
stop_names_types = dict.fromkeys(stops_list, [])
for _ in range(len(stops_dict)):
    for bus in stop_names_types:
        stop_names_types[bus] = [line[value] for line in data for value in line if any([(value == 'stop_name' and line['bus_id'] == bus), (value == 'stop_type' and line['bus_id'] == bus)])]

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

time_travel_check()
