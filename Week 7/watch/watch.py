import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    # Convert s subdomain to "https://youtu.be/"
    s = re.sub(r"^<iframe (?:width=\"\d+\" height=\"\d+\" )?src=\"https?://(?:www\.)?youtube.com/embed/",
                "https://youtu.be/", s, re.IGNORECASE)

    # Remove HTML attributes
    s = re.sub(r"\"( title=\D+)?( frameborder=\"\d+)?(\D+)?(\w+)?></iframe>$", "", s, re.IGNORECASE)

    # Return the correct link
    if s:= re.search(r"(https://youtu\.be/.+)", s):
        return s.group(1)
    else:
        return None


if __name__ == "__main__":
    main()