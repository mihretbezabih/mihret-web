appliances = []

def register_appliance(name, watt, quantity, usage_hours):
    appliance = {
        "name": name,
        "watt": watt,
        "quantity": quantity,
        "usage_hours": usage_hours,
    }
    appliances.append(appliance)
    print(f"Appliance registered: {name} (W:{watt}, Q:{quantity}, H:{usage_hours})")


def list_appliances():
    return appliances
