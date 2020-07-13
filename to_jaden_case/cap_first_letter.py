# Submitted


# Code
def to_jaden_case(string):
    quote = string.split(" ")
    cap_quote = ""
    for word in quote:
        cap_word = word.capitalize()
        cap_quote = cap_quote + " " + cap_word
    return cap_quote.strip()


if __name__ == "__main__":

    # Input
    jaden = "Hello friends from twitter"
    jaden = "HELLO, FRIENDS FR&M TWITTER!"

    # Output
    print(to_jaden_case(jaden))
