# ☕ Mount a Windows Fileshare in Windows Subsystem Linux (WSL)

Linux is a nice way to check filesystem integrity and run checksums on files easily. In Windows for some reason knowing a file is borked or wanting to hash it will cost
you some extra Microsoft money. One example of how this is used is to be able to traverse a directory to find corrupted files in a share.

## How can we mount a fileshare in Windows?
1. Make a mountpoint `mkdir /mnt/m` or whatever or wherever you want your mount to be. 
2. `sudo mount -t drvfs '//PATH' /mnt/m`
3. You can probably setup a mount point in `/etc/fstab` as a `_netdev` entry so you can automount the drive. 
4. Okay, that's all folks 🐰
