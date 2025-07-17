emoji_map = {
    "love": "❤️", 
    "happy": "😊", 
    "sad": "😢", 
    "angry": "😠",
    "code": "💻",
    "coffee": "☕",
    "party": "🎉",
    "star": "⭐",
    "fire": "🔥",
}

message = input("Enter your message: ")

updated_words = []

for word in message.split():
    clean_word = word.lower().strip(".,!?;:")  # Remove punctuation
    emoji = emoji_map.get(clean_word,"")
    if emoji:
        updated_words.append(f"{word.upper()}{emoji}")
    else:
        updated_words.append(word.upper())

updated_message = " ".join(updated_words)
print("\n word is \n")
print(updated_message)