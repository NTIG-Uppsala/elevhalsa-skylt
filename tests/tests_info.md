# Tests
## Requirements
Use the following command to download the libraries needed to use the tests. Use this in a python terminal **NOT in the WSL**
    
    py -m pip install (library)
The libraries needed are:
- Selenium
- openpyxl
- gspread
## Info
- Be sure to have oauth2client installed via pip if you are using unittest in Visual Studio Code. otherwise the code will crash.

        py -m pip install oauth2client
- And be sure to have a jekyll server up before starting any test.

        jekyll serve -s site
