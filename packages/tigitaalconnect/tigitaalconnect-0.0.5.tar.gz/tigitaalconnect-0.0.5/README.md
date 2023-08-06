# **TigitaalConnect**
The official Python Library to connect with the TigitaalAPI! This library helps easily send requests
to the API, so you dont have to do the hard work of manually setting up requests.
Use a range of easy-to-use functions and explore the endless posibilities of the TigitaalAPI with 
TigitalConnect!


## INSTALLATION:

`pip install tigitaalconnect`


## SETUP:

### UserConnect: 
```python
from  tigitaalconnect import UserConnect
user = UserConnect(username, password)
# Enter your username and password in the parantheses
```

# REQUESTS:

## Reload Request:
```python
user.reload()
```
## ReloadAdvanced Request: 
```python
user.reloadadvanced()
```
## PFP Request:
```python
user.pfp(fileid)
```
## Nickname Request:
```python
user.nickname(new_nickname)
```
## Mail Request:
```python
user.mail(new_email)
```