import pyautogui
import subprocess
import time
import cv2 as cv
import os
import numpy as np


pyautogui.PAUSE = 2.5

# OPEN PDF IN FULL SCREEN
def openPDF(pdfFile):
    openPDF_s = time.time()
    edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
    command = [edge_path, '--kiosk', pdfFile]
    subprocess.Popen(command)
    x=1747
    y=135
    pyautogui.moveTo(x,y)
    pyautogui.click()
    time.sleep(5) #remove 
    openPDF_f =time.time()
    print('Open PDF time: ', (openPDF_f - openPDF_s))

# GET PNG
def getPNG(filename):
    getPNG_s= time.time()

    # NOW CREATE THE PNG VERSION FOR COMPUTER VISION TASKS
    screenshot = pyautogui.screenshot()
    screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

    PNGpath = 'C:/Users/mcevoye3799/Documents/Programming/Computer Vision/PNGS/'
    fullPath = PNGpath + (filename.replace('.pdf','.png'))
    print('full path ', fullPath)
    cv.imwrite(fullPath, screenshot) 
    pyautogui.hotkey('Esc')

    getPNG_f = time.time()
    print('getPNG time: ', (getPNG_f-getPNG_s))

    return fullPath
   
def main():

    directory_path= 'C:/Users/mcevoye3799/Documents/Programming/Computer Vision/PDF_drawings'
    index = 0
    total = len(directory_path)

    for filename in os.listdir(directory_path):
       
        pdfFile = os.path.join(directory_path, filename) 
        openPDF(pdfFile)
        getPNG(filename)

        # CLOSE PDF
        pyautogui.hotkey('Esc')
        pyautogui.hotkey('ctrl', 'w')
        print ('PDF ', index, '/', total)
        index = index + 1 
    


main()