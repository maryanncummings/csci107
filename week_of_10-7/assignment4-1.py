# Taken from LyricFind.com
# Lyrics by andrew taggart, chris martin,
# guy berryman, johnny buckland, will champion
# Sung by Coldplay and Chainsmokers
def repeats(str, num):
    for i in range(num):
        print(str)

def first_two(str):
    print(str + "been reading books of old")
    print("The legends and the myths")

def first_not_repeated():
    print("Achilles and his gold\nHercules and his gifts")
    print("Spiderman's control\nAnd Batman with his fists")
    print("And clearly I don't see myself upon that list")

def refrain(str, kiss_or_miss, str2):
    str1="Oh, I want something just like this"
    print(str + "'Where'd you wanna go?'\nHow much you \
wanna risk?\nI'm not looking for somebody\nWith some \
superhuman gifts\nSome superhero\nSome fairytale bliss\nJust \
something I can turn to\nSomebody I can " + kiss_or_miss + "\n" +
"I want something just like this\n" + str2 + "want something \
just like this")
    repeats(str1, 2)

def second_not_repeated():
    print("The testaments they told\nThe moon and its eclipse")
    print("And Superman unrolls\nA suit before he lifts")
    print("But I'm not the kind of person that it fits")    
    
def main():
    first_two("I've ")
    first_not_repeated()
    refrain("But she said,", "kiss", "Oh, I ")
    first_two("Oh, I've ")
    second_not_repeated()
    refrain("She said ", "miss", "I ")
    refrain("", "kiss", "Oh, I ")

main()
