print("=== Welcome to the Custom Ride Builder ===")
vehicle = input("Choose a vechile (Bike/Car): ")
if vehicle.lower() == "bike":
    bike = input ("Choose a bike (Mountain/Road): ")
    if bike.lower() == "mountain":
        print("Model: Mountain Bike")
        print("Top speed: 25 mph")
        print("Best Use: off-road trails")
    else:
        print("Model: Road bike")
        print("Top speed: 35 mph")
        print("Best Use: City roads and racing")
elif vehicle.lower() == "car":
    car = input ("Choose a car (SUV/Sedan):")
    if car.lower() == "sedan":
        print("Model: Sedan")
        print("Seats: 5")
        print("Best use: Daliy")
    else:
        print("Model: SUV")
        print("Seats: 7")
        print("Best use: Family trip")
else:
    print("Invalid vechile choice")