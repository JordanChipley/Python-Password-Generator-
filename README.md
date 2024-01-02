 # Replit-Python-Random-Password-Generator
 
 Using the Visual Studio Code: Python Code for a Random Password Generator
==============

Run Command:

	python main.py <input file name>


Smart Backtracking Algorithm (MRV)
----------------------------------

Run Command:

	python main.py <input file name>

## Defining Your Problem:

![Snopf device](readme/snopf_header.jpg)

I recently had my password stolen online from a online gaming account. It turns out that the password that I picked for that account was not very strong, nor was it able to protect my account from getting hacked. I then came to the realization that I needed to find a way to come up with stronger passwords when it comes to the applications that I use.

So, I decided to design a random password generator using the coding langauge Python. I chose to use the the programing application Visual Code Studio when writing the random password generator. 

## Advantages of Snopf

* Very simple and robust design
* Easy to use
* You don't have to remember any passwords anymore (except preferably a master PIN for Snopf)
* Every password is unique and as strong as the accessed service allows
* The actual password creation is only happening on the USB device
* It is (under certain restrictions) possible to restore all passwords from a 24 word mnemonic representing the 256 bit secret
* It's more secure than a common pure software based password manager because the password creation is physically detached from the computer
* As Snopf emulates a regular keyboard, no passwords are stored in the clipboard

### Advantage over Common Software Password Managers
Common software password managers are very good tools to create and manage strong passwords for all your logins. Still, there is a possibility of your computer being remotely attacked and an attacker is able to access your password database getting all your login credentials.
Snopf is an improvement over these managers because an attacker can't access your Snopf token remotely. All passwords are derived from the secret on the device which an attacker must have phyiscal access to. So there is an additional *physical barrier* for an attacker.

![conventional_vs_Snopf](readme/conventional_vs_snopf.png)

## Using Snopf
A default request process for a password is pictured below, using the Snopf browser extension:

![request_process](readme/request_process.png)

To use Snopf two tools are currently available (an additional Android App is being developed), the *Snopf Manager* and a browser extension.

The Snopf Manager needs to be running on a computer when using Snopf. Beside managing the account table for snopf (see below) it also runs a background server for the browser extension. Whenever a password request is made in the browser, it is sent to the server which in turn talks to the USB device. The Snopf Manager minimizes to tray and runs silently in the background if you are not currently editing the account table. You can also create new entries in the account table from the browser extension.

![snopf manager screenshot](readme/screenshot_manager.png)

![snopf tool overview](readme/snopf_tools.png)

### Account table
With Snopf Manager you can create new entries, delete entries and change entries in the account table. A Snopf account table is a simple json with entries for every unique (service, account) combination. Each entry has six fields:

1. `Service` = Hostname or service name for the login, for example the email service `examplemail.com`
2. `Account` = Your account at this service, for example the email address for the email service `my_mail_address@examplemail.com`
3. `Password length` = The password length you set for this service
4. `Password iteration` = An integer for every unique (service, account) combination which you increase if you have to set a new password for this combination for example after a databreach at the used service.
5. `Rules` = Rules for password creation, for example 'The password must include a lowercase character'
6. `Keymap` = A keymap which will be used for the password creation which allows to include and exclude certain characters

The account table file is AES encrypted on the hard disk using the same master password (not to be confused with the secret on the USB device!) that is used whenever a password request is submitted.

![host_data_to_snopf](readme/host_data_to_snopf.png)


#### Setting the secret
You can change the secret on the Snopf device using Snopf Manager.

## Restoring passwords

To restore passwords, for example after losing or damaging Snopf, you need to be in possesion of the following data:

1. The Snopf's secret (comfortably as a 24 word mnemonic)
2. The optional master password (if you used one)
3. The account table

You might not absolutely need the account table if you have your logins, like email address and email service in your memory and just used passwords with default settings. Even if you need to remember *password iteration* you can just try out low numbers there.

Apart from that it is strongly advised to backup the account table and use a master password that you can remember. You should write down the 24 word mnemonic for the Snopf secret and store at a safe place.

With the above information you will be able to recreate all your passwords.


## Disclaimer
There is no warranty for data security and integrity or security issues of any kind. Care has been taken to make this a device that increases your security, however security bugs are possible.
