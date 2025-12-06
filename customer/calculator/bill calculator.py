def calculate_bill(total_consumptio

    # Step 1: Energy cost based on tariff
    if total_consumption <= 50:
        energy_cost = total_consumption * 0.273
        service_charge = 10
    elif total_consumption <= 100:
        energy_cost = total_consumption * 0.767
        service_charge = 42
    elif total_consumption <= 200:
        energy_cost = total_consumption * 1.625
        service_charge = 42
    elif total_consumption <= 300:
        energy_cost = total_consumption * 2
        service_charge = 42
    elif total_consumption <= 400:
        energy_cost = total_consumption * 2.2
        service_charge = 42
    elif total_consumption <= 500:
        energy_cost = total_consumption * 2.405
        service_charge = 42
    else:
        energy_cost = total_consumption * 2.481
        service_charge = 42

    # Step 2: Total bill = energy cost + service charge
    total_bill = energy_cost + service_charge
    return total_bill

