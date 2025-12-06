
customers = []


def register_customer(name, customer_id):
	"""Register a customer if the `customer_id` is not already taken."""
	# Check if customer_id already exists
	for c in customers:
		if c["customer_id"] == customer_id:
			print(f"Error: Customer ID '{customer_id}' is already taken!")
			return

	customer = {"name": str(name), "customer_id": str(customer_id)}
	customers.append(customer)
	print("Customer registered successfully!")


def list_customers():
	"""Print registered customers to stdout."""
	if not customers:
		print("No customers registered.")
		return
	print("\nRegistered Customers:")
	for c in customers:
		print(f"Name: {c['name']}, Customer ID: {c['customer_id']}")


def get_customers():
	"""Return a copy of the customers list for programmatic use."""
	return list(customers)


if __name__ == "__main__":
	# Self-test: running this module should register and list demo customers
	print("Running customer service self-test...")
	register_customer("Alice", "C001")
	register_customer("Bob", "C002")
	# Attempt duplicate
	register_customer("Eve", "C001")
	list_customers()
