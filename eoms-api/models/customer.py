class Customer:
    id = 0
    customer_reference = ""
    customer_name = ""
    customer_email_address = ""
    updated_on = None
    created_on = None

def list_customers(db_connection):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM customer LIMIT 20")
    records = cur.fetchall()

    customers = []

    for record in records:
        customer = Customer()
        values = list(record)

        # TODO: Do this dynamically
        customer.id = values[0]
        customer.customer_reference = values[1]
        customer.customer_name = values[2]
        customer.customer_email_address = values[3]
        customer.updated_on = values[4]
        customer.created_on = values[5]

        customers.append(customer)

    return customers
