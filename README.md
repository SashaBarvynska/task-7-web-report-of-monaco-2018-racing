

DESCRIPTION:

The application is to read data from 3 files, order racers by time and print report that shows the top 15 racers and the rest after underline INSTALLATION: To install the package use:

pip install -i https://test.pypi.org/simple/ top-15-racers-Barvynska

HOW TO USE:

Create file, for example app.py with following content:

from task_Barvynska import main

main()

Run following command in console:

    Shows statistic about driver:

py app.py --files [path to folder] --driver “Sebastian Vettel”

    Shows list of drivers in :

increasing order: py app.py --files [path to folder] --asc

or

decreasing order: py app.py --files [path to folder] --desc

Note: default order is asc

Note: Folder should containe files: start.log, end.log, abbreviations.txt
