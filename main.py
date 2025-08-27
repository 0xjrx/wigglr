#!/usr/bin/env python3
import argparse
import sys
from Xlib import X, display
import pyautogui
import time
def linux():

    while True:
        pyautogui.moveTo(1280,720)
        pyautogui.moveTo(1290,730)
        pyautogui.moveTo(1280,720)
        pyautogui.moveTo(1270,710)
        pyautogui.moveTo(1280,720)
        time.sleep(1)

def windows():

    while True:
        pyautogui.moveTo(1280,720)
        pyautogui.moveTo(1290,730)
        pyautogui.moveTo(1280,720)
        pyautogui.moveTo(1270,710)
        pyautogui.moveTo(1280,720)
        time.sleep(1)

def create_parser():
    parser = argparse.ArgumentParser(
        description='',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Global arguments
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    # Example command
    parser.add_argument(
        '--mode',
        choices = ["linux", "windows"],
        help='Run the main functionality'
    ) 
    return parser

def main():
    """Main function."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.mode =="linux":
        linux()
    if args.mode == "windows":
        windows()

if __name__ == '__main__':
    sys.exit(main())
