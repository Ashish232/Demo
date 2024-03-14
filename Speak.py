import os
import pygame
import re

def Speak(data:str):
    
    #pygame.init()
    command = f'edge-tts --voice "en-CA-LiamNeural" --pitch=+5Hz --rate=+15% -t "{data}" --write-media "data.mp3"'
    while 1:
        try:
            os.system(command)
            pygame.mixer.init()
            pygame.mixer.music.load("data.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            return
        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()

if __name__=="__main__":
    Speak("unrecognized arguments: send me the news headlines and I'll handle the rest.")