# Student Health Monitor

[Raspberry Pi Documentation](documentation.md#raspberry-pi)

***

## Definition of Done
+ https://docs.google.com/document/d/1oLyPqJwN76pdIZRc8FyYE1W91b1bqy2K/edit

## Before Merging With Main
+ All code and documentation should be read by groupmembers onsite and approved.
+ Should be complete and ready to be shipped to customer.

# Programming Languages & Frameworks
## Programming Languages
+ HTML5
+ CSS3
+ Python3
+ JavaScript V8

## Frameworks
+ Bootstrap 3.4.1
+ JQuery 3.6.0

## Static Site Generator
+ Jekyll 4.3.2 (Installed on Ruby 3.0.2)

## Coding Conventions
+ [pep8](https://peps.python.org/pep-0008/) For Python 
+ [w3schools HTML Style Guide](https://www.w3schools.com/html/html5_syntax.asp) For HTML/CSS
+ [w3schools JavaScript Style Guide](https://www.w3schools.com/js/js_conventions.asp) For JavaScript

# Development Environment
[How to set up a development environment](documentation.md#set-up-development-environment)
<br><br>
**Editor** - Visual Studio Code <br>
Extension: Remote - SSH <br><br>
**Version Control Host** - GitHub <br><br>
**OS** - Windows 10 <br><br>
**Documentation** - English <br>

### Keeping the repo up to date in the Raspberry Pi: 
+ Code locally, either on a development Raspberry Pi or on your personal computer
+ Push to the Github repo
+ Pull from the main Raspberry Pi

# How To Change The Information Currently Displayed

# How To Change The Information Currently Displayed
Changing the information that is displayed on the monitor will be done by changing the information in [this](https://docs.google.com/spreadsheets/d/1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs) google spreadsheet. Our code then downloads the data from google sheets as csv files and then renders the slides with jekyll using the csv data.
