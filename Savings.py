print("Your Saving Calculator")
user_input = input("How much do you earn per hr?")
hours_per_day = 8

daily_savings = int(user_input) * hours_per_day
print("This is your daily savings", daily_savings)

weekly_savings = int(user_input) *  5
print("This is your weekly savings", weekly_savings)

monthly_savings = int(user_input) * 4
print("This is your monthly savings", monthly_savings)
