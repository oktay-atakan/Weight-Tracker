# Weight Tracker

A simple console-based application for tracking weight measurements over time.

## Features

* Add new weight measurements manually through the console.
* Read and display previously saved measurements.
* Update existing weight records.
* Delete existing measurements.
* Store weight data in a local data file.
* Automatically create the data file if it does not already exist.
* Import new measurements from properly formatted `.csv` or `.txt` files.
* Handle common input and file-related errors to prevent unexpected crashes.

## Data Storage

The application stores weight measurements together with their dates.

When the program starts, it reads the existing data file if one is available. If there is no existing data file, the application can create one automatically.

Users can then add, modify, or delete measurements, and the updated data is saved back to the file.

## Data Import

Measurements can be added in two ways:

1. Manually through console input.
2. By importing data from `.csv` or properly formatted `.txt` files.

This makes it possible to add multiple measurements without entering every record manually.

## Error Handling

Basic error handling is included throughout the application to deal with invalid inputs, missing files, and incorrectly formatted data.

## Future Work

The next main goal is to add simple data visualization and analysis features.

Possible future improvements include:

* Plotting weight changes over time.
* Performing basic exploratory data analysis (EDA) on weight data.
* Including additional information such as height and age in the analysis.
* Allowing users to enter a target weight.
* Showing progress toward the target weight.
* Highlighting periods when the user's weight is above, below, or within a desired range.
* Applying machine learning methods to experiment with weight prediction.
* Exploring other AI-based analysis methods using weight and additional user data.

## Long-Term Goal

A web or mobile interface could be developed in the future to turn the current console-based program into a complete application.
