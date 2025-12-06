def calculate_monthly_kwh(watt, quantity, usage_hours):
    """Calculate estimated monthly kWh for the appliance(s).

    Formula: kWh = (watt * quantity * hours_per_day * 30) / 1000
    """
    daily_wh = watt * quantity * usage_hours
    monthly_kwh = daily_wh * 30 / 1000.0
    return monthly_kwh
