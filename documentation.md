# Setup/Installing dependencies
Begin by cloning this repo to your computer. 
After that you will need to install the requirements installed.

1. Jekyll: Install jekyll (if you dont have it installed already) following this [guide](https://jekyllrb.com/docs/installation/).

2. Now install the required dependencies which is python for your OS.

Linux:
```
sudo apt install python3 python3-pip xdotool
```

If needed on Windows:

Follow this link `https://www.python.org/downloads/` and download the latest version of python.
Make sure to mark Add to PATH while installing python

3. After installing the required dependencies for your OS, run the following code in your CMD while you are in the project folder:
```
cd C:\Users\user.name\AppData\Local\Programs\Python\Python39

py -m pip install -r requirements.txt (For Windows)

or

pip install -r requirements.txt (For Linux)
```

# Raspberry Pi

These steps are already done so you don't have to do them unless you are starting from scratch, so to say starting with a new Raspberry Pi

Tool and OS that are necessary:

SD formatting tool https://www.sdcard.org/downloads/formatter/eula_windows/
NOOBS OS https://www.raspberrypi.org/downloads/noobs/

Tutorial for NOOBS installation:
1. Install SD card formatting tool
2. Insert SD card in computer
3. Format SD card with installed tool	
4. Download NOOBS from Raspberry's website
5. Unzip and transfer NOOBS directory content to SD card boot folder
6. Plug in SD card into Raspberry Pi and connect to a Wi-Fi
7. After connecting select Raspbian and select install
8. Follow install wizard to install Raspbian on SD card

***

## How to Remote Control Raspberry Pi

### Download/Install VNC Viewer
1. Go to https://www.realvnc.com/en/connect/download/viewer/
2. Download and install VNC viewer on the computer or phone that you want to control the RPI from.
    
### Remote control the Raspberry Pi
1. On the Pi, run the following code to get the IP adress:
```
hostname -I 
```
2. Open VNC Viewer, enter the IP of the RPi in the top of the VNC application. If you’ve entered the correct IP Address, you will be prompted for your Raspberry Pi user credentials. 
3. Enter the Raspberry Pi user credentials and all done! You shall now be able to remote access your Raspberry Pi from this workstation or any other devices with VNC Viewer configured.

***
### Enable Remote Control:
To be able to control your raspberry's graphical interface remotely, follow these steps.
1. Open the Command Line Interface and enter the following commands:
       
        sudo apt-get update
        sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
2. Write this command: 
    
        sudo raspi-config
3. Navigate to Interfacing Options and enable VNC

***

### Configuration

To change the resolution of the raspberry outputs navigate to settings > screen configuration > configure > screens > HTMI-X > resolution > your desired resolution.

To start configuring your Raspberry Pi, create a directory named "Git" in your Raspberry file manager /home/pi/.

Change active directory to the Git directory with the command:

	cd /home/pi/Git
and then clone the git repository with the command:

   	git clone https://github.com/NTIG-Uppsala/elevhalsa-skylt
Change active directory to elevhalsa-skylt using the command:

    	cd /home/pi/git/elevhalsa-skylt/
    
***
### New Repository

If you create a new repository and clone it, you need to modify two files in the raspberry: 

1. autostart: This file builds the site using jekyll and opens the chromium browser and shows the website in fullscreen.
- Write the following code to open it:

        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
- Change the path from the old repository folder to the new one you cloned.

2. crontab -e: This file re-uploads the site at midnight.
- Write the file's name (crontab -e) in the CLI to open it.
- Change the path from the old repository folder to the new one you cloned.
***
### Browser autostart:

1. Open the Command Line Interface and type in the following command:
               
        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
2. Add the following lines at the bottom:
	
        python3 /home/pi/Git/elevhalsa-digital-skylt/download-data.py
        chromium-browser --force-device-scale-factor=0.6 --start-fullscreen --kiosk http://127.0.0.1:4000/ --incognito
- `"--force-device-scale-factor=0.6"` scales the browser by 60%. Note that this is different from zooming out on the browser.

3. Open the Command Line Interface and type in the following command:

        nano /home/pi/.bashrc
4. Add the following lines at the bottom:

        jekyll serve -s /home/pi/Git/elevhalsa-skylt-site
- This runs `jekyll serve -s /home/pi/Git/elevhalsa-skylt-site` whenever a terminal starts.
***
### Change active display times
1. Open the Command Line Interface and enter the following command:

        crontab -e

2. Type 1 to choose nano as your editor.
3. Go to the bottom of the opened document and type in the following commands:

        * * * * * sudo vcgencmd display_power 0
        * * * * * sudo reboot
        
        asterisk 1 = minutes (from 0 to 59)
        asterisk 2 = hours (from 0 to 24)
        asterisk 3 = day of month (from 1 to 31)
        asterisk 4 = month (from 1 to 12)
        asterisk 5 = day of week (0 - 7) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
        
        example: 0 10 * * * sudo vcgencmd display_power 0
                    5 10 * * * sudo reboot
    This will turn of HDMI output at 10:00 and start it again at 10:05.

***    

<!-- ## Custom Shortcuts

    Ctrl + F11 : disables HDMI output and closes all chromium instances
    Ctrl + F12 : enables HDMI output and opens the index file in elevhalsa-digital-skylt -->

### Create shortcut
1. Open the Command Line Interface and enter the following command:
        
        sudo nano /etc/xdg/openbox/lxde-pi-rc.xml file

2. Find the `<keyboard></keyboard>` tags and add the following text between the tags:

        <keybind key="">
            <action name="Execute">
                <command>
                </command>
            </action>
        </keybind>
        
3. Add the shortcut in the `<keybind>` tag and command you want to run between the `<command></command>` tags

    Example for running a bash script when Ctrl+F11 is pressed:

        <keybind key="C-F11">
            <action name="Execute">
                <command>
                    bash ~/shortcut/close
                </command>
            </action>
        </keybind>

    C - stands for control

    A - stands for alt

    S - stands for shift 
    
***            
### Disable Black Border around Screen
1. Open the Command Line Interface and type the following command:

        sudo nano /boot/config.txt
2. Find the disable_overscan line and change it to:

        disable_overscan=1

***
### Remove Chromium offer to Translate Page
1. Open Chromium browser
2. Go to Settings > Advanced Settings > Language
3. Untick Offer to Translate Page checkbox
4. Exit Browser 

***
### Remove Cursor:

1. Open Command Line Interface and type in the following commands:
	```
	sudo apt-get install unclutter
	sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
	```
2. Add the following line at the bottom:
	```
	@unclutter -idle 3
	```
***
### Hide Taskbar:

1. Right-click on the taskbar and select `Panel Settings`
2. Click on the `Advanced` tab, and check `Minimize panel when not in use`

***
### Remove Screensaver:

1. Open Command Line Interface and type in the following command:

        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
2. Comment out `@xscreensaver -no-splash` using a hashtag at the beginning of that line.
3. Then add this line:
        
        @xset s off
4. Save and exit.

***
### Disable Raspberry Pi sleep mode

1. Open the Command Line Interface and type in the following command:
        
        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
2. Add the following lines at the bottom:
        
        @xset -dpms
        @xset s noblank

***
### Remove Raspberry Icons:
1. Open Command Line Interface and type in the following command:
        
        sudo nano /boot/cmdline.txt
2. In the editor, at the end of the line add:
        
        logo.nologo

***
### Replace Boot Image:

1. Open Command Line Interface and type in the following command:
       
        sudo cp /home/pi/my_splash.png /usr/share/plymouth/themes/pix/splash.png

***
### Change Background Image:

1. Right-click on desktop and select desktop preferences.  
2. Under the desktop tab, in the Picture setting, click on the folder next to Picture.  
3. Navigate to `/home/pi/my_splash.png`, press open, then press ok.  

***


<!-- 
don't forget that
images must be jpg
 -->
