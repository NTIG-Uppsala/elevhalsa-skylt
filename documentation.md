# Student Health Staff Monitor Documentation

## Table of Contents

- [Set up development environment](documentation.md#set-up-development-environment)
- [Raspberry Pi](documentation.md#raspberry-pi)
- [How to Remote Control Raspberry Pi](documentation.md#how-to-remote-control-raspberry-pi)
- [Configuration](documentation.md#configuration)
- [New Repository](documentation.md#new-repository)
- [Set Up Autostart](documentation.md#set-up-autostart)
- [Change active display times](documentation.md#change-active-display-times)
- [Create shortcut](documentation.md#create-shortcut)
- [Disable Black Border around Screen](documentation.md#disable-black-border-around-screen)
- [Remove Chromium offer to Translate Page](documentation.md#remove-chromium-offer-to-translate-page)
- [Remove Cursor](documentation.md#remove-cursor)
- [Hide Taskbar](documentation.md#hide-taskbar)
- [Remove Screensaver](documentation.md#remove-screensaver)
- [Disable Raspberry Pi sleep mode](documentation.md#disable-raspberry-pi-sleep-mode)
- [Remove Raspberry Icons](documentation.md#remove-raspberry-icons)
- [Replace Boot Image](documentation.md#replace-boot-image)
- [Change Background Image](documentation.md#change-background-image)
- [Hardware used](documentation.md#hardware-used)

## Set up development environment

### Step 1 - Clone this repository

If you use Github Desktop, go to [the repository page](https://github.com/NTIG-Uppsala/elevhalsa-skylt) and press the "Code" button. Then click on "Open with GitHub Desktop". Choose directory and then press "Clone".

> Be sure to choose a directory that is not synced with OneDrive, Google Drive, or similar apps. Otherwise Jekyll will not work.

### Step 2 - install WSL Ubuntu

- Go to the Control Panel → Programs → Programs and Feautures → Turn Windows features on or off

- Check the Windows-subsystem box (commonly found at the bottom) and press OK. Windows will prompt a restart and press restart

- Press (Windows) + R

- Write "cmd" and press enter

- Run the command: `wsl --install`
  > Try `wsl --install -d Ubuntu` if the command above does not work

- Follow the instructions shown on the screen

### Step 3 - install Ruby and jekyll

- Open a terminal in the folder that the repository has been cloned into. This can be done by opening this cloned repository in Github Desktop and pressing Ctrl + Ö. (Ctrl + ` for American keyboard layouts)

**Run the following command in an Ubuntu terminal (WSL)**
```
sudo apt update ; sudo apt-get install ruby-full build-essential zlib1g-dev ; echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc ; echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc ; echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc ; source ~/.bashrc ;gem install jekyll bundler ; sudo apt install python3 python3-pip ; pip install -r requirements.txt ; pip install xdotool
```

### Step 4 - Add google service account credentials

Download the file [service_account_credentials.json](https://drive.google.com/file/d/177ZQ10REm72G-kb8c3xZvUWBMFjTJQYq/) and put it in the cloned repository on your computer.

> The google service account api credentials are not stored in the GitHub repository for security reasons.

### Step 5 - Running it

#### Set up
Most of the programs require an .env file. To create one, make a new file in your directory and name it .env. The contents of the file should be the Google Sheet IDs that you are using for your project.
```
sheet_id = SPREADSHEET_ID

test_sheet_id = SPREADSHEET_ID
``` 
`sheet_id` and `test_sheet_id` are the variable names that are already in the code. For the easiest setup, use those.

#### Running
To run any of the Python programs, you have two choices. You can either run them without any arguments, using the content from the .env file and the recommended file paths for each program:
```
python3 get_csv.py
```
Or you can type in a custom spreadsheet ID and file path, which may require configuration of the code:```
python3 get_csv.py <SPREADSHEET_ID> <SITE_DATA_DIR>
```
`SPREADSHEET_ID` can be found in the sheet's url.

`SITE_DATA_DIR` is the location where data is stored for showcase on the site/Pi.
```
jekyll serve -s site
```
`jekyll serve -s site` runs the site locally and let's you preview it.

### Step 6 - Development environment for testing

See [tests_info.md](tests/tests_info.md) for how to install necessary libraries for testing.

## Keeping the repo up to date in the Raspberry Pi

- Code locally, either on a development Raspberry Pi or on your personal computer
- Push to the Github repo
- Pull from the main branch on the Raspberry Pi

## Raspberry Pi

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

### Enable Remote Control

To be able to control your raspberry's graphical interface remotely, follow these steps.
1. Open the Command Line Interface and enter the following commands:

        sudo apt-get update
        sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
2. Write this command:

        sudo raspi-config
3. Navigate to Interfacing Options and enable VNC

***

## Configuration

To change the resolution of the raspberry outputs navigate to settings > screen configuration > configure > screens > HTMI-X > resolution > your desired resolution.

To start configuring your Raspberry Pi, create a directory named "Git" in your Raspberry file manager /home/pi/.

Change active directory to the Git directory with the command:

	cd /home/pi/Git
and then clone the git repository with the command:

   	git clone https://github.com/NTIG-Uppsala/elevhalsa-skylt
Change active directory to elevhalsa-skylt using the command:

    	cd /home/pi/git/elevhalsa-skylt/

***

## New Repository

If you create a new repository and clone it, you need to modify two files in the raspberry:

1. autostart: This file builds the site using Jekyll and opens the chromium browser and shows the website in fullscreen.
- Write the following code to open it:

        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
- Change the path from the old repository folder to the new one you cloned.

2. crontab -e: This file re-uploads the site at midnight.
- Write the file's name (crontab -e) in the CLI to open it.
- Change the path from the old repository folder to the new one you cloned.
***

## Set Up Autostart

Follow these steps to ensure that the website automatically displays on the Raspberry Pi after it starts.
The commands should be run on the Raspberry Pi.

1. Open the Command Line Interface and type in the following command:

        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
2. Add the following lines at the bottom:

        bash /home/pi/Git/elevhalsa-skylt/on_startup.sh

3. Open the Command Line Interface and type in the following command:

        nano /home/pi/.bashrc
4. Add the following lines at the bottom:

        jekyll serve -s /home/pi/Git/elevhalsa-skylt-site

The jekyll serve command is in .bashrc and not in `on_startup.sh` because it does not work when placed in `on_startup.sh`.
It is not optimal that it is in `.bashrc `
because all commands in `.bashrc` are run everytime a new terminal is opened.
So every time you ssh into the Raspberry Pi it tries to start a Jekyll server, but fails because one is already running.

Commands in `autostart` are processed in a parallel fashion, so commands do not wait for previous commands to finish. More about this [here](https://forums.raspberrypi.com/viewtopic.php?t=294014).
For this reason, the commands are put in `on_startup.sh` instead, and the autostart file just runs `on_startup.sh`.

***

## Change active display times

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

## Create shortcut

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

## Disable Black Border around Screen

1. Open the Command Line Interface and type the following command:

        sudo nano /boot/config.txt
2. Find the disable_overscan line and change it to:

        disable_overscan=1

***

## Remove Chromium offer to Translate Page

1. Open Chromium browser
2. Go to Settings > Advanced Settings > Language
3. Untick Offer to Translate Page checkbox
4. Exit Browser

***

## Remove Cursor

1. Open Command Line Interface and type in the following commands:
	```
	sudo apt-get install unclutter
	```
	```
	sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
	```
2. Add the following line at the bottom:
	```
	@unclutter -idle 3
	```
***

## Hide Taskbar

1. Right-click on the taskbar and select `Panel Settings`
2. Click on the `Advanced` tab, and check `Minimize panel when not in use`

***

## Remove Screensaver

1. Open Command Line Interface and type in the following command:

        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
2. Comment out `@xscreensaver -no-splash` using a hashtag at the beginning of that line.
3. Then add this line:

        @xset s off
4. Save and exit.

***

## Disable Raspberry Pi sleep mode

1. Open the Command Line Interface and type in the following command:

        sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
2. Add the following lines at the bottom:

        @xset -dpms
        @xset s noblank

***

## Remove Raspberry Icons

1. Open Command Line Interface and type in the following command:

        sudo nano /boot/cmdline.txt
2. In the editor, at the end of the line add:

        logo.nologo

***

## Replace Boot Image

1. Open Command Line Interface and type in the following command:

        sudo cp /home/pi/my_splash.png /usr/share/plymouth/themes/pix/splash.png

***

## Change Background Image

1. Right-click on desktop and select desktop preferences.  
2. Under the desktop tab, in the Picture setting, click on the folder next to Picture.  
3. Navigate to `/home/pi/my_splash.png`, press open, then press ok.  

***

## Hardware used

### Screen

- Name: Voxicon VXM232HD
- Size: 32 inches
- Resolution: 1360 x 768
- Touch screen: No
- Number of HDMI-ports: 2

### Raspberry Pi 4 Model B Rev 1.2
