"SecureU (OPC) Private Limited"
" Make sure all permissions(Read and Write) are granted for Windows Registry"

import winreg

def block_usb_ports():
    """Blocks all USB ports on the system."""
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Services\USBSTOR",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(reg_key, "Start", 0, winreg.REG_DWORD, 4)
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"An error occurred: {e}")

def disable_bluetooth():
    """Disables Bluetooth on the system."""
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Services\BTHPORT",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(reg_key, "Start", 0, winreg.REG_DWORD, 4)
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"An error occurred: {e}")

def disable_command_prompt():
    """Disables the command prompt on the system."""
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Policies\Microsoft\Windows\System",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(reg_key, "DisableCMD", 0, winreg.REG_DWORD, 2)
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"An error occurred: {e}")

def block_website(website):
    """Blocks access to the specified website."""
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(
            reg_key,
            "ProxyServer",
            0,
            winreg.REG_SZ,
            f"{website} localhost:127.0.0.1"
        )
        winreg.CloseKey(reg_key)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    block_usb_ports()
    disable_bluetooth()
    disable_command_prompt()
    block_website("facebook.com")

if __name__ == "__main__":
    main()