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

if len(videos) > 0:
    print("Calculating total duration...")

    total_duration = 0

    for video_file in videos:
        # Read metadata for the current video file
        metadata = ffmpeg.probe(video_file)

        # Extract the duration of the video
        video_time = float(metadata['streams'][0]['duration'])

        # Add the duration to the total duration
        total_duration += video_time

    # Print the total duration
    print(f"Total Duration: {int(total_duration // 3600)} hours {int((total_duration % 3600) // 60)} minutes {int(total_duration % 60)} seconds")
else:
    print("No video files found.")
