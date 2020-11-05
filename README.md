# Student Health Monitor

[Raspberry Pi Documentation](https://github.com/NTI-Gymnasieingenjor/elevhalsa-digital-skylt/blob/master/documentation.md)

***

## Definition of Done
+ All group members shall understand the code.
+ Tests shall be green.
+ Code shall be commented.
+ Code and documentation shall be uploaded on GitHub.
+ Code shall follow the coding conventions in place.
+ Content/Documentation shall go through spellchecker.

## Before Merging With Main
+ All code and documentation should be read by groupmembers onsite and approved.
+ Should be complete and ready to be shipped to customer.

## Coding Conventions
+ Spaces: 4
+ Comments: English, space between // and the comment, capitalized.
+ Variable naming: CSS/HTML: kebab-case, JS: camelCase, classes: UpperCamelCase, Python: snake_case
+ HTML/CSS: Only use inline CSS with JavaScript actions.

# Programming Languages & Frameworks
## Programming Languages
+ HTML5
+ CSS3
+ Python3

## Frameworks
+ Bootstrap 4
+ FontAwesome 5

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

While it is not yet fully implemented, changing the information that is displayed on the monitor will be done by changing the information in [this google spreadsheet](https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/edit#gid=0). Our code then downloads the data from google sheets as csv files and then renders the slides with jekyll using the csv data.

# Copyright

Placeholder staff icons were made by [Gregor Cresnar](https://www.flaticon.com/authors/gregor-cresnar) from [www.flaticon.com](https://www.flaticon.com/).
