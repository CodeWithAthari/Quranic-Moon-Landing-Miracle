import json

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

lines = """---------------------------------------------
---------------------------------------------
---------------------------------------------"""

with open("chapters.json","r") as f:
    data = json.loads(f.read())
    chapters = data['chapters']
    total_verses = 0
    print("Calculating the Moon Landing Year in the Quran")
    for chapter in chapters:
        id = chapter['id']
        verses_count = chapter['verses_count']
        name_simple = chapter['name_simple']
        if id >= 54:
            print(f"Chapter {id} has {verses_count} verses and its name is {name_simple}")
            # 54 is the Surah Al-Qamar, the moon
            # started counting verses from the moon chapter & onwards
            total_verses = total_verses + verses_count
    
    print(lines)
    # if we subtract 5 from 10. The result is 5 but the offset is 4
    # i.e 10-5 = (6,7,8,9)
    # same way we are subtracting 1 from the total verses to get offset 
    # or steps required to go to the 6236th (total verses in the Quran) verse
    verses_offset = total_verses-1    
    print(f"The year of the moon landing in the Quran is: {color.BOLD}{verses_offset}{color.END}")
    
    message = "For more information read following article:\nhttps://www.answeringislamicskeptics.com/moon-landing.html"
    print(message)
    print(lines)