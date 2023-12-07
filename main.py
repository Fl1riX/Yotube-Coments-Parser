from googleapiclient.discovery import build

api_key = "yotube_api_key"
video_id = "Video_id"

def get_all_video_comments(api_key, video_id, start_page_token=None):
    youtube = build('youtube', 'v3', developerKey=api_key)

    nextPageToken = start_page_token
    all_comments = []

    while True:
        comments = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            pageToken=nextPageToken,
            maxResults=100,  
            order="time"     
        ).execute()

        all_comments.extend([comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in comments['items']])

        nextPageToken = comments.get('nextPageToken')

        if not nextPageToken:
            break

    return all_comments, nextPageToken

if __name__ == "__main__":
    api_key = api_key
    video_id = video_id

    start_page_token = None 

    comments, next_page_token = get_all_video_comments(api_key, video_id, start_page_token)

    with open("yotube_comments.txt", "a", encoding="utf-8", errors="ignore") as file:
        for i, comment in enumerate(comments, start=1):
            file.write(f"Comment {i}: {comment}\n")

    print(f"Следующий nextPageToken: {next_page_token}")

