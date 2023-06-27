def convert(emoji):
    emoji = emoji.replace(":)","\U0001F642").replace(":(","\U0001F641")
    return emoji

def main():
    phrase = input()
    phrase = convert(phrase)
    print(phrase)

main()