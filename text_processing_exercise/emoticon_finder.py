text = input()
emoticons = [text[i:i+2] for i in range(len(text) - 1) if text[i] == ":"]
print("\n".join(emoticons))
