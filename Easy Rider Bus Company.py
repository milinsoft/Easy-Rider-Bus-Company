# Write your awesome code here
import json
import string

data = json.loads(input())  # proper way to read the json file

def print_report():
    print(f"""Type and required field validation: {total_errors} errors
bus_id: {bus_id_errors}
stop_id: {stop_id_errors}
stop_name: {stop_name_errors}
next_stop: {next_stop_errors}
stop_type: {stop_type_errors}
a_time: {a_time_errors}\n\n""")


def time_format_check(time):
    if not isinstance(time, str):
        return False
    if time == "":
        return False
    if len(time) != 5:
        return False
    if time[0:2].isdigit() and time[2] == ":" and time[3:].isdigit():
        return True
    return True


bus_id_errors = 0
stop_id_errors = 0
stop_name_errors = 0
next_stop_errors = 0
stop_type_errors = 0
a_time_errors = 0

total_errors = 0
current_time = 0



for x in data:
    bus_id = x["bus_id"]
    stop_id = x["stop_id"]
    stop_name = x["stop_name"]
    next_stop = x["next_stop"]
    stop_type = x["stop_type"]
    a_time = x["a_time"]


    if not isinstance(bus_id, int) or bus_id == "":
        bus_id_errors += 1
        total_errors += 1
    if not isinstance(stop_id, int) or stop_id == "":
        stop_id_errors += 1
        total_errors += 1
    if not isinstance(stop_name, str) or stop_name == "":
        stop_name_errors += 1
        total_errors += 1
    if not isinstance(next_stop, int) or next_stop == "":
        next_stop_errors += 1
        total_errors += 1
    if not isinstance(stop_type, str) or len(stop_type) > 1:
        stop_type_errors += 1
        total_errors += 1



    # move it to function using global access
    if time_format_check(a_time):
        if int(current_time) < int(a_time[0:2]) * 60 + int(a_time[3:5]):
            current_time = int(a_time[0:2]) * 60 + int(a_time[3:5])

    else:
        a_time_errors += 1
        total_errors += 1

print_report()
