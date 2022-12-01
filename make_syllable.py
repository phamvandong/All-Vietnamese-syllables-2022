import json
from typing import List

import pandas


def load_json(path: str) -> dict:
    with open(path, encoding="utf8") as fp:
        data = json.load(fp)
    return data

def write_txt(
        data: List[str],
        path: str
    ) -> None:

    with open(path, mode='w', encoding='utf8') as fp:
        fp.writelines(data)

# load data
meta_data = load_json("meta_data.json")
rimes_construction_table = pandas.read_excel("rimes_construction_table.ods", sheet_name= "Sheet1")

onset_list = meta_data["onset"].split(",")

# rimes construction
syllable_list = list()

for index, row in rimes_construction_table.iterrows():
    row = row.to_list()
    values = row[1:]
    final_consonant = row[0]
    
    for _id_, value in enumerate(values):
        value = str(int(value))
        rimes_region = meta_data["notation"][value]
        
        if not rimes_region: continue
        
        tone_list = meta_data["rimes"][rimes_region].split(",")
        
        # make rimes
        for tone in tone_list:
            prefix_list = meta_data["tone"][tone].strip().split(",")
            prefix = prefix_list[_id_]

            if final_consonant == "nothing":
                rime = prefix
            else:
                rime = f"{prefix}{final_consonant}"
            
            if rimes_region != "yellow":
                syllable_list.append(f"{rime}\n")

                for onset in onset_list:
                    syllable = f"{onset}{rime}\n"
                    syllable_list.append(syllable)
                    
            else:
                syllable = f"{rime}\n"
                syllable_list.append(syllable)


syllable_list= sorted(syllable_list)
write_txt(syllable_list, "syllables.txt")

# sysllabel contrucstion

