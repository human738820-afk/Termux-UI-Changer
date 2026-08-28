# Termux-UI-Changer
Step-by-step commands to copy and enter

1. Run the setup command:

pkg update && pkg upgrade -y                                                                                                                          
termux-setup-storage                                                                                                                                  
pkg install python ncurses-utils -y                                                                                                                   
pip install --upgrade pip                                                                                                                             

3. Create the file:
nano termux_ui.py

4. Copy-paste the code from termux_ui.py

5. Save and exit:
Press Ctrl + X, then Y, then Enter

6. Make the file executable:
chmod +x termux_ui.py

7. Run the tool:
python termux_ui.py
