from customers.customer_service import register_customer, list_customers
from appliances.appliance_service import register_appliance, list_appliances, appliances
from calculators.consumption_calculator import calculate_monthly_kwh
from calculators.bill_calculator import calculate_bill


def main_menu():
	while True:
		print("\n=== Electric Consumption & Bill Calculator ===")
		print("1. Customer")
		print("2. Appliance")
		print("3. Consumption and Bill")
		print("4. Exit")
		choice = input("Enter choice: ")
		if choice == "1":
			name = input("Customer name: ")
			customer_id = input("Customer ID: ")
			register_customer(name, customer_id)
		elif choice == "2":
			aname = input("Appliance name: ")
			try:
				watt = int(input("Wattage: "))
				qty = int(input("Quantity: "))
				hrs = float(input("Daily usage hours: "))
			except ValueError:
				print("Invalid numeric input. Try again.")
				continue
			register_appliance(aname, watt, qty, hrs)
		elif choice == "3":
			if not appliances:
				print("No appliances registered!")
				continue

			total_kwh = 0
			for a in appliances:
				total_kwh += calculate_monthly_kwh(a["watt"], a["quantity"], a["usage_hours"])

			print(f"\nTotal Monthly Consumption: {total_kwh:.2f} kWh")
			bill = calculate_bill(total_kwh)
			print(f"Total Monthly Payable Bill: {bill:.2f} ETB")

		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Invalid choice. Try again")
if __name__ == "__main__":
	main_menu()