import random

print(f"Welcome to Kumari Anjali's Fortune Teller (21je0495) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

# Version 1.1 - Added 'stressed' mood and multiple fortunes per mood
fortunes = {
    "happy": [
        f"Great things await you, Kumari Anjali! Keep smiling.",
        "Your positive energy will bring wonderful opportunities today!",
        "Your happiness is contagious - spread it far and wide!"
    ],
    "sad": [
        "The clouds will soon part. Brighter days are ahead!",
        "Every setback is setting you up for a comeback.",
        "It's okay to feel down sometimes - tomorrow will be better."
    ],
    "neutral": [
        "Embrace the unexpected. Good fortune may find you today.",
        "Balance is the key to harmony in your life.",
        "Stay present and mindful - good things are developing."
    ],
    "stressed": [
        "Take a deep breath. This challenge will make you stronger.",
        "Step back and prioritize - you've got this!",
        "Remember to care for yourself as you handle your responsibilities."
    ]
}

if mood in fortunes:
    # Choose a random fortune for the given mood
    chosen_fortune = random.choice(fortunes[mood])
    print(f"✨ Your fortune: {chosen_fortune} ✨")
else:
    print("Sorry, I don't understand that mood. Try happy, sad, neutral, or stressed.")
