import requests
import pygame
import os

def download_mp4(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def play_mp4(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load("C:\Users\st6109064\Desktop")
    pygame.mixer.music.play()

def main():
    repository_url = "https://github.com/Ekementrievich/pythoncode.git"  # Replace with the actual repository URL
    mp4_files = ["video1.mp4", "video3.mp4",]  # Replace with the actual MP4 file names

    for mp4_file in mp4_files:
        mp4_url = repository_url + mp4_file
        destination = mp4_file

        # Download the MP4 file
        print("Downloading:", mp4_file)
        download_mp4(mp4_url, destination)

        # Play the MP4 file
        print("Playing:", mp4_file)
        play_mp4(destination)

        # Wait for the file to finish playing
        pygame.event.wait()

        # Clean up the downloaded file
        os.remove(destination)

if __name__ == "__main__":
    main()
