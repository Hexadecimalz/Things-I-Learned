# MacOS Tricks 

## 🖥 Verify SSH  On/Off status remotely and set it 
```
sudo systemsetup -getremotelogin 
sudo systemsetup -setremotelogin on
# OR 
sudo systemsetup -setremotelogin off 
```

## 🔐Remotely Encrypt through SSH 
```
ssh user@IP 
sudo su 
# Type username / type password 
fdesetup enable 
# Type username / password 
# Outputs 
# Recovery key = 'xxxx-xxxx-xxxx-xxxx-xxxx-xxxx'

# Test status 
fdesetup status 
```
Sometimes a reboot is necessary, but usually status will update to remote monitor right away. 

## macOS Shows Managed by Organization Erroneously
If System Preference shows a device is managed by an organization where it should not be, then try the below commands in terminal. 
```
sudo fdesetup removerecovery -institutional
sudo fdesetup changerecovery -personal
```
The second command should show the new backup key. 


- Source : [mac World](https://www.macworld.com/article/233872/can-t-enable-filevault-an-errant-set-of-files-may-be-blocking-you.html)
