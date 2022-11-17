# Student Health Monitor

[Raspberry Pi Documentation](https://github.com/NTIG-Uppsala/elevhalsa-skylt/blob/master/documentation.md)

***

## Definition of Done
+ https://docs.google.com/document/d/1oLyPqJwN76pdIZRc8FyYE1W91b1bqy2K/edit

## Before Merging With Main
+ All code and documentation should be read by groupmembers onsite and approved.
+ Should be complete and ready to be shipped to customer.

## Coding Conventions
+ Spaces: 4
+ Comments: English, space between // and the comment, capitalized.
+ Variable naming: CSS/HTML: kebab-case, JS: camelCase, classes: UpperCamelCase, Python: snake_case
+ HTML/CSS: Only use inline CSS with JavaScript actions.

## Connecting to Rasberry
### To keep the cloned repo in Rasberry up to date with the Github repo: 
+ Code locally 
+ Push to the Github repo
+ Pull from the Rasberry 

# Programming Languages & Frameworks
## Programming Languages
+ HTML5
+ CSS3
+ Python3

## Frameworks
+ Bootstrap 4
+ FontAwesome 5
+ JQuery 3

## Static Site Generator
+ Jekyll

# Development Environment
**Editor** - Personal Preference <br>
**Version Control Host** - GitHub <br>
**OS** - WSL/Ubuntu(20.04) <br>
**Tests** - Python Selenium <br>
**Documentation** - English <br>
**Git Branches**
+ Feature branches
+ Branch names should use kebab-case
+ Needs to be approved by at least 2 members of the group before merging with main branch.

# How To Change The Information Currently Displayed

Changing the information that is displayed on the monitor will be done by changing the information in [this google spreadsheet](https://docs.google.com/spreadsheets/d/1qY1KYAY-AjFh2DWsjiVwOVj2qqJ29kpSs_YaBHi-TEs/edit#gid=0). Our code then downloads the data from google sheets as csv files and then renders the slides with jekyll using the csv data.

# Copyright

Placeholder staff icons were made by [Gregor Cresnar](https://www.flaticon.com/authors/gregor-cresnar) from [www.flaticon.com](https://www.flaticon.com/).
