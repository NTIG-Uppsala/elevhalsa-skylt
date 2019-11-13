## Custom Shortcuts

### Ctrl + F11 : disables HDMI output and closes all chromium instances

### Ctrl + F12 : enables HDMI output and opens the index file in elevhalsa-digital-skylt


## Where to change hardcoded data

A carousel item found in Skylt/index.html.
Anything wrapped with curly brackets can be changed.

```html
<div class="carousel-item active">
    <div class="name row justify-content-between">
        <div class="col-7">
            <!-- Name -->
            <h2 style="padding-left: 10px;"> {Name} </h2>
        </div>
        <div class="col-4 pl-0">
            <!-- Role -->
                <h2>{Role}</h2>
        </div>
    </div>
    <div class="row">
        <div class="col-7">
            <p>
                <!-- Info -->
                {Info}

            </p>
        </div>
        <div class="col-4 text-center">
            <!-- Image -->
            <img class="profile-image" src="{Image source}" />
        </div>
    </div>
    <p class="contact">
        <!-- Email -->
        <i class="fa fa-envelope"></i> E-post: {Email}<br />

        <!-- Phone -->
        <i class="fa fa-phone"></i> Telefon: {Phone}<br />

        <!-- Working days and hours -->
        <i class="fa fa-calendar-alt"></i> Arbetar: {Working days and hours}<br />

        <!-- room number/location -->
        <i class="fa fa-map-marker-alt"></i> Sal: {Room number/location}
    </p>
</div>
```

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

To change the resolution of the Raspberry outputs navigate to settings>screen configuration>configure>screens>HTMI-X>resolution>your desired resolution

To start Configuring your Raspberry Pi 4 Model B, Create a directory named "Git" in /home/pi/. 


Change active directory to the Git directory with the command 

    "cd /home/pi/Git"
and then clone the git repostitory with the command

    "git clone https://gitlab.com/nordtech/elevhalsa-digital-skylt.git"
Change active directory to elevhalsa-digital-skylt using the command

    "cd /home/pi/git/elevhalsa-digital-skylt/"
and then enter the following command


### Change active display times
        1. Open the Command Line Interface and enter the following command:
                sudo nano /etc/xdg/openbox/lxde-pi-rc.xml file

        2. Find the <keyboard></keyboard> tags and add the following text between the tags to add a shortcut
        
               <keybind key="">
                  <action name="Execute">
                     <command>
                     </command>
                  </action>
                </keybind>
                
        3. Add the shortcut in the <keybind> tag and command you want to run between the <command></command> tags

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
            

### Create shortcut
        1. Open the Command Line Interface and enter the following command:
                crontab -e

        2. Type 1 to chose nano as your editor
        3. Go to the bottom of the opened document and type in the following commands:
                * * * * * sudo vcgencmd display_power 0
                * * * * * sudo reboot
    

### Disable Black Border around Screen
        1. Open the Command Line Interface and type the following command:
                sudo nano /boot/config.txt
        2. Find the disable_overscan line and change it to:
                disable_overscan=1

***
### Remove Chromium offer to Translate Page
        1.  Open Chromium browser
        2. Go to Settings --> Advanced Settings --> Language
        3. Untick Offer to Translate Page checkbox
        4. Exit Browser 

***
#### Browser autostart:

		1. Open the Command Line Interface and type in the following command:
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Add the following lines at the bottom:
                chromium-browser --start-fullscreen --kiosk /home/pi/Git/elevhalsa-digital-skylt/Skylt/index.html --incognito
***
#### Remove Cursor:

		1. Open Command Line Interface and type in the following commands:
                sudo apt-get install unclutter
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Add the following line at the bottom:
                @unclutter -idle 3

***
#### Hide Taskbar:

		1. Right-click on the taskbar and select "Panel Settings"
		2. Click on the "Advanced" tab, and check "Minimize panel when not in use"

***
#### Remove Screensaver:

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

		1. Open Command Line Interface and type in the following command:
                sudo cp /home/pi/Git/prislista/RaspberryPi/configuration/pix/splash.png /usr/share/plymouth/themes/pix/splash.png

***
#### Change Background Image:

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
				Password: TE4NordTech

***