customers = []

def register_customer(name, customer_id):
    customer = {"name": name, "id": customer_id}
    customers.append(customer)
    print(f"Customer registered: {name} (ID: {customer_id})")


def list_customers():
    return customers
