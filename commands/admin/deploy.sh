# /bin/bash

cd /home/python_stuff/ccr/ccr_venv/bot
git pull

screen -S ccr -X stuff '^C'
screen -S ccr -X stuff 'python3 main.py'

screen -XS ccr-deploy quit