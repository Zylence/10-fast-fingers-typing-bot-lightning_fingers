# Lightning-Fingers-typing-Bot

## CONTENTS:
[Introduction](https://github.com/Zylence/10-fast-fingers-typing-bot-lightning_fingers#introduction)

[Setup](https://github.com/Zylence/10-fast-fingers-typing-bot-lightning_fingers#setup)

[Walkthrough](https://github.com/Zylence/10-fast-fingers-typing-bot-lightning_fingers#walkthrough)

[Disclaimer](https://github.com/Zylence/10-fast-fingers-typing-bot-lightning_fingers#disclaimer)


## INTRODUCTION:

https://youtu.be/xk9nXOd2G-Y

I am happy to announce my first project ever! Lightning_fingers in an easy-to-use cheat/bot that can type for you on the [10-fast-figers website](https://10fastfingers.com/typing-test/). It was build around Python and popular Open-Source libraries such as Pytesseract and Selenium.

This Bot is meant to be LEGIT, so you can be playing in the leaderboards without getting banned. It has smart error feature and anti-anticheat build in. You can play multiplayer, competitions, everything! Everything it does is based around
probability so there are no repeating patterns! It'a inputting letters at once mimicing human typing. You could easily record videos of it and noone would notice!


![image](https://github.com/Zylence/10-fast-fingers-typing-bot-lightning_fingers/blob/main/Screenshots/operation.gif)

## BUILDING FROM SOURCE
In case you want to build the project from source, because you want to make own adjustments, this section is for you. In case you just want to use the precompiled biarny, skip to the [Setup Section](#SETUP) directly.
+ Install the dependencies via: `pip install -r requirements.txt`
+ To build the binary, in the project root, run: ` pyinstaller --onefile --noconsole --icon=./main/lightning_fingers.ico ./main/main.py --name lf`
+ Remove `--noconsole` for easier debugging of the binary. 
+ Tipp: use a new venv, this will make the resulting exe smaller by avoiding including unnecessary packages. 

## SETUP:

### Follow the instructions carefully... It may seem a little hard to setup, but once it's done you will appreciate it because you won't ever have to do this again. ;)
(A youtube video explaining the process may be linked soon...)

1.
   + To unlock the programs full capabilities you will have to go to the following [link](https://github.com/UB-Mannheim/tesseract/wiki) and download and install the tesseract-      ocr-w... setup exe that matches your Operating Systems Version(64 bit or 32 bit).

   + IMPORTANT: write down the path to the location where you install tesseract! You will need it. For most people it will look sth. like this:
     "C:\Users\YOUR_NAME\AppData\Local\Programs\Tesseract-OCR" (without " and YOUR_NAME replaced with your user name)


2. 
   + After you have done this you need to add tesseract to your "path variable". This can be done by pressing "win key" + "r" on your keyboard and then inputting
     "sysdm.cpl" inside the dialogue box that pops up. You press enter an then choose the "Advanced" tab in the upcoming window and click "Environment Variables" at the bottom.      Now in the "user variables" section you click "Path" once and choose "edit". You click on "New" and input the path which you saved somewhere earlier. That's it, you just        have to confirm everything by pressing "OK".


3. 
   + I recommend using [Google Chrome](https://www.google.com/intl/en_en/chrome/), it may not work with other browsers.


4. 
   + Now you download the precompiled exe from the ["Releases"](https://github.com/Zylence/10-fast-fingers-typing-bot-lightning_fingers/releases/latest). 


After running the exe you will need to wait a few seconds until your GUI as well as a browser instance are spawned. Once everything has started your firewall will ask you to allow the program. I advise to allow it, otherwise it may not work.


## Walkthrough:

You have made it congrats. Now it's time to enjoy the program ;)

As pointed out this program is meant to look legit. On the top right you can choose the "failure rate" at which smart typos will be made.
But I advise leaving it around 5 (that will be 5%).


### GO!
The buttons are tied to the input field above them and serve the following tasks:

#### Normal 
Meant for all the typing-stuff and challenges that are accessible directly from the main page of 10 fast fingers.

-> input wpm at the top -> input failure rate -> hit "GO!"

#### Multiplayer
A special mode for competitions where you go head to head with others.

-> input wpm at the top -> input failure rate -> hit "GO!"

#### Anti Anticheat
Once prompted to evaluate your result, click on the notification and head to the test.

-> input your desired wpm up top -> head over to the evaluation process -> click "Start" on the website -> click "GO!"

+ this may not work immediately. It's a little luck based if your system can read the picture. Just retry..

#### Stat Creator
Plays a user definable amount of games, slowly increasing wpm. This is meant to make your stats look more legit, but does not work particularly well, so you might as well skip it.

-> at the top input the wpm you wish to achieve -> input the number of games you want the system to play under "Stat Creator" -> click "GO!"

+ During this process (and any other as well) the program can run in the background, you don't have to waste any time watching it while this is running, simply minimize it and carry on with what you are doing.
+ The more you make it play the more legit it looks. Unless of course you let it play to much... I advise between 20 - 50 games to start with. But in the end its up to you what amount to input there.

+ NEVER use stat creator with less than 100 wpm (if you want up your final statistics to end up at 180, pick 180)!
+ ONLY use stat creator once!


### MODES:
"Rage Mode", "Dynamic Mode" and "Standard Mode" can be paired with any of the game modes! Simply select it before starting.

#### Rage Mode 
Inputs words with no delays and no errors. It enables speed up to 3000 wpm depending on your systems capabilities. This mode works well on low-end hardware, but be warned: Only use this if you are willing to get banned! The speed is not really controllable in this mode!

#### Dynamic Mode
Continuously compares your goal with the actual achievements, trying to mitigate random delays with slight increases (or decreases if it's too fast) This is the most accurate mode for achieving your desired results.

#### Standard Mode
Calculates the average time it needed per letter at the start, therefore it's the most legit looking, but less accurate in forms of desired wpm.


## HINT:

When playing on a low-end PC or laptop you can try inputting higher wpm numbers such as 300, 400 ... this will shorten the timing and may enable you to get higher speeds. 
But first try if you really need it!


## DISCLAIMER:

This program so far has only been tested on Win 10 64 Bit AMD Desktop Computers, It may not work on others. Due to its smart error features and it's goal to look legit it also may be a little slow on less powerful hardware especially in laptops. I am not accountable for anything you do using this software, this includes your account getting banned.
