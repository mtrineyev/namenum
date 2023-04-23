# Name The Number Telegram bot
"Name the Number" telegram bot translates natural numbers as well as
powers of 10 into their nominal names and can convert binary,
octal and hex numbers to decimal

Written by @mtrineyev

Live bot @NameTheNumberBot

## Deployment and running
Installation and running process:
```bash
cd install_directory
git clone git@github.com:mtrineyev/namenum.git
cd namenum
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp settings.example settings.py
nano settings.py
python namenum.py
```
You can also start the bot in background:
```bash
nohup python namenum.py > /dev/null 2>&1&
```
You can find the process and its process ID with this command:
```bash
ps ax | grep namenum.py
```
If you want to stop the execution, you can kill it with the kill command:
```bash
kill PID
```

Have a nice journey :)
