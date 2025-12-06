
appliances = []


def register_appliance(name, watt, quantity, usage_hours):
	"""Register an appliance entry with basic validation."""
	try:
		w = float(watt)
		q = int(quantity)
		hrs = float(usage_hours)
	except (TypeError, ValueError):
		print("Invalid numeric values for appliance. Registration failed.")
		return

	item = {
		"name": str(name),
		"watt": w,
		"quantity": q,
		"usage_hours": hrs,
	}
	appliances.append(item)
	print("Appliance registered successfully!")


def list_appliances():
	"""Print the list of registered appliances."""
	if not appliances:
		print("No appliances registered.")
		return
	print("\nAppliance List:")
	for a in appliances:
		print(f"{a['name']} - {a['watt']}W, Qty: {a['quantity']}, Usage: {a['usage_hours']} hrs/day")


def get_appliances():
	"""Return a shallow copy of the registered appliances list."""
	return list(appliances)