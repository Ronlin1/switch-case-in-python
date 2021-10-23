def Sunday():
    return "Sunday"

def Monday():
    return "Monday"

def Tuesday():
    return "Tuesday"

def Wednesday():
    return "Wednesday"

def Thursday():
    return "Thursday"

def Friday():
    return "Friday"

def Saturday():
    return "Saturday"

switcher = {
    0: Sunday,
    1: Monday,
    2: Tuesday,
    3: Wednesday,
    4: Thursday,
    5: Friday,
    6: Saturday,
}

def switch(day0fWeek):
    return switcher.get(day0fWeek)()

print(switch(6))
