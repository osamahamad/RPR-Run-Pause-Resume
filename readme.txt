INRODUCTION:

When pen-testing login credentials it is often useful to be able to set a pause time after a specified number of test requests to avoid having the target site block the attack. Many websites implement network defences against such repeated login requests to prevent misuse and this often comes into play after the user has tried a set number of login attempts (eg 10 or 20 etc). The user, after a set period of not making any further requests (usually a few minutes to one hour), is often then permitted by the application to resume making credential-guessing requests.

This script allows BurpSuite Intruder to iterate through a list of passwords but with the ability to set pauses in the middle of the attack after a specified number of requests have been made. After each pause, the attack then resumes automatically.

For example this script can can run the first 20 username/password requests using a list of credentials, pause the script for 10 minutes, then carry on with the script from where it left off for the next 20 requests, pause for 10 minutes, run the next 20 requests etc etc until the whole list of credentials has been tried.


REQUIREMENTS:

A free or paid version of BurpSuite with Turbo-Intruder installed.


USAGE INSTRUCTIONS: 

Download the script1_0.py from this repo. Right click on the login request to be tested (either within the proxy tab in Burp or within the Intruder tab) and select Turbo Intruder which should open another window showing the request to be tested. In the top half of the Turbo-Intruder window (within the `Raw' tab) replace the password string by entering "%s" (without the quotes) e.g password=%s. On the bottom half of the same window you will see the default Turbo script. There you have to copy & paste the content of script1_0.py, replacing the whole content in this part of the window. Within the first lines of the pasted script you will see "#Parameters to configure", where you can edit the following:

triedWords=the number of words to try before pausing. Example usage: triedWords=20
timeMins=number of minutes to pause for. Example usage: triedMins=0
timeSecs=number of seconds to pause for. Example usage: triedSecs=5
throttleMillisecs=number of milliseconds to wait before each request. Example usage: throttleMillisecs=200
 
The script reads the password list from a .txt file which must be named `words.txt' and copied to the main BurpSuite directory (where the Burp exe file is located).

Click on `Attack' at the bottom of the Turbo window to execute the script.
Note this has only been tested on the `sniper' attack type within Burp Intruder. Some tweaking of the parameters described above may be needed to ensure this script works against the particular target to be tested.

