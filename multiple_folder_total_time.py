import os
import sys
import ffmpeg

def find_video_files(folder):
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']  # Add more extensions as needed
    video_files = []

    for root, dirs, files in os.walk(folder):
        if not any(folder.endswith('.fcpbundle') or folder.endswith('.fcpxmld') for folder in root.split(os.sep)):
            for file in files:
                if any(file.endswith(ext) for ext in video_extensions):
                    video_files.append(os.path.join(root, file))

    return video_files


# User input for folder paths
print("Enter the folder paths to search for video files (one per line).")
print("Press Enter on an empty line to finish.")
folder_paths = []

while True:
    folder_path = input()
    if not folder_path:
        break
    folder_paths.append(folder_path.strip())

total_duration = 0

for folder_path in folder_paths:
    videos = find_video_files(folder_path)

    if len(videos) > 0:
        print(f"Calculating total duration for {folder_path}...")

        for video_file in videos:

            # Read metadata for the current video file
            metadata = ffmpeg.probe(video_file)

            # Extract the duration of the video
            video_time = float(metadata['streams'][0]['duration'])

            # Add the duration to the total duration
            total_duration += video_time

    else:
        print(f"No video files found in {folder_path}.")

# Print the total duration
print(f"Total Duration: {int(total_duration // 3600)} hours {int((total_duration % 3600) // 60)} minutes {int(total_duration % 60)} seconds")
