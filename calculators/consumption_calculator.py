def calculate_monthly_kwh(watt, quantity, usage_hours):
	"""Estimate monthly kWh consumption for an appliance or group.

	Parameters
	- watt: power rating in watts (number)
	- quantity: number of such appliances (number)
	- usage_hours: average daily usage hours (number)

	Returns estimated monthly kWh (float).
	"""
	try:
		w = float(watt)
		q = float(quantity)
		hrs = float(usage_hours)
	except (TypeError, ValueError):
		raise TypeError("watt, quantity and usage_hours must be numbers")

	# Convert watts to kW, multiply by quantity and hours, then by 30 days
	daily_kwh = (w / 1000.0) * q * hrs
	monthly_kwh = daily_kwh * 30
	return monthly_kwh

