# Random-Tempature-Filler
A simple script using Python 3.5, Selenium and chromedriver to randomly fill up tempatures on any temptaking.ado site
Simply Fill Up the following to get started

List of users and the respective pins in order
```
#List of Users
userList = ("") #Enter your ID here
pwdList = ("") #Enter your Pin here
```

Executable path for Chromedriver and temptaking.ado link
```
#Creating Chrome Instance
browser = webdriver.Chrome(executable_path='', chrome_options=option) #Enter Executable Path Here
browser.get("") #Enter ADO Link Here
```

The script will continously loop till all the users in the user list is finished
