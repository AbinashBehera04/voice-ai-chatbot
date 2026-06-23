import webbrowser
import os
import ctypes
import psutil
import pyautogui
import cv2

def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_github():
    webbrowser.open("https://github.com")


def shutdown_pc():
    os.system("shutdown /s /t 60")


def restart_pc():
    os.system("shutdown /r /t 60")


def lock_pc():
    ctypes.windll.user32.LockWorkStation()

def battery_status():

    battery = psutil.sensors_battery()

    return f"Battery is {battery.percent} percent"    
def take_screenshot():

    pyautogui.screenshot("screenshot.png")

def take_photo():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return

    ret, frame = camera.read()

    if ret:
        cv2.imwrite("photo.jpg", frame)

    camera.release()