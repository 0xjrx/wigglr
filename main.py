#!/usr/bin/env python3
import argparse
import sys
import logging

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
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    # Subcommands
    subparsers = parser.add_subparsers(
        dest='command',
        help='Available commands'
    )
    
    # Example command
    cmd_parser = subparsers.add_parser(
        'run',
        help='Run the main functionality'
    )
    
    cmd_parser.add_argument(
        'input',
        help='Input file or data'
    )
    
    cmd_parser.add_argument(
        '-o', '--output',
        help='Output file'
    )
    
    return parser

def main():
    """Main function."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    # Handle commands
    if not args.command:
        parser.print_help()
        return 1
    
    if args.command == 'run':
        logging.info(f"Processing: {args.input}")
        if args.output:
            logging.info(f"Output: {args.output}")
        
        # Your main logic here
        print("Hello, World!")
        return 0
    
    return 1

if __name__ == '__main__':
    sys.exit(main())
