# Student Health Monitor

[Raspberry Pi Documentation](https://github.com/NTI-Gymnasieingenjor/elevhalsa-digital-skylt/blob/master/documentation.md)

***

## Definition of Done
+ All group members shall understand the code.
+ Tests shall be green.
+ Code shall be commented.
+ Code and documentation shall be uploaded on GitHub.
+ Code shall follow the coding conventions in place.

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
+ JavaScript

## Frameworks
+ Bootstrap 4
+ FontAwesome 5
+ Selenium (for testing)

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

# Google Sheets scripts
We use google app scripts for features in the google sheet. The code in the sheet script is the following:
```Javascript
// If the text limit is reached all characters over the limit gets marked with red text color
function onEdit(e) {
  var limit = 355;
 
  if(e.range.getColumn() == 10){
    limit = 185;
  } else if(e.range.getColumn() == 2){
    if(e.range.getSheet().getName() == "VIKTIGA_DATUM"){
      limit = 245;
    } else {
      limit = 1500;
    }
  }
  if(e.value.length > limit) {
    let richTextValue = e.range.getRichTextValue()
    let oldContent = richTextValue.getText();
    let newStyles = [{
      start: limit,
      end: oldContent.length,
      style: SpreadsheetApp.newTextStyle().setBold(true).setForegroundColor("red").build()
    }]
    let richText = SpreadsheetApp.newRichTextValue().setText(oldContent);
    richText.setTextStyle(newStyles[0].start, newStyles[0].end, newStyles[0].style);
    e.range.setRichTextValue(richText.build())
  }
}

// Clears cells if the date and time in that cell has passed.
function clearDropin(){
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var nti_sheet = ss.getSheetByName("NTI");
  var proc_sheet = ss.getSheetByName("PROCIVITAS");
  var col_start = "K";
  var col_end = "L";
  let sheets = [nti_sheet, proc_sheet];
  sheets.forEach((sh)=> {
      for(let i = 2; i <= sh.getLastRow() + 1; i++){
          end_time = sh.getRange(col_end + i).getValue();
          if(end_time != "") {
              let today = new Date();
              let date = ("0" + today.getDate()).slice(-2);
              let month = ("0" + (today.getMonth() + 1)).slice(-2);
              let year = today.getFullYear();
              let hour = ("0" + today.getHours()).slice(-2);
              let minutes = ("0" + today.getMinutes()).slice(-2);
              let todaysDate = year + "-" + month + "-" + date;
              let date_and_time = end_time.split(" ");

              if(todaysDate == date_and_time[0]){
                  let endHour = date_and_time[1].split(":")[0]
                  let endMin = date_and_time[1].split(":")[1]
                  if(hour > endHour || (hour == endHour && minutes >= endMin)){
                    sh.getRange(col_start + i).clear()
                    sh.getRange(col_end + i).clear()
                  }
              } else {
                  sh.getRange(col_start + i).clear()
                  sh.getRange(col_end + i).clear()
              }
          }
      }
  })
}

// Clears cells if the date in that row has passed.
function clearCountdown(){
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("VIKTIGA_DATUM");
  for(let i = 2; i <= sheet.getLastRow() + 1; i++){
    var countdownColumn = sheet.getRange("C" + i).getValue();
    if(countdownColumn != "") {
      let today = new Date();
      
      let countDownYear = countdownColumn.split("-")[0]
      let countDownMonth = countdownColumn.split("-")[1]
      let countDownDate = countdownColumn.split("-")[2]
      
      let countdown = new Date(countDownYear, countDownMonth - 1 , countDownDate);
      
      if(today > countdown){
        sheet.getRange("A" + i).clear();
        sheet.getRange("B" + i).clear();
        sheet.getRange("C" + i).clear();
      }
    }
  }
}
```

# Copyright

Placeholder staff icons were made by [Gregor Cresnar](https://www.flaticon.com/authors/gregor-cresnar) from [www.flaticon.com](https://www.flaticon.com/).
