from python:3
workdir /app
copy . .
run pip install --upgrade pip
run pip install -r ./requirements.txt
cmd ["python","./dc\ bot.py"]
