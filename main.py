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
            total_verses = total_verses + verses_count
    
    verses_offset = total_verses-1    
    print(f"The year of the moon landing in the Quran is {verses_offset}")