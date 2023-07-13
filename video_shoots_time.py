import os
import sys
import ffmpeg

def find_video_files(folder):
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']  # Add more extensions as needed
    video_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if any(file.endswith(ext) for ext in video_extensions):
                video_files.append(os.path.join(root, file))

    return video_files

# User input for folder path
folder_to_search = input("Enter the folder path to search for video files: ")

videos = find_video_files(folder_to_search)

print("Video files found:")
for video in videos:
    print(video)

if len(videos) > 0:
    print("Metadata for each video found:")

    for video_file in videos:
        # Read metadata for the current video file
        metadata = ffmpeg.probe(video_file)

        # Extract the duration of the video
        video_time = float(metadata['streams'][0]['duration'])

        # Print the video file path and its duration
        print(f"Video: {video_file}")
        print(f"Duration: {int(video_time // 60)} minutes {int(video_time % 60)} seconds")
        print()
else:
    print("No video files found.")
