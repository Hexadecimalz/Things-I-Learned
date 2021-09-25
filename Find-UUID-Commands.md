# 🛴 Find UUID Commands 

Here I have found some ways to find the UUID of a device, so it can be put into `/etc/fstab` the self-made challenge was to find a way to print the string `UUID="id.."`, mainly
because copy-paste on a large string is prone to error. 

```
# option #1 use d5w when in vim to remove the extra dev name 
blkid -s UUID /dev/device >> /etc/fstab

# option #2 
echo -e "UUID=\"$(lsblk -no UUID /dev/sde1)\"\t/mount\txfs\tdefaults\t0 0"

# option #3 🦅
blkid -s UUID /dev/sde1 | awk -F : '{print $2}'

# option #4 🦅 with awk 
echo -e "$(blkid -s UUID /dev/sde1 | awk -F : '{print $2}')\t/mount\txfs\tdefaults\0 0 "

# option #5 simplify the awk 🦅
echo -e "$(blkid -s UUID /dev/sde1 | awk '{print $2}')\t/mount\txfs\tdefaults\0 0 "
```
