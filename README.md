# File-Integrity-Checker

*COPAMY*: CODTECH IT SOLUTIONS

*NAME*: PADMAKAR SUBHASH MORALE

*INTERN ID*:  CTIS1717

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

# File Integrity Checker – Project Description

1.

We live in a world where computersre a big part of our daily lives. So it is very important that the information on our computers is safe and sound. Sometimes the files on our computer can get changed on purpose or by accident because of software people getting in who should not problems with the programs or mistakes that people make. Even a tiny change to a file can cause big problems, with safety. That is why we use a **File Integrity Checker (FIC)** to check our files.

The **File Integrity Checker** project is a program that uses Python to keep an eye on files. It checks if someone made any changes to these files without permission.

The program does this by figuring out codes for each file called hash values and then comparing them to the codes it stored earlier.

If the codes do not match, the **File Integrity Checker** tells us what happened to the file. If it was **modified deleted, added or unchanged**. This helps us know if something is wrong, with our files. The project is made as a *Windows desktop application**. This means it has a graphical user interface, which people call GUI for short. The graphical user interface makes the **Windows desktop application** easy to use and good, for work.

 2. Objective of the Project

The main objectives of this project are:

* To ensure **file integrity** by detecting unauthorized changes in files.

* To develop a **secure and reliable monitoring system** using cryptographic hashing.

* To provide a **user-friendly Windows application** instead of a command-line tool.

* To demonstrate the practical use of **Python libraries** for security applications.

* To convert a Python program into a **standalone Windows application (.exe)**.

3. Working Principle of File Integrity Checker

The File Integrity Checker is based on the idea of comparing **hash comparison**. So what is a hash value? It is like a code that is always the same length and it is made from the things that are, inside a file. This special code is made using a code maker called a cryptographic hash function. For this project the File Integrity Checker uses the SHA-256 hashing algorithm to make these codes or **hash comparison** to check files.

This is how things work:

1. When the application does the scan it figures out the hash values of every single file that is, in the directory that you picked.

2. The hash values are kept safe in a file called hashes.json. This file is a kind of file that uses something called JSON to store the hash values. The hash values are what is stored in this hashes.json file.

3. When the program does scans it figures out the hash values of those same files again. The program recalculates the hash values of the files which're the same files it looked at before. This means the application checks the hash values of the files every time it does a new scan.

4. Now the system looks at the hash values and checks them against the hash values that are already stored. The new hash values are compared to the stored hash values to see if they match.

5. Based on the comparison, the application identifies:

* Modified files

* Deleted files

* Newly added files

* Unchanged files

If the hash values are different that means the file content has changed. This is a sign that something might be wrong with the file like someone or something messed with it. The hash values are like a code for the file content so if that code does not match then the file content is not the same. This is a problem because it means the integrity of the file is, at risk and that is why it is called an integrity violation of the file.
 4. Libraries Used in the Project
 4.1 hashlib Library

The hashlib library is what we use to do hashing. This library gives us some ways to hash things, like MD5, SHA-1 and SHA-256. For this project we are using **SHA-256** because SHA-256 is more secure and reliable, than the others. We like SHA-256 because it helps keep our information safe.

Functions of `hashlib` in this project:

* Generates a unique hash value for each file

* Detects even a single-byte change in file content

* Ensures data integrity through cryptographic techniques
 4.2 os Library

The `os` library is really useful because it lets us work with the operating system. We use the `library to get to files and directories and paths. This is great because the `os` library works the way, on different operating systems.

Functions of `os` in this project:

* Traversing directories using `os.walk()`

* Handling file paths using `os.path.join()`

* Checking file existence

* Scanning all subdirectories and files

4.3 json Library

The `json` library is really useful for storing and retrieving hash values in a way that makes sense. The `json` format is simple and easy to understand which is why people, like it. It is also pretty lightweight which means it does not take up a lot of space. It is easy to manage the `json` files.

Functions of `json` in this project:

* Saving file hash values permanently

* The computer is now loading the stored hash values so it can compare them to the ones.

* Maintaining key-value pairs (file path : hash value)
 4.4 tkinter Library

The tkinter library is what Python uses to make the interface of a program that people can see and interact with. This tkinter library is really good, for designing the frontend of the application, which's the part that users will actually see when they use the application.

Functions of `tkinter` in this project:

* Creating windows, buttons, labels, and text areas

* The program lets users look through and pick the directories they want to use. This means users can choose the directories they need and the program will let them browse and select directories easily.

* Displaying scan results in a graphical format

* Showing popup messages for success or error
4.5 threading Library

The `threading` library is really useful for making our application more responsive. Things like scanning files and hashing them take a lot of time. If we do these things on the part of our interface it can make the whole interface stop working. This is why we use the `library. It helps us keep our application running while the `threading` library does the heavy work, in the background.

