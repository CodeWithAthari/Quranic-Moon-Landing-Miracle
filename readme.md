# Moon Landing Year in the Quran

This Python script calculates the year of the moon landing according to the Quran.

## How it works

The script reads a JSON file named `chapters.json` which contains information about the chapters of the Quran. Each chapter in the JSON file has an `id`, `verses_count`, and `name_simple`.

The script then iterates over each chapter. If the `id` of the chapter is 54 or more, it starts counting the number of verses. The number 54 is significant because it corresponds to Surah Al-Qamar, which is associated with the moon.

The total number of verses from Surah Al-Qamar onwards is then calculated. This total is then decremented by 1 to get the offset or the steps required to go to the 6236th verse (which is the total number of verses in the Quran).

The script then prints the calculated year of the moon landing according to the Quran.

## Usage

To run the script, simply execute the `main.py` file:

```bash
python main.py
```
Make sure you have the `chapters.json` file in the same directory as the script.

### Output
```bash
...
---------------------------------------------
---------------------------------------------
---------------------------------------------
The year of the moon landing in the Quran is: 1389 # hijri date
...
```

## Requirements
- Python 3
- JSON file named `chapters.json` in the same directory as the script
