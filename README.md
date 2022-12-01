# All-Vietnamese-syllables-2022
All Vietnamese syllables 2022: 20190
1. Code based on the blog: https://www.hieuthi.com/blog/2017/03/21/all-vietnamese-syllables.html
2. The structure of a syllable

![image](https://user-images.githubusercontent.com/36023580/204964672-efee3da2-d7df-41be-8ae6-1a49cb3c4835.png)

Figure 1: One-syllable structure of Vietnamese
• Onset of 27 letters (one letter, two letters, pairs)
• Tone includes six tones (equal, sharp, profound, question, fall, heavy)
• Rime: to generate rimes, the author gives the following table

![image](https://user-images.githubusercontent.com/36023580/204964787-8692582d-f671-4ba1-9fc9-92a6e63a81a4.png)

Figure 2: Rimes architecture table with equal tone (blank)
◦ Blue areas are rimes that can be combined with six tones, red can combine with sharp and heavy accents (grave, dot), and yellow areas can combine with six tones (but no standing onset). head)
3. Prepare
• File meta_data.json (contains information about tones, rimes, notation, and onset)
• File rimes_construction_table.ods (excel, contains information similar to Figure 2, but encoded with the values ​​0, 1, 2, 3 corresponding to the information in the meta_data.json file)
4. Code explanation
- Looking at Figure 2, we see that each rime will consist of 2 components, called prefix and suffix (prefixes and suffix).
- Step 1: Create the rimes first, based on the tone field in the file meta_data.json and the color area that the rime belongs to (blue, red, or yellow) to determine the correct tone
- Step 2: After having rhyme, we will generate a syllable by combining it with the onset (except for the yellow zone because the rimes in this region are not associated with the onset)
* Code for each cell in the rimes construction table, from top to bottom and from left to right
