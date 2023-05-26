import requests
import pygame
import os

def download_mp3(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    repository_url = "https://github.com/Ekementrievich/pythoncode.git"  # Replace with the actual repository URL
    mp3_files = ["video1.mp3", "video2.mp3"]  # Replace with the actual MP3 file names

    for mp3_file in mp3_files:
        mp3_url = repository_url + mp3_file
        destination = mp3_file

        # Download the MP3 file
        print("Downloading:", mp3_file)
        download_mp3(mp3_url, destination)

        # Play the MP3 file
        print("Playing:", mp3_file)
        play_mp3(destination)

        # Wait for the file to finish playing
        pygame.time.wait(5000)

        # Clean up the downloaded file
        os.remove(destination)

if __name__ == "__main__":
    main()
