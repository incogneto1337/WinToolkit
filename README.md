# WindowsToolkit

## Overview

This tool provides a comprehensive suite of functionalities for extracting various types of information from a mounted Windows partition. It supports operations such as mounting partitions, extracting user information, dumping passwords, retrieving browser data, and more. The tool is designed for use in a Linux environment where Windows partitions are accessible.

## Features

- **Mount Windows Partition:** Mounts a Windows partition to a specified directory.
- **Extract User Information:** Extracts user information and password hashes from the Windows registry.
- **Dump Passwords with Mimikatz:** Runs Mimikatz for password dumping.
- **Retrieve Browser Passwords:** Extracts saved passwords from Google Chrome and Mozilla Firefox.
- **Retrieve Wi-Fi Passwords:** Extracts saved Wi-Fi passwords.
- **Retrieve System Information:** Retrieves system information from the Windows partition.
- **Dump Browser History:** Dumps browser history from Google Chrome and Mozilla Firefox.
- **List Installed Applications:** Lists installed applications.
- **Capture Screenshot:** Captures a screenshot of the current desktop.
- **Retrieve Windows Product Keys:** Extracts Windows product keys.
- **Extract User Account Details:** Extracts user account details from the Windows registry.
- **Extract Network Configuration:** Extracts network configuration details.
- **Extract Startup Programs:** Extracts startup programs information.
- **Extract Event Logs:** Extracts Windows event logs.
- **Remove User Password:** Removes a user's password.
- **Add Admin User:** Adds a new administrative user to the system.

## Requirements

- **Python 3:** Ensure Python 3 is installed.
- **ntfs-3g:** Required for mounting NTFS partitions.
- **mimikatz:** Needs to be available for password dumping.
- **sqlite3:** Required for dumping browser history.
- **wine:** Required to run Mimikatz if used on a non-Windows system.
- **chntpw:** Required for registry editing operations.

## Installation

1. **Install Dependencies:**
   ```bash
   sudo apt-get install python3 ntfs-3g wine sqlite3 chntpw
   ```

2. **Download and Configure Mimikatz:**
   - Download Mimikatz from its official repository.
   - Ensure it is executable and available in your PATH.

3. **Save the Script:**
   - Save the script to a file, e.g., `wintoolkit.py`.

## Usage

1. **Run the Script:**
   ```bash
   python3 wintoolkit.py
   ```

2. **Select an Option:**
   - Follow the menu prompts to select and execute the desired functionality.

## Menu Options

- **1. Mount Windows Partition:** Mounts the specified Windows partition.
- **2. Extract User Information:** Extracts user information and password hashes.
- **3. Dump Passwords with Mimikatz:** Dumps passwords using Mimikatz.
- **4. Retrieve Browser Passwords:** Retrieves saved passwords from browsers.
- **5. Retrieve Wi-Fi Passwords:** Extracts saved Wi-Fi passwords.
- **6. Retrieve System Information:** Retrieves system information.
- **7. Dump Browser History:** Dumps browser history from Chrome and Firefox.
- **8. List Installed Applications:** Lists installed applications.
- **9. Capture Screenshot:** Captures a screenshot of the current desktop.
- **10. Retrieve Windows Product Key:** Retrieves the Windows product key.
- **11. Extract User Account Details:** Extracts user account details.
- **12. Extract Network Configuration:** Extracts network configuration details.
- **13. Extract Startup Programs:** Extracts startup programs information.
- **14. Extract Event Logs:** Extracts Windows event logs.
- **15. Remove User Password:** Removes a specified user's password.
- **16. Add Admin User:** Adds a new administrative user.
- **17. Exit:** Exits the script.

## Notes

- Make sure you have the necessary permissions to perform these operations.
- Use responsibly and ensure compliance with all relevant laws and regulations.

## License

This tool is provided for educational and research purposes only. Use responsibly and in accordance with the law.

---

Feel free to modify or expand this README as needed!
