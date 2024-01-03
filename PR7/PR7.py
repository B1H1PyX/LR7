def calculate_total_cost(cars_dict):
    total_cost = 0
    for car in cars_dict.values():
        if car["power"] > 100:
            total_cost += car["cost"]
    return total_cost
def main():
    cars_dict = {}
    for i in range(1, 11):
        power = float(input(f"Enter power of car {i} (in horsepower): "))
        cost = float(input(f"Enter cost of car {i} (in dollars): "))
        cars_dict[i] = {"power": power, "cost": cost}
    total_cost_above_100_hp = calculate_total_cost(cars_dict)
    print("Total cost of cars with power above 100 horsepower:", total_cost_above_100_hp)
if __name__ == "__main__":
    main()