import logging
import requests
from dconfig import config
import mysql.connector
from datetime import datetime



#Methods: blocks of code that cannot run by themselves
def fetch_playlist_items(google_api_key, youtube_playlist_id):
    url = f"https://www.googleapis.com/youtube/v3/playlistItems"
    items = []
    params = {
        "part": "contentDetails",
        "playlistId": youtube_playlist_id,
        "key": google_api_key
    }

    while True:
        response = requests.get(url, params=params).json()
        items.extend(response.get("items", []))
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
        params["pageToken"] = next_page_token

    return items

# Function to fetch video details
def fetch_videos(google_api_key, youtube_playlist_id):
    url = f"https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,statistics,liveStreamingDetails",
        "id": youtube_playlist_id,
        "key": google_api_key
    }
    response = requests.get(url, params=params).json()
    items = response.get("items", [])
    return items

# Function to summarize video details
def summarize_video(video):
    return {
        "video_id": video["id"],
        "title": video["snippet"]["title"],
        "date_published": video["snippet"]["publishedAt"],
        "views": int(video["statistics"].get("viewCount", 0)),
        "likes": int(video["statistics"].get("likeCount", 0)),
        "comments": int(video["statistics"].get("commentCount", 0)),
        "pull_date": datetime.now().strftime("%Y-%m-%d")
    }

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    logging.info("START")

    google_api_key = config["google_api_key"]
    youtube_playlist_id = config["youtube_playlist_id"]

    try:
        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*************",
            database="youtube_data"
        )
        mycursor = mydb.cursor()

        # Create table if it doesn't exist
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS videos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                video_id VARCHAR(255),
                title VARCHAR(255),
                date_published VARCHAR(255),
                views INT,
                likes INT,
                comments INT,
                pull_date VARCHAR(255)
            )
        """)

        # Fetch playlist items once
        playlist_items = fetch_playlist_items(google_api_key, youtube_playlist_id)
        
        # Iterate through playlist items once
        for video_item in playlist_items:
            video_id = video_item["contentDetails"]["videoId"]

            # Fetch video details
            videos = fetch_videos(google_api_key, video_id)
            for video in videos:
                # Summarize video data
                video_summary = summarize_video(video)

                # Insert data into MySQL table
                sql = """
                    INSERT INTO videos (video_id, title, date_published, views, likes, comments, pull_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                val = (
                    video_summary['video_id'], video_summary['title'], video_summary['date_published'],
                    video_summary['views'], video_summary['likes'], video_summary['comments'], video_summary['pull_date']
                )
                mycursor.execute(sql, val)

                mydb.commit()

                logging.info("GOT %s", video_summary)

    except mysql.connector.Error as err:
        logging.error("Error: %s", err)
    except Exception as e:
        logging.error("Unexpected error: %s", e)
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
        logging.info("END")

if __name__ == "__main__":
    main()



