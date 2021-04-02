# MacOS Tricks 

## 🖥 Verify SSH  On/Off status remotely and set it 
```
ssh systemsetup -getremotelogin 
ssh systemsetup -setremotelogin on 
# OR 
ssh systemsetup -setremotelogin off 
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
