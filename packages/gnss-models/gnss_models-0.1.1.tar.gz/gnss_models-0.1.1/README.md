GNSS Data Models
================

A tool that inputs u-center generated csv file(s) of GNSS satellites data
and outputs a generated piecewise cubic curve fit model, including charts
and model evaluation in a PDF.

Choose a satellite number, the directory where all csv files are included (or the direct path to the csv file) that you
wish to perform the analysis on, and choose the output directory where the PDF will be created.

Condition: At least one file from the target directory (or the file targeted) must contain over 24h of continuous data.


Install
=======

    $ pip install gnss-models

Usage
=====


Example: Create models for specific file
----------------------------------------------------------------

    $ python gnss-models -file path_to_filename.csv -sat your_satellite_number -save path_to_save_directory

Example: Create models for all files from specific repository
----------------------------------------------------------------

    $ python gnss-models -dir path_to_directory -sat your_satellite_number -save path_to_save_directory

Get information about all arguments usage
-----------------------------------------

    $ python gnss-models -help