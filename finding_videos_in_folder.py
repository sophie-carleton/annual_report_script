import os

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
