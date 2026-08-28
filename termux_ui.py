#!/usr/bin/env python3
import os
import sys

# Color definitions for terminal output
COLOR_RESET = "\033[0m"
COLOR_TITLE = "\033[1;36m"
COLOR_OPTION = "\033[1;33m"
COLOR_SUCCESS = "\033[1;32m"
COLOR_ERROR = "\033[1;31m"

TERMUX_COLOR_FILE = os.path.expanduser("~/.termux/colors.properties")
BASHRC_FILE = os.path.expanduser("~/.bashrc")
MOTD_FILE = "/data/data/com.termux/files/usr/etc/motd"

COLOR_SCHEMES = {
    "1": ("Monokai Dark", "#272822", "#f8f8f2", "#a6e22e"),
    "2": ("Dracula", "#282a36", "#f8f8f2", "#bd93f9"),
    "3": ("Matrix Green", "#000000", "#00ff00", "#003300"),
    "4": ("Nord", "#2e3440", "#d8dee9", "#88c0d0"),
    "5": ("Cyberpunk Yellow", "#101010", "#fcee0a", "#00f0ff")
}

def clear_screen():
    os.system("clear")

def print_banner():
    banner = f"""{COLOR_TITLE}
  ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗██╗
  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║██║  ██║██║
     ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║███████║██║
     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║██╔══██║██║
     ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██║██║
     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
                    Termux UI Customizer
{COLOR_RESET}"""
    print(banner)

def set_custom_name():
    name = input("\nEnter the custom name/title to display: ").strip()
    if not name:
        print(f"{COLOR_ERROR}Name cannot be empty!{COLOR_RESET}")
        return

    # Update MOTD (Startup Greeting)
    try:
        with open(MOTD_FILE, "w") as f:
            f.write(f"\nWelcome to Termux, {name}!\n\n")
        print(f"{COLOR_SUCCESS}[+] Startup banner updated successfully.{COLOR_RESET}")
    except PermissionError:
        print(f"{COLOR_ERROR}[!] Unable to write to {MOTD_FILE}. Run Termux as normal user.{COLOR_RESET}")
    except Exception as e:
        print(f"{COLOR_ERROR}[!] Failed to update MOTD: {e}{COLOR_RESET}")

    # Update PS1 prompt in .bashrc
    ps1_line = f'export PS1="\\033[1;32m{name}@termux\\033[0m:\\033[1;34m\\w\\033[0m\\$ "'
    
    lines = []
    if os.path.exists(BASHRC_FILE):
        with open(BASHRC_FILE, "r") as f:
            lines = f.readlines()
            
    # Remove existing PS1 exports set by this script
    lines = [line for line in lines if not line.startswith('export PS1=')]
    lines.append(f"\n{ps1_line}\n")
    
    with open(BASHRC_FILE, "w") as f:
        f.writelines(lines)

    print(f"{COLOR_SUCCESS}[+] Command prompt (PS1) updated successfully.{COLOR_RESET}")

def apply_color_scheme():
    print("\nSelect a Color Scheme:")
    for key, (scheme_name, bg, fg, cursor) in COLOR_SCHEMES.items():
        print(f" {COLOR_OPTION}[{key}]{COLOR_RESET} {scheme_name}")
        
    choice = input("\nSelect choice (1-5): ").strip()
    if choice not in COLOR_SCHEMES:
        print(f"{COLOR_ERROR}Invalid choice!{COLOR_RESET}")
        return

    _, bg, fg, cursor = COLOR_SCHEMES[choice]
    
    os.makedirs(os.path.expanduser("~/.termux"), exist_ok=True)
    
    properties = f"""background={bg}
foreground={fg}
cursor={cursor}
"""
    with open(TERMUX_COLOR_FILE, "w") as f:
        f.write(properties)

    # Reload Termux settings
    os.system("termux-reload-settings")
    print(f"{COLOR_SUCCESS}[+] Color scheme applied successfully.{COLOR_RESET}")

def main():
    while True:
        clear_screen()
        print_banner()
        print(f" {COLOR_OPTION}[1]{COLOR_RESET} Change Termux Display Name & Prompt")
        print(f" {COLOR_OPTION}[2]{COLOR_RESET} Change Color Scheme")
        print(f" {COLOR_OPTION}[3]{COLOR_RESET} Reload Termux Settings")
        print(f" {COLOR_OPTION}[4]{COLOR_RESET} Exit")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == "1":
            set_custom_name()
            input("\nPress Enter to return...")
        elif choice == "2":
            apply_color_scheme()
            input("\nPress Enter to return...")
        elif choice == "3":
            os.system("termux-reload-settings")
            print(f"{COLOR_SUCCESS}[+] Termux reloaded.{COLOR_RESET}")
            input("\nPress Enter to return...")
        elif choice == "4":
            print("\nExiting TermuxUI. Restart your shell to see all prompt changes!")
            sys.exit(0)
        else:
            print(f"{COLOR_ERROR}Invalid selection.{COLOR_RESET}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
      
