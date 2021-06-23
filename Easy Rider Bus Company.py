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
    global current_time
    if not isinstance(time, str):
        return False
    if len(time) != 5:
        return False
    if time[0:2].isdigit() and time[2] == ":" and time[3:].isdigit():
        current_time = int(a_time[0:2]) * 60 + int(a_time[3:5])
        return True
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
    if not isinstance(name, str) or name == "":
        return False
    return True

def next_stop_check(stop):
    if not isinstance(stop, int) or stop == "":
        return False
    return True

def stop_type_check(type):
    if not isinstance(type, str) or len(type) > 1:
        return False
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

print_report()
