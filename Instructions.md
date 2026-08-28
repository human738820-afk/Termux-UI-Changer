# Termux-UI-Changer
Step by step commands to copy and enter 
# 1
# Update packages and grant storage access
pkg update && pkg upgrade -y
termux-setup-storage

# Install Python and essential utilities
pkg install python ncurses-utils -y

# Optional: Ensure pip is up-to-date
pip install --upgrade pip
# 2
mkdir termux_ui.py
# 3
nano termux_ui.py
# 4
copy-paste the code from the file termux_ui.py
# 5
click Ctrl then x y then enter 
# 5
chmod +x termux_ui.py
# 6
python termux_ui.py
