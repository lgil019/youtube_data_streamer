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

### Key Questions

-What was number of views gained each day?
-Comparison of comment engagement between similar videos?
-Average amount of likes a day?

### Results/Findings

### Code Instructions

-If any of the imports do not work, -pip install *add the import without the stars in the terminal*
-You will need to get an API key from youtube after following the instructions here: https://developers.google.com/youtube/v3/getting-started 
-You will need a youtube account to create a playlist, add videos to it, copy and paste the playlist link.
-Add both API Key and Playlist Link into the dconfig.py file.
-In MySQL you will need to add a new schema, call it youtube_data
-Add your credentials of MySQL in line 61-67 of main.py
-Run application you will see data populate in the terminal and database.
