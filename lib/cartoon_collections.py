
def roll_call_dwarves(dwarf_names):
    for index, name in enumerate(dwarf_names):
        print(f"{index+1}. {name}")

def summon_captain_planet(planteer_calls):
    new_list = []
    for call in planteer_calls:
        new_call = f"{call.capitalize()}!"
        new_list.append(new_call)
    return new_list

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
    

def find_the_cheese(list):
    for string in list:
        if (string == "cheddar") or (string == "gouda") or (string == "camembert"):
            return string
    return None
