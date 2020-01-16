Daniel Berger

What does this program do?
1. the command line argument for the keyword is checked
2. if the argument is save then the clipboard contents are saved to the keyword
3. if the argument is list, then all the keywords are copied to the clipboard
4. Otherwise, the text for the keyword is copied to the clipboard

This means the code will need to do the following:
1. Read the command line arguments from sys.argv?
2. Read and write to the clipboard
3. Save and load to shelf file

