import os
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id_from_url(url):
    query = urlparse(url)
    if query.hostname == 'www.youtube.com':
        if 'v' in query.query:
            video_id = parse_qs(query.query)['v'][0]
            return video_id
    elif query.hostname == 'youtu.be':
        video_id = query.path[1:]
        return video_id
    return None

def get_all_comments(youtube, video_id):
    all_comments = []

    # Get video comments using pagination
    next_page_token = None
    while True:
        comments_response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,  # Adjust as needed
            pageToken=next_page_token
        ).execute()

        comments = [comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in comments_response.get('items', [])]
        all_comments.extend(comments)

        next_page_token = comments_response.get('nextPageToken')
        if not next_page_token:
            break

    return all_comments

def get_youtube_video_data(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get video details
    video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
    video_data = video_response['items'][0]

    # Extract likes and comments count
    likes_count = video_data['statistics']['likeCount']
    comments_count = video_data['statistics']['commentCount']

    # Get all video comments
    all_comments = get_all_comments(youtube, video_id)

    return {
        'likes': likes_count,
        'comments_count': comments_count,
        'comments': all_comments,
    }

def main():
    # Replace 'YOUR_API_KEY' with your actual YouTube Data API key
    api_key = 'AIzaSyCMEFGCfoj0oNtiZoaXXzI87hywf0loKkk'
    
    # Take input from the user for the YouTube video link
    video_link = input("Enter the YouTube video link: ")
    
    # Extract video ID from the link
    video_id = extract_video_id_from_url(video_link)
    
    if video_id:
        # Get video data
        video_data = get_youtube_video_data(api_key, video_id)

        # Print video information
        print(f"Likes: {video_data['likes']}")
        print(f"Comments Count: {video_data['comments_count']}")
        
        if video_data['comments']:
            print("\nAll Comments:")
            for i, comment in enumerate(video_data['comments'], start=1):
                print(f"{i}. {comment}")

            # Save comments to a separate text file
            with open('comments.txt', 'w', encoding='utf-8') as comment_file:
                for comment in video_data['comments']:
                    comment_file.write(f"{comment}\n")

            print("Comments have been saved to comments.txt")

        # Get and save video transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        with open('transcript.txt', 'w', encoding='utf-8') as file:
            for entry in transcript:
                file.write(f"{entry['start']} - {entry['start'] + entry['duration']}: {entry['text']}\n")

        print("Transcript has been saved to transcript.txt")
    else:
        print("Invalid YouTube video link.")

if __name__ == "__main__":
    main()
