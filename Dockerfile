from archlinux:base-devel
workdir /app
run mkdir ./tmp
run pacman -Syu --cachedir ./tmp python-pip git --noconfirm
run rm -rf ./tmp
copy . .
run pip install --upgrade pip
run pip install -r ./requirements.txt
cmd ["python","./bot.py"]
