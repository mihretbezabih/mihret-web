
def calculate_bill(total_consumption):
	"""Calculate the bill from total consumption (kWh).

	The function accepts numeric input and returns the total payable amount
	(energy cost + service charge). Raises TypeError for invalid input.
	"""
	try:
		total = float(total_consumption)
	except (TypeError, ValueError):
		raise TypeError("total_consumption must be a number")

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

	return energy_cost + service_charge

