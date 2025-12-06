def calculate_bill(total_kwh):
    """Calculate a simple bill from total kWh.

    This uses a flat rate (ETB/kWh). Adjust rates as needed.
    """
    rate_per_kwh = 1.5  # ETB per kWh — change to match local tariffs
    return total_kwh * rate_per_kwh
