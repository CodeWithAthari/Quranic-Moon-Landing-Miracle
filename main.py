import json


with open("chapters.json","r") as f:
    data = json.loads(f.read())
    chapters = data['chapters']
    total_verses = 0
    for chapter in chapters:
        id = chapter['id']
        verses_count = chapter['verses_count']
        name_simple = chapter['name_simple']
        print(f"Chapter {id} has {verses_count} verses and its name is {name_simple}")
        if id >= 54:
            # 54 is the Surah Al-Qamar, the moon
            # started counting verses from the moon chapter & onwards
            total_verses = total_verses + verses_count
    
    # if we subtract 5 from 10. The result is 5 but the offset is 4
    # i.e 10-5 = (6,7,8,9)
    # same way we are subtracting 1 from the total verses to get offset 
    # or steps required to go to the 6236th (total verses in the Quran) verse
    verses_offset = total_verses-1    
    print(f"The year of the moon landing in the Quran is {verses_offset}")