---
ITS 211 – Project 5
Basic Markdown File Analyzer (Python, OOP)
Author: Trent Mora
Course: ITS 211 – Introduction to Python Programming
---
ASL README HERE: https://youtu.be/dn2CK9qkLqk

This is a simple Python program that scans a given directory for
Markdown (.md) files, and analyzes the content of these files by 
creating a corresponding representative object for each Markdown file.

Then these representative objects are aggreated into a single report.txt
through FileAnalysis.
---

What the Program Does:
    Given a folder path from the user, the program:
        • Finds all .md files in the directory
        • Creates a FileStatus object for each file
        • Analyzes each file to determine:
            • Whether it contains YAML metadata (---)
            • Whether it mentions “GPT”
            • How many words it contains (letters only, ≥ 3 characters)
            • Identifies orphaned files (files with zero valid words)
        • Outputs:
            • A summary in the terminal
            • A detailed report.txt file

FileStatus
    Represents a single Markdown file and stores:
        • File path
        • YAML status
        • GPT status
        • Word count

Each analysis method updates the object’s internal state, which is later 
accessed through getter methods.

    FileAnalysis
    Works with a list of FileStatus objects to:
        • Count files with YAML
        • Count files mentioning GPT
        • Sum total words
        • Count orphaned files
        • Write the final report

FILE Structure:
    Project_5/
    │
    ├── main.py           # Program entry point
    ├── FileStatus.py     # File-level object and analysis logic
    ├── FileAnalysis.py   # Collection-level analysis and reporting
    ├── report.txt        # Auto-generated analysis report
    └── README.md         # Project documentation

Sample Output on Terminal:
    ==== Summary ====
    Total files: 5
    Files with YAML: 1
    Files mentioning GPT: 2
    Total words (>=3 letters): 1420
    Orphaned Notes: 2
