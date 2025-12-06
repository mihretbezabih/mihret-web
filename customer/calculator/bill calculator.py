
def calculate_bill(total_consumption):
	"""Return total payable bill for a monthly consumption (kWh).

	Converts input to float and raises `TypeError` for invalid input.
	"""
	try:
		total = float(total_consumption)
	except (TypeError, ValueError):
		raise TypeError("total_consumption must be a number")

	# Step 1: Energy cost based on tariff
	if total <= 50:
		energy_cost = total * 0.273
		service_charge = 10
	elif total <= 100:
		energy_cost = total * 0.767
		service_charge = 42
	elif total <= 200:
		energy_cost = total * 1.625
		service_charge = 42
	elif total <= 300:
		energy_cost = total * 2.0
		service_charge = 42
	elif total <= 400:
		energy_cost = total * 2.2
		service_charge = 42
	elif total <= 500:
		energy_cost = total * 2.405
		service_charge = 42
	else:
		energy_cost = total * 2.481
		service_charge = 42

	# Step 2: Total bill = energy cost + service charge
	return energy_cost + service_charge

