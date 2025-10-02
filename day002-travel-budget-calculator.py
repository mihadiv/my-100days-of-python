print("Welcome to the Travel Budget Calculator!")

budget = float(input("What's your total travel budget? $"))
days = int(input("How many days are you traveling? "))
savings_percent = int(input("What percentage do you want to save for extras? "))

daily_budget = (budget * (1 - savings_percent / 100)) / days
daily_budget = round(daily_budget, 2)

print(f"You can spend ${daily_budget} per day for your trip!")
