// Clears cells if the date and time in that cell has passed.
function clearDropin(){
  var ss = SpreadsheetApp.getActiveSpreadsheet("https://docs.google.com/spreadsheets/d/1k0qCUQbKvipCa8dhFcFjccRAWVGSeYF_MJwcu1Fy5Ls/edit#gid=0");
  var nti_sheet = ss.getSheetByName("NTI");
  var maud_sheet = ss.getSheetByName("MAUD");
  var proc_sheet = ss.getSheetByName("PROCIVITAS");
  var col_start = "K";
  var col_end = "L";
  let sheets = [nti_sheet, maud_sheet, proc_sheet];
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