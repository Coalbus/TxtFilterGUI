This Python script provides a simple Graphical User Interface (GUI) for filtering large text files based on user-specified keywords. Built with Tkinter, the script allows users to apply multiple keyword filters to a chosen text file and view the resulting filtered lines directly in the application window.

Features
File Browsing: Choose the text file you wish to apply filters to.
Filtering: Input a comma-separated list of keywords, then click "Apply Filter". The script will display lines from the text file that contain all the specified keywords.
Exporting: After applying filters, you can export the filtered results to a new .txt file by clicking "Export Results".
Usage
To use the script, simply run it using Python (Tkinter needs to be installed, which it should be by default in most Python installations).

Once the GUI is up:

Click "Browse" to select the text file you want to filter.
Input your keywords in the text field, separated by commas.
Click "Apply Filter" to see the lines containing all the specified keywords.
Click "Export Results" to save the filtered lines to a new text file.
This tool is helpful for quickly filtering large text files based on specific criteria, and it's designed to be easy to use even for those with little to no coding experience.

Installation
This script can be turned into a standalone application using utilities like PyInstaller, enabling it to run on systems even without Python installed. Check the PyInstaller documentation to learn how to freeze Python scripts into executables.
