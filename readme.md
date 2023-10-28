# PDF Parser Prototype

This is an early prototype of a PDF parsing tool that is being developed to automate the extraction and population of required information for job applications. Currently, it functions as a command line tool, and future plans include implementing it as a web application. This README provides information on the purpose of the tool and how to use it.

## Purpose

The PDF Parser Prototype is designed to extract text and data from PDF files, specifically for parsing resumes or CVs. It aims to retrieve essential information such as the candidate's name, contact details, educational qualifications, and more. The tool can also identify and extract social media URLs, including LinkedIn and GitHub profiles.

Please note that this is an early prototype and is subject to further development for a more innovative and user-friendly future version.

## Usage

To use the PDF Parser Prototype, follow these steps:

1. **Installation**: Make sure you have the necessary Python libraries installed. You can install them using `pip`:

   ```bash
   pip install PyPDF2 argparse
2. **Clone the Repository**: Clone the repository containing the main.py and parser_2.py files to your local machine.

3. **Command Line Usage**:
    - Open a terminal or command prompt.
    - Navigate to the directory where the main.py file is located.
    - Run the tool by executing the following command:

         ```bash
        python main.py -f <path to your PDF file> [-d]
    - Replace <path to your PDF file> with the path to the PDF file you want to parse.
    - The optional -d flag is for enabling debug mode, which provides additional information during parsing.

4. **Results**: After running the command, the tool will extract and display the following information (if found in the PDF):

    - Candidate's Name
    - Email Address
    - Mobile Number
    - Gender (if specified)
    - Highest Qualification
    - College/University
    - Specialization/Branch of Study
    - Graduation Year
    - LinkedIn and GitHub URLs (if available)
    - Other URLs (if available)

## Future Development
As mentioned, this is an early prototype of the PDF Parser. In the future, the tool is expected to evolve into a web application with a more user-friendly interface. This web app will automate the extraction and organization of information from resumes for job applications.

We appreciate your interest in this prototype and look forward to delivering a more advanced and innovative solution in the future. Stay tuned for updates and improvements!

## Contribution
This project is open source, and we welcome contributions from the community. If you'd like to contribute, here's how you can get involved:

1. **Fork the Repository**: Click the "Fork" button at the top right of this repository to create your own copy.
2. **Make Your Changes**: Make your desired updates and improvements in your forked repository.
3. **Submit a Pull Request**: When you're ready, submit a pull request to this repository. We'll review your changes and consider merging them into the main project.
4. **Give a Star**: If you find this project useful and like what we're doing, please consider giving this repository a star to show your support.

Thank you for contributing to the PDF Parser Prototype! Your contributions help make this project better for everyone.