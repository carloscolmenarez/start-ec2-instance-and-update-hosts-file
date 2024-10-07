import os
import sys
import win32com.client

BAT_FILE_NAME = "launch_py_script_start_ec2_instance.bat"
LNK_FILE_NAME = "Start EC2 Instance and update hosts.lnk"

def create_bat_file(bat_file_path, script_path):
    with open(bat_file_path, 'w') as bat_file:
        bat_file.write(f'@echo off\n')
        bat_file.write(f'python "{script_path}"\n')
        bat_file.write(f'pause\n')
    print(f"Batch file created at: {bat_file_path}")

def set_run_as_administrator(lnk_file_path):
    powershell_script = f"""
    $shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut("{lnk_file_path}")
    $shortcut.Save()
    $bytes = [System.IO.File]::ReadAllBytes("{lnk_file_path}")
    $bytes[21] = $bytes[21] -bor 0x20
    [System.IO.File]::WriteAllBytes("{lnk_file_path}", $bytes)
    """
    script_path = os.path.join(os.path.dirname(lnk_file_path), "set_admin.ps1")
    with open(script_path, 'w') as file:
        file.write(powershell_script)
    os.system(f'powershell -ExecutionPolicy Bypass -File "{script_path}"')
    os.remove(script_path)

def create_shortcut(lnk_file_path, target_path, working_directory):
    shell = win32com.client.Dispatch("WScript.Shell")

    shortcut = shell.CreateShortCut(lnk_file_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = working_directory

    icon_path = os.path.join(current_dir, "images", "icono-256.ico")
    shortcut.IconLocation = icon_path
    shortcut.save()

    set_run_as_administrator(lnk_file_path)

    print(f"Shortcut created at: {lnk_file_path}")

# EXECUTION STARTS HERE
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Create .bat file
    bat_file_path = os.path.join(current_dir, BAT_FILE_NAME)
    create_bat_file(
        bat_file_path,
        os.path.join(current_dir, "start_ec2_instance.py")
    )

    # Create .lnk file for desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    create_shortcut(
        os.path.join(desktop_path, LNK_FILE_NAME),
        bat_file_path, current_dir
    )
else:
    print("This script is intended to be executed directly.")
    sys.exit(1)