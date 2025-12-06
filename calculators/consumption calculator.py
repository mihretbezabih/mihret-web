def calculate_monthly_kwh(watt, quantity, usage_hours):
    # kW = watt/1000
    daily_kwh = (watt / 1000) * quantity * usage_hours
    monthly_kwh = daily_kwh * 30
    return monthly_kwh