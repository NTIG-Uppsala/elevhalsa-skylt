## Development:

Windows 10 Education

[GitBash 2.23.0 64-bit](https://git-scm.com/download/win)

Type in these commands in GitBash to clone down the files onto your computer:
   
     git clone https://gitlab.com/lazy-lounge/prislista.git
     git clone https://gitlab.com/lazy-lounge/prislista-resources.git

***
## Tests:
    Programs: 
    
[Jetbrains Pycharm Community Edition 2019.2.1](https://www.jetbrains.com/pycharm/download/other.html)

[Python 3.7.4](https://www.python.org/downloads/)

[chromedriver 77.0.3865.40](https://chromedriver.chromium.org/downloads)

[Java 8 update 221](https://www.java.com/sv/download/)		

***
## Plugins:
        Selenium 3.141.0				
    	        pip install selenium==3.141.0
    	Unittest
    	html5validator 0.3.1				
    	        pip install html5validator==0.3.1
***    
## Coding Language:
	Python

*Download Chromedriver.exe and save it in the same folder as the tests.*
    Automatically run tests at each commit:
    
		1. Open File Explorer, click view and turn on hidden items.
		2. Navigate to the ".git" folder then naviagate to the "hooks" folder.
		3. Rename the file "pre-commit.sample" to "pre-commit" and replace all code with the following lines:
               For Git/prislista:
                    #!/bin/sh
                
                    cd PyTests
                    python PrislistaTester.py
***
## Website:

Programs:

[Notepad++ 7.7.1](https://notepad-plus-plus.org/download/v7.7.1.html)
	
Browser:
        
        Google Chrome	77.0.3865.40

Coding Language:
        
        HTML5
        CSS3
	
Framework:  (Compiled CSS and JS)
        
[Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/download/)  

For the website to work you need to link to bootstraps css.
    Using these lines:
        
    <link rel="stylesheet" href="css/bootstrap.min.css">
        

Use these lines to link to bootstraps Javascript in the following order:

    <script type='text/javascript' src="js/jquery-3.3.1.slim.min.js"></script>
    <script type='text/javascript' src="js/popper.min.js"></script>
    <script type='text/javascript' src="js/bootstrap.min.js"></script>
***
## Raspberry:

*Tool and OS that are necessary:*

[SD formating tool](https://www.sdcard.org/downloads/formatter/eula_windows/)

[NOOBS OS](https://www.raspberrypi.org/downloads/noobs/)

[Vnc Viewer](https://www.realvnc.com/en/connect/download/viewer/)

***
### Tutorial for NOOBS installation:
		1. Install SD card formating tool
		2. Insert SD card in computer
		3. Format SD card with installed tool	
		4. Download NOOBS from raspberry website
		5. Unzip and transfer NOOBS directory content to SD card boot folder
		6. Plug in SD card into raspberry pi and connect to a Wi-Fi
		7. After connecting select Raspian and select install
		8. Follow install wizard to install Raspian on SD card

***
### Configuration

To start Configuring your Raspberry Pi 3B+, Create a directory named "Git" in /home/pi/. 

Change active directory to the Git directory with the command 

    "cd /home/pi/Git"
and then clone the git repostitory with the command

    "git clone git clone https://gitlab.com/lazy-lounge/prislista.git"
Change active directory to Prislista using the command

    "cd /home/pi/git/prislista/"
and then enter the following command

    "git config credential.helper store"
to store credentials.

Then type the command 

    "git push https://gitlab.com/lazy-lounge/prislista.git"

and log in with the credentials:

    username = LillaBoiBot

    password = boibot6969

After storing credentials enter the command 

    "git config --global user.name "LillaBoiBot"
and the command 

    "git config --global user.email "boibot6969@gmail.com"
Now that all credentials are stored, change directory to python using the command 

    "cd /home/pi/Git/prislista/Raspberry/python"
and then enter the command 

    "python symconfig.py"
to run a script that will configure your Raspberry Pi 3B+. 

***
### Disable Black Border around Screen
        1. Open the Command Line Interface and type the following command:
                sudo nano /boot/config.txt
        2. Find the disable_overscan line and change it to:
                disable_overscan=1

***
#### Rotating screen:
		1. Open the Command Line Interface and type in the following command:
                sudo nano /boot/config.txt
		2. At the bottom, write: 
                display_rotate=3
                extra_transpose_buffer=2

***
### Remove Chromium offer to Translate Page
        1.  Open Chromium browser
        2. Go to Settings --> Advanced Settings --> Language
        3. Untick Offer to Translate Page checkbox
        4. Exit Browser 

***
#### Browser autostart:
Already done if you followed the configuration step

		1. Open the Command Line Interface and type in the following command:
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Add the following lines at the bottom:
                @xset -dpms
                @xset s noblank
                @chromium-browser --kiosk /home/pi/Git/prislista/public/index.html --incognito

***
#### Remove Cursor:
Already done if you followed the configuration step

		1. Open Command Line Interface and type in the following commands:
                sudo apt-get install unclutter
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Add the following line at the bottom:
                @unclutter -idle 3

***
#### Remove Taskbar:
		1. Right-click on the panel and click Panel Settings.
		2. In the Geometry tab, change size to:

			Height = 200 pixels
			Width = 200 pixels
			Icon size = 16 pixels
			Edge = Right
			Alignment = Bottom

		3. In the advanced  tab, turn on automatic hiding with "size when minimized" at 0 pixels.
		4. In the appearance tab select solid color for taskbar.

***
#### Remove Screensaver:
Already done if you followed the configuration step

		1. Open Command Line Interface and type in the following command:
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Comment out @xscreensaver -no-splash using a hashtag at the beginning of that line.
		3. Then add this line:
                @xset s off
		4. Save and exit.

***
#### Remove Raspberry Icons:
		1. Open Command Line Interface and type in the following command:
                sudo nano /boot/cmdline.txt
		2. In the editor, at the end of the line add:
                logo.nologo

***
#### Replace Boot Image:
Already done if you followed the configuration step

		1. Open Command Line Interface and type in the following command:
                sudo cp /home/pi/Git/prislista/RaspberryPi/configuration/pix/splash.png /usr/share/plymouth/themes/pix/splash.png

***
#### Change Background Image:
Already done if you followed the configuration step

		1. Right-click on desktop and select desktop preferences.
		2. Under the desktop tab, in the Picture setting, select the picture named purple-logo.png
                /home/pi/Git/prislista/RaspberryPi/configuration/wallpaper.png

***
#### Remote Update Script:
Already done if you followed the configuration step

	To link the python file so it will run when you boot the Raspberry pi and continue to run follow these steps:
		1. Configure git and clone down the prislista repository in /home/pi/Git
		2. Open the Command Line Interface and write the following command:
                sudo nano /etc/profile
		3. Add the following line at the bottom:
             python3 /home/pi/Git/prislista/RaspberryPi/python/loop.py &
    
Notice: You will get an error each time the autopull script runs that is as follows (Fatal: unable to get credential storage lock: File exists)

The autopull script will still run as intended.     
		
***
#### Remote Control:
	To be able to control your raspberry's graphical interface remotely, follow these steps.
		1. Open the Command Line Interface and enter the following commands:
				sudo apt-get update
				sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
		2. Write the command sudo raspi-config
		3. Navigate to Interfacing Options and enable Vnc
		4. Get your raspberry's private ip by writing ifconfig in the Command Line
		5. Enter the ip in VNC viewer on your desktop and write the raspberry's username and password when promted:
				Username: pi
				Password: raspberry

***
#### Remove HDMI output at certain times:
        1. Open the Command Line Interface and enter the following command:
                crontab -e

        2. Type 1 to chose nano as your editor
        3. Go to the bottom of the opened document and type in the following commands:
                * * * * * fbset -accel false && sudo /opt/vc/bin/tvservice -o
                * * * * * sudo /opt/vc/bin/tvservice -p && fbset -accel true
                
                asterisk 1 = minutes (from 0 to 59)
                asterisk 2 = hours (from 0 to 24)
                asterisk 3 = day of month (from 1 to 31)
                asterisk 4 = month (from 1 to 12)
                asterisk 5 = day of week (from 0 to 7 where 0 to 6 is sunday to saturday and 7 is also sunday)
                
                example: 0 10 * * * fbset -accel false && sudo /opt/vc/bin/tvservice -o
                         5 10 * * * sudo /opt/vc/bin/tvservice -p && fbset -accel true
                         this will turn of HDMI output at 10:00 and start it agian at 10:05
***
## Coding Standard:
	Standard for indents , one indents 
	<html>

	    <body> 
		    <div>
	            </div>
	    </body>
	    
	</html>

The standard language for variable names, class names and such is english.

Comments in html are written this way:
    \<!-- this is a comment -->.

Comments in css are written this way:
    /* this is a comment */

Comments in Python are written with hashtags at the beginning of the line.
    #This is a comment

HTML5 Style Guide is to be followed.

 [W3Schools HTML5 STyle Guide](https://www.w3schools.com/html/html5_syntax.asp)


Variables should match in indentation.
    if (var1, var2,
        var3, var4)
