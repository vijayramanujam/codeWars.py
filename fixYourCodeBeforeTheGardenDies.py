def rain_amount(rain_amount):
    if (rain_amount < 40):
        return f"You need to give your plant {40 - rain_amount }mm of water"
    return "Your plant has had more than enough water for today!"
