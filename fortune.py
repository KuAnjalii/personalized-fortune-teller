print(f" Welcome to Kumari Anjali's Fortune Teller (21JE0495) ")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": f"Great things await you, Kumari Anjali! Keep smiling.",
    "sad": "Hey what happend don't worry Kumari Anjali, everything will be fine just try to remember some old good memories which can make you smile, and be happy.",
    "neutral": "Stay calm and carry on.",
    "stressed": "Take a deep breath and relax, have some rest. Everything will be fine."
}

if mood in fortunes:
    print(f" Your fortune: {fortunes[mood]} ")
else:
    print("Sorry, I don't have a fortune for that mood.")
