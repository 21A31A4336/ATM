Bank Account Management System
This Python script provides a simple command-line interface for managing bank account operations such as withdrawal, deposit, balance inquiry, and password change. The script includes user authentication via username, password, and PIN.

Features
User Authentication:
Validates username, password, and PIN.
Allows three attempts for password entry before blocking the account.
Password Strength Check:
Ensures the password contains uppercase, lowercase, digit, and special characters.
Recommends adding missing character types or increasing password length if it's too weak.
Bank Operations:
Withdrawal: Checks balance before allowing withdrawal and updates the balance accordingly.
Deposit: Adds the deposited amount to the balance.
Balance Inquiry: Displays the current balance.
Password Change: Allows users to update their password after validating the current password and ensuring the new password is strong.
Usage
User Login:

Enter your username. If the username is invalid, the script exits.
Enter your password. You have three attempts to enter the correct password before the account is blocked.
Enter your PIN. If the PIN is incorrect, the script exits.
Bank Operations Menu:

After successful login, choose an operation from the following options:
Withdrawal
Deposit
Balance Inquiry
Change Password
Withdrawal:

Enter your PIN for verification.
Enter the amount to withdraw. If the amount exceeds the available balance, an error message is displayed.
Deposit:

Enter the amount to deposit.
Enter your PIN for verification.
The new balance is displayed after the deposit.
Balance Inquiry:

The current balance is displayed.
Change Password:

Enter your current password for verification.
Enter and re-enter the new password. The script checks the strength of the new password using the passcheck function. If the password is weak, recommendations for strengthening it are provided.
Example
***********************************
python
Copy code
# Run the script
python bank_account_management.py

# Sample interaction
enter your username: divya
enter your password: D
enter your pin: 8055
choose one
1.withdrawal
2.deposit
3.balance
4.change password
1
enter your pin: 8055
enter amount to withdraw: 500
available balance: 1525
*****************************************
Code Explanation
passcheck(x): Function to check password strength. It ensures the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character. It also checks the length of the password.
User Data: Hardcoded lists for usernames, passwords, PINs, and balances.
Main Program: Handles user input for username, password, and PIN. Provides options for withdrawal, deposit, balance inquiry, and password change.
Note
This script is intended for educational purposes and demonstrates basic concepts of user authentication and simple banking operations. In a real-world application, user data should be securely stored and managed, and the script should handle exceptions and edge cases more robustly.