Functions of `threading` in this project:

* Running file scanning in a background thread

* Keeping the GUI responsive during long operations

* Improving user experience
 5. Features of the Project

The File Integrity Checker application does a lot of things for us. It has features. The File Integrity Checker application is very useful because it provides the following features:

* The File Integrity Checker application checks files to see if they are good or not

* The File Integrity Checker application helps us to know if someone changed our files

* The File Integrity Checker application gives us reports about our files. What is happening to them

The File Integrity Checker application is a big help, to people who use computers and need to keep their files safe. The File Integrity Checker application is something that we can use every day to check our files.

* **Directory Selection**: People can choose any folder they want to keep an eye on.

* **Hash-Based Verification**: Uses SHA-256 for secure integrity checking.

* **Change Detection**: This thing looks at files. Figures out which ones have been modified, which ones have been deleted, which ones are new and which ones are still the same as they were before. It checks the files to see what has happened to them like if they have been changed, removed or added or if they are still unchanged. The **Change Detection** does this to keep track of the files.

* **Persistent Storage**: This is where the system saves the hash values so it can use them for comparisons on. The **Persistent Storage** is really useful because it keeps all the hash values in one place. The system can look at the **Persistent Storage** and compare the old hash values, with the new ones.

* **Graphical User Interface**: Easy-to-use Windows GUI.

* **Responsive Application**: Uses multithreading to avoid freezing.

* **Desktop Application**: Converted into a standalone Windows executable.
 6. Backend and Frontend Implementation
 6.1 Backend Implementation

The backend of the project is where all the logic, for scanning files and checking if they are okay is done. It has lots of functions that do things like:

* Calculate file hash values

* Scan directories recursively

* Load old hash values from JSON file

* Compare old and new hash values

* Generate a structured result dictionary

The backend is made to work on its own so it does not need the GUI to function. This means the backend and the GUI are separate which makes the backend and the GUI easier to maintain and the backend and the GUI can handle work.
6.2 Frontend Implementation

The frontend of the program is made using Tkinter. This frontend provides:

* Input fields for directory selection

* Buttons to start integrity checks

* This is where we show the results of the scan

* Dialog boxes for notifications

The frontend talks to the backend. It does this by calling the integrity check function. Then it shows us the results that the integrity check function gives back to the frontend. The frontend is really good, at displaying these results from the integrity check function.
 7. Making the Application (Python to Windows App)

I used a tool called **PyInstaller** to turn my Python program into a Windows application. This **PyInstaller** thing is really cool because it puts everything I need like the Python interpreter and libraries and my source code into one file that I can run on Windows.

Implementation steps:

1. Developed and tested the Python backend and frontend.

2. Integrated frontend and backend modules.

3. Added multithreading to improve responsiveness.

4. Created an application icon (`.ico`).

5. Used PyInstaller command:

pyinstaller --onefile --windowed --icon=app_icon.ico app_gui.py

6. Generated a standalone `.exe` file.

7. Created a desktop shortcut to use the application easily.

This process made it possible for the application to work on Windows systems without needing to have Python installed on the computer. The application can run on Windows systems without requiring Python installation.
 8. Applications of the Project

The File Integrity Checker is really useful, in lots of situations that happen in life:

* Detecting malware or virus attacks

* Monitoring system and configuration files

* Digital forensics and investigations

* Protecting sensitive documents

* Server and network security monitoring

* Academic and educational security projects

 9. Other Methods Used in File Integrity Checking

Apart, from hash-based methods there are some ways to do things. These other techniques include:

* Digital signatures

* Checksum verification

* File permissions and access control

* Real-time monitoring tools

* Intrusion detection systems (IDS)

Cryptographic hash-based integrity checking is really good, at making sure things are safe. It is used by a lot of people. This method is one of the ways to check if something is okay or not and that is why cryptographic hash-based integrity checking is so popular.

10.

The File Integrity Checker project successfully demonstrates how Python can be used to build a practical security application. By combining cryptographic hashing, file system traversal, GUI development, and application packaging, this project provides a complete solution for monitoring file integrity. The project not only enhances understanding of cybersecurity concepts but also offers hands-on experience in developing real-world desktop applications. This makes it suitable for academic submissions, mini-projects, and practical demonstrations

