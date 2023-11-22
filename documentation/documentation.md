# Student Health Staff Monitor Documentation

## Table of Contents

- [Set up development environment](documentation.md#set-up-development-environment)
- [Tests](documentation.md#tests)
- [Keeping the repo up to date in the Raspberry Pi](documentation.md#keeping-the-repo-up-to-date-in-the-raspberry-pi)
- [How to Remote Control Raspberry Pi](documentation.md#how-to-remote-control-raspberry-pi)
- [Raspberry Pi Setup](documentation.md#raspberry-pi-setup)
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

```
git clone https://github.com/NTIG-Uppsala/elevhalsa-skylt.git
```

> Be sure to choose a directory that is not synced with OneDrive, Google Drive, or similar apps. Otherwise Jekyll will not work.

### Step 2 - Install WSL Ubuntu

- Go to the Control Panel → Programs → Programs and Feautures → Turn Windows features on or off

- Check the "Windows Subsystem for Linux" box (found near the bottom) and press OK. Restart the computer when prompted.

- Run the following in the Command Prompt: 

    ```
    wsl --install -d Ubuntu
    ```

- Follow the instructions shown on the screen

### Step 3 - Install Ruby and Jekyll

Open an Ubuntu (WSL) terminal and navigate into the cloned repository's folder. Run the following:

```
sudo apt update ; sudo apt install ruby-full build-essential zlib1g-dev ; echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc ; echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc ; echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc ; sudo gem install jekyll bundler 
```

### Step 4 - Python setup

#### Install Python

```
sudo apt update && sudo apt install python3 python3-pip
```

#### Python virtual environment

##### Create a Python virtual environment

In the cloned Git repository, run:

```
python3 -m venv .venv
```

##### Activate the virtual environment

If on Windows use the following command:

```
./.venv/Scripts/activate
```

If on Linux:

```
source ./.venv/bin/activate
```

**Note:** the virtual environment should be activated when running Python scripts

##### Exit virtual environment

To exit the virtual environment, enter `deactivate` into the terminal.

#### Install dependencies

Before installing the dependencies, make sure to [activate](documentation.md#activate-the-virtual-environment) the Python virtual environment.

```
cd ~/Git/elevhalsa-skylt
```

```
python3 -m pip install -r scripts/requirements.txt
```

### Step 5 - Add Google service account credentials

Download the file [service_account_credentials.json](https://drive.google.com/file/d/177ZQ10REm72G-kb8c3xZvUWBMFjTJQYq/) and put it in the root directory of the cloned repository on your computer.

> The Google service account API credentials are not stored in the GitHub repository for security reasons.

### Step 6 - Add .env file

This project requires a `.env` file. To create one, make a new file in your directory and name it `.env`. For users who have access to the corresponding [Google Drive](https://drive.google.com/drive/folders/1PE9KzvEw8aPh5E4z1SYBZf03GJ8k5gWZ), a ready-to-use `.env` file can be found there.

The contents of the `.env` file is

```
sheet_id = SPREADSHEET_ID
```

where `SPREADSHEET_ID` can be found in the Google Sheets sheet's URL.

### Step 7 - Running it

Before running the script, make sure to [activate](documentation.md#activate-the-virtual-environment) the Python virtual environment.

Get CSV and image data by running `scripts/main.py` with Python:

```
python scripts/main.py
```

Run the following command to build and serve the Jekyll site locally:

```
jekyll serve -s site --config _config.yml
```

## Tests

See [tests_info.md](../tests/tests_info.md) for information regarding installation of dependencies and running tests.

## Keeping the repo up to date in the Raspberry Pi

- Code locally, either on a development Raspberry Pi or on your personal computer
- Push to the Github repo
- Pull from the main branch on the Raspberry Pi

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

### Enable Remote Control

To be able to control your raspberry's graphical interface remotely, follow these steps.
1. Open the Command Line Interface and enter the following commands:

    ```
    sudo apt-get update
    ```

    ```
    sudo apt-get install realvnc-vnc-server
    ```

    ```
    realvnc-vnc-viewer
    ```

2. Write this command:

    ```
    sudo raspi-config
    ```

3. Navigate to Interfacing Options and enable VNC

## Raspberry Pi Setup

### Install Raspberry Pi OS

Follow the instructions [here](https://www.raspberrypi.com/software/)

### Clone Repository

To start configuring your Raspberry Pi, create a directory named "Git"
```
mkdir ~/Git
```
Change active directory to the Git directory with the command:

```
cd ~/Git
```

and then clone the git repository with the command:

```
git clone https://github.com/NTIG-Uppsala/elevhalsa-skylt
```

### Change Resolution

To change the resolution of the Raspberry Pi outputs, open cmd > ssh to desired pi > run `sudo raspi-config` > choose "2 Display Options" > "D1 Resolution" > choose a resolution (Default is 1360x768) 

### Installing Ruby, Jekyll, and Python

See [above](documentation.md#step-3---install-ruby-and-jekyll) on how to install Ruby and Jekyll.

See [above](documentation.md#step-4---install-python-and-dependencies) on how to install Python and required dependencies.

### Add Google service account credentials

Download the file [service_account_credentials.json](https://drive.google.com/file/d/177ZQ10REm72G-kb8c3xZvUWBMFjTJQYq/) and put it in the root directory of the cloned repository on the Raspberry Pi.

> The Google service account API credentials are not stored in the GitHub repository for security reasons.

### Add .env file

See [above](documentation.md#step-6---add-env-file)

## Set Up Autostart

Follow these steps to ensure that the website automatically displays on the Raspberry Pi after it starts.
The commands should be run on the Raspberry Pi.

1. Open the Command Line Interface and type in the following command:

    ```
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
    ```

2. Add the following line at the bottom:

    ```
    bash /home/exampleuser/Git/elevhalsa-skylt/scripts/on_startup.sh
    ```
    Replace the "exampleuser" with the name of the Raspberry Pi's username.

3. Open the Command Line Interface and type in the following command:

    ```
    sudo nano /etc/systemd/system/jekyll.service
    ```

4. Write this into the editor, make sure to replace `exampleuser` with the user of your Raspberry Pi, and then save and exit:

    ```
    [Unit]
    Description=Jekyll service
    After=syslog.target
    After=network.target

    [Service]
    # Name of the user account that is running the Jekyll server
    User=exampleuser
    Type=simple
    # Location (source) of the markdown files to be rendered
    ExecStart=sudo jekyll serve -s /home/exampleuser/Git/elevhalsa-skylt/site --config /home/exampleuser/Git/elevhalsa-skylt/_config.yml
    Restart=always
    StandardOutput=journal
    StandardError=journal
    SyslogIdentifier=jekyll

    [Install]
    WantedBy=multi-user.target
    ```

5. Type the following command into the Command Line Interface:

    ```
    sudo systemctl enable jekyll.service
    ```

The jekyll serve command is in a system service and not in `on_startup.sh` because it does not work when placed in `on_startup.sh`.

Commands in `autostart` are processed in a parallel fashion, so commands do not wait for previous commands to finish. More about this [here](https://forums.raspberrypi.com/viewtopic.php?t=294014).
For this reason, the commands are put in `on_startup.sh` instead, and the autostart file just runs `on_startup.sh`.

## Change active display times

1. Open the Command Line Interface and enter the following command:

    ```
    crontab -e
    ```

2. Type 1 to choose nano as your editor.
3. Go to the bottom of the opened document and type in the following commands:

    ```
    * * * * * sudo vcgencmd display_power 0
    * * * * * sudo reboot
    ```

Asterisk 1 = minutes (from 0 to 59)

Asterisk 2 = hours (from 0 to 24)

Asterisk 3 = day of month (from 1 to 31)

Asterisk 4 = month (from 1 to 12)

Asterisk 5 = day of week (0 - 7) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)

Example:

```
0 10 * * * sudo vcgencmd display_power 0
5 10 * * * sudo reboot
```

This will turn of HDMI output at 10:00 and start it again at 10:05.

## Create shortcut

1. Open the Command Line Interface and enter the following command:

    ```
    sudo nano /etc/xdg/openbox/lxde-pi-rc.xml file
    ```

2. Find the `<keyboard></keyboard>` tags and add the following text between the tags:

    ```
    <keybind key="">
        <action name="Execute">
            <command>
            </command>
        </action>
    </keybind>
    ```

3. Add the shortcut in the `<keybind>` tag and command you want to run between the `<command></command>` tags

    Example for running a bash script when Ctrl+F11 is pressed:

    ```
    <keybind key="C-F11">
        <action name="Execute">
            <command>
                bash ~/shortcut/close
            </command>
        </action>
    </keybind>
    ```

    C - stands for control

    A - stands for alt

    S - stands for shift

## Disable Black Border around Screen

1. Open the Command Line Interface and type the following command:

    ```
    sudo nano /boot/config.txt
    ```

2. Find the disable_overscan line and change it to:

    ```
    disable_overscan=1
    ```

## Remove Chromium offer to Translate Page

1. Open Chromium browser
2. Go to Settings > Advanced Settings > Language
3. Untick Offer to Translate Page checkbox
4. Exit Browser

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

## Hide Taskbar

1. Right-click on the taskbar and select `Panel Settings`
2. Click on the `Advanced` tab, and check `Minimize panel when not in use`

## Remove Screensaver

1. Open Command Line Interface and type in the following command:

    ```
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
    ```

2. Comment out `@xscreensaver -no-splash` using a hashtag at the beginning of that line.
3. Then add this line:

    ```
    @xset s off
    ```

4. Save and exit.

## Disable Raspberry Pi sleep mode

1. Open the Command Line Interface and type in the following command:

    ```
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
    ```

2. Add the following lines at the bottom:

    ```
    @xset -dpms
    @xset s noblank
    ```

## Remove Raspberry Icons

1. Open Command Line Interface and type in the following command:

    ```
    sudo nano /boot/cmdline.txt
    ```

2. In the editor, at the end of the line add:

    ```
    logo.nologo
    ```

## Replace Boot Image

1. Open Command Line Interface and type in the following command:

    ```
    sudo cp ~/my_splash.png /usr/share/plymouth/themes/pix/splash.png
    ```

## Change Background Image

1. Right-click on desktop and select desktop preferences.
2. Under the desktop tab, in the Picture setting, click on the folder next to Picture.
3. Navigate to `~/my_splash.png`, press open, then press ok.

## Hardware used

### Screen

- Name: Voxicon VXM232HD
- Size: 32 inches
- Resolution: 1360 x 768
- Touch screen: No
- Number of HDMI-ports: 2

### Raspberry Pi 4 Model B Rev 1.2
