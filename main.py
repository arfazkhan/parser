
import argparse
from parser import PdfParser

def main():
    parser = argparse.ArgumentParser(description='PDF parser endpoint')
    parser.add_argument('-f', '--file', help='File to parse')
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')

    args = parser.parse_args()
    file_path = args.file
    debug_mode = args.debug

    if file_path:
        # Initialize PdfParser with the provided file path
        pdf_parser = PdfParser(file_path)
        pdf_parser.parse_pdf(file_path, debug_val=debug_mode)
    else:
        print("Please provide a file to parse.")

if __name__ == "__main__":
    main()
