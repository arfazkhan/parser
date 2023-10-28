import argparse
from parser_2 import PdfParser

def main():
    parser = argparse.ArgumentParser(description='PDF parsing tool - Extract text and data from PDF files')
    parser.add_argument('-f', '--file', help='File to parse (e.g., python main.py -f <path to your pdf>)')
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')

    args = parser.parse_args()

    if not args.file:
        parser.print_help()
        return

    file_path = args.file
    debug_mode = args.debug

    # Initialize PdfParser with the provided file path
    pdf_parser = PdfParser(file_path)
    pdf_parser.parse_pdf(file_path, debug_val=debug_mode)

if __name__ == "__main__":
    main()
