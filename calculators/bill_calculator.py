

def calculate_bill(total_consumption):
	"""Calculate the payable bill (energy cost + service charge) from kWh.

	Accepts numeric input for `total_consumption` (kWh). Raises TypeError
	if the input cannot be converted to a number.
	"""
	try:
		total = float(total_consumption)
	except (TypeError, ValueError):
		raise TypeError("total_consumption must be a number")

	# Determine rate and service charge by consumption band
    if total <= 50:
        rate = 0.273
        service_charge = 10
    elif total <= 100:
        rate = 0.767
        service_charge = 42
    elif total <= 200:
        rate = 1.625
        service_charge = 42
    elif total <= 300:
        rate = 2.0
        service_charge = 42
    elif total <= 400:
        rate = 2.2
        service_charge = 42
    elif total <= 500:
        rate = 2.405
        service_charge = 42
    else:
        rate = 2.481
        service_charge = 42

	energy_cost = total * rate
	return energy_cost + service_charge


if __name__ == "__main__":
    # Simple self-test: show bills for example consumptions
    examples = [30, 75, 150, 250, 350, 450, 600]
    print("Bill calculator self-test:")
    for kwh in examples:
        bill = calculate_bill(kwh)
        print(f"{kwh} kWh -> {bill:.2f} ETB")


if __name__ == "__main__":
	# Quick manual test
	samples = [30, 75, 150, 250, 350, 450, 600]
	for s in samples:
		print(f"{s} kWh -> {calculate_bill(s):.2f} ETB")