# Automatically daily report of HIT
## Requirements
- [chromedriver](https://chromedriver.chromium.org/downloads) or [Edgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- Selenium
- Python3+

## Installation

- Install Chromedriver

    Chromedriver is an open source tool for automated testing of webapps across many browsers. 
    It provides capabilities for navigating to web pages, user input, JavaScript execution, and more.
    ChromeDriver is a standalone server that implements the W3C WebDriver standard. 
    ChromeDriver is available for Chrome on Android and Chrome on Desktop (Mac, Linux, Windows and ChromeOS).  
    Chromedriver can be download from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

    **You need to confirm your chrome verison** from the about page of chrome.

    unzip the chromedriver and move to the install directory of your chrome.

    **Add the Chrome to the PATH**

- Install python
    Download installer from the [python home page](https://python.org)

- Install Selenium via pip
    ```
    python3 -m pip install Selenium
    ```

## Usage
Modify the USERNAME and PASSWD with your hit_id username and password.
- test the python
    Run `python3 main.py id1 password1`
- run use a windows script
    Run 'auto.bat'
- add to the schedule tasks in windows.
    You can add a scheduled tasks to run the script at specify time!

