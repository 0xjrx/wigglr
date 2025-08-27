#!/usr/bin/env python3
import argparse
import sys
from Xlib import X, display

def linux():
    while True:
        d = display.Display()
        s = d.screen()
        root = s.root()
        root.warp_pointer(300,300)
        d.sync()


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
    

if __name__ == '__main__':
    sys.exit(main())
