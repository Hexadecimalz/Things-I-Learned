# Adding sudoers through `/etc/sudoers.d`

Simple sudo access. You can replicate sudoer permissions just like you would when editing the sudoers file. The benefit of this is that you can simply delete a file
to revoke access on the fly. This is useful when it comes to Ansible as well, since you could very easily create a file with permissions for a user and remove it as well. 

In Ubuntu this is turned on by default, but sometimes you might need to turn it on if it's been turned off in sudoers. 

## How It Works 
1. Create file with the user account name in `/etc/sudoers.d`
2. Edit the file with the user account name
sudo vim [user]
```
user ALL=(ALL:ALL) ALL
```
For passwordless
```
user ALL=(ALL) NOPASSWD: ALL
```
3. Save and exit the changes are now posted to sudoers. 

## Command only permissions 

You can set command only permissions in sudoers or is sudoers.d 

```
# Allow icebear to edit passwords for all users, except for  root
icebear ALL=/usr/bin/passwd, !/usr/bin/passwd *root*
# Allow icebear to shutdown localhost
icebear localhost=/sbin/shutdown -h now 
# Allow icebear to shutdown all machines 
icebear ALL=/usr/sbin/shutdown
# Allow icebear to poweroff all machines
icebear ALL=/usr/sbin/poweroff 
```

## Resources

[man sudoers](https://linux.die.net/man/5/sudoers)
