# Youtube data streamer is real time data streaming application.

# Table of contents
-[Project Overview](#project-overview)
-[Data Sources](#data-sources)
-[Tools](#tools)
-[Key Questions](#key-questions)
- 

### Project Overview

This data analysis project aims to provide real time data such as views, likes, comments and dislikes. the data is then processed into a database using MySQL in order to be used in any BI Tool.

### Data Sources

Youtube data playlist, you can use any playlist as long as you provide a API Key from Youtube Developers and the playlist link.

### Tools

-Python -Application Code
-MySQL -Data Analysis
-PowerBI -Creating Reports

### Key Questions (relating to streamers fuwamoco twin sibling vtubers from Cover Corp.'s HOLOLIVE)

-What is the difference in total views between Fuwamoco streamers when they are streaming the same game but from different perspectives?

-How many views are accumulated daily for a VOD featuring the streamers together?

-Is there a difference in viewership when Fuwamoco collaborates with English branches compared to Japanese branches?

-What is the difference in total likes between different POV streams of Fuwamoco?

-How do the view counts differ when Fuwawa streams alone compared to when she streams together with her sister?

### Results/Findings

-When Fuwamoco streams the same game from different perspectives, Fuwawa experiences a notable dip in viewership compared to Mococo. Fuwawa's VOD viewership tends to stagnate after a certain point, while Mococo's viewership shows slight growth.

-VOD's featuring Fuwamoco streaming together exhibit a consistent growth in views over time.

-Fuwamoco's viewership significantly increases during collaborations with the Japanese branch, such as the Marine collaboration, which garnered 264k viewers. This surge is likely due to their fluency in Japanese, setting them apart from most of the English branch. In contrast collaborations with the English branch see a dip in viewership, with a notable example being the 79k views on a "content warning" stream compared to the 194k views during an off-collab event.

-There is a significant difference in total likes between different POV streams, with Mococo receiving 10k likes and Fuwawa receiving 7k likes. Streaming the same game separately does not appear to be beneficial, as it splits the viewership.

-Fuwawa tends to perform better in viewership when streaming solo, especially with games tailored to her tastes. For instance, her "Hitman" stream received 187k views while a joint stream with her sister on a popular game like "Suika Game" garnered 113k views.

### Recommendations

-Instead of splitting perspectives, Fuwamoco could consider streaming together more often to consolidate their viewership. This approach can prevent viewership fragmentation and help build a more solid audience.

-Focus on collaborations with high-profile and popular members, especially from the Japanese branch, to maximize viewership and subscriber growth. Fuwamoco also focuses on bilingual streams which should be continued as well.

-Encourage Fuwawa to continue streaming games tailored to her tastes, as these tend to attract higher viewership. Identifying and focusing on niche content that resonates with her audience can be beneficial.

### Code Instructions

-If any of the imports do not work, -pip install (add the import without the parenthesis in the terminal)

-You will need to get an API key from youtube after following the instructions here: https://developers.google.com/youtube/v3/getting-started 

-You will need a youtube account to create a playlist, add videos to it, copy and paste the playlist link.

-Add both API Key and Playlist Link into the dconfig.py file.

-In MySQL you will need to add a new schema, call it youtube_data.

-Add your credentials of MySQL in line 61-67 of main.py.

-Run application you will see data populate in the terminal and database.

-select mysql in any BI tools, its been tested in tableau and powerBI.
