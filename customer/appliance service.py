
appliances = []

def register_appliance(name, watt, quantity, usage_hours):
    item = {
        "name": name,
        "watt": watt,
        "quantity": quantity,
        "usage_hours": usage_hours,
    }
    appliances.append(item)
    print("Appliance registered successfully!")

def list_appliances():
    if not appliances:
        print("No appliances registered.")
        return
    print("\nAppliance List:")
    for a in appliances:
        print(f"{a['name']} - {a['watt']}W, Qty: {a['quantity']}, Usage: {a['usage_hours']} hrs/day")