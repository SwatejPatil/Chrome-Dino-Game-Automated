import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    #birds
    for i in range(190, 200):
        for j in range(350, 405):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(240, 290):
        for j in range(470, 490):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    
    time.sleep(2)


    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        

      
      