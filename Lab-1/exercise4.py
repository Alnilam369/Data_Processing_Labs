name = input("Passenger name: ")
destination = input("Destination: ")
tickets = int(input("Enter number of tickets: "))
passenger_type = input("Enter passenger type (adult/child/student/senior): ")

if destination.lower() == "dhaka":
    fare = 500
elif destination.lower() == "barisal":
    fare = 800
elif destination.lower() == "sylhet":
    fare = 700
else:
    fare = 600

if passenger_type.lower() == "child":
    discount = 0.50
elif passenger_type.lower() == "student":
    discount = 0.20
elif passenger_type.lower() == "senior":
    discount = 0.30
else:
    discount = 0

total = fare * tickets
discount_amount = total * discount
final_fare = total - discount_amount

print("Passenger:", name, "Destination:", destination, "Tickets:", tickets,
       "Passenger Type:", passenger_type, "Total Fare:", total,
        "Discount:", discount_amount, "Final Fare:", final_fare)
