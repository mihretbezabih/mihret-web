appliances = []


def register_appliance(name, watt, quantity, usage_hours):
	"""Register an appliance entry.

	Performs simple validation of numeric fields. Prints an error and returns
	without adding if values are invalid.
	"""
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
	"""Return the internal appliances list (read-only copy)."""
	return list(appliances)


if __name__ == "__main__":
	# Quick self-test so running this file shows expected output.
	print("Running appliance_service self-test...")
	register_appliance("Test Lamp", 60, 2, 5)
	register_appliance("Fan", 75, 1, 8)
	list_appliances()
	print("get_appliances() ->", get_appliances())