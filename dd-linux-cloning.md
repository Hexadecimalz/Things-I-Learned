# © Cloning a FileSystem with `dd`

Some notes about copying an NVMe from a 512gb drive to a 4tb drive using Ubuntu, as well as the other most common use I've had for `dd`. Byte Size can make a difference in transfer rates, see the resources for more details. 

The `bs` indicator is very important in terms of speed. In cloisng 512gb on two separate occassions without `bs` indicator it took 3 hours to copy 512GB where as it took a little short of an hour to copy the same amount of data specifying `bs=1M`.

## ⚠ Disclaimer 

Don't try this without a backup. If you select the wrong disks you'll overwrite your data... 

## 💾 NVMe Drive Clone 

Recently I needed to do an OS clone to upgrade a 512GB to 4TB OS drive, but both disks were on NVMe. This was fairly easy to do in Ubuntu, but I noticed a hiccup with the bios settings,
which was worth noting. An easy way to remember this command is to remember that if = input file and of = output file. 

**How to get this done:**
1. 🛠 **Tools:** Keep the host OS drive mounted in place, and connect the second NVMe drive through a USB interface. We need to boot into an external Ubuntu live USB. 
2. In the BIOS, if Intel Rapid Store Technology (RST) is on, you will need to disable it and change over to AHCI. 
3. When booting back into the drive choose `AHCI` in the BIOS. The drive will fail to boot and eventually get to the 'Advanced Options' menu choose to boot into safe mode with networking. Login and give it a bit of time, but then perform a reboot and things should work on the next reboot without problem.  
4. Identify your disks `lsblk -t` or `fdisk -l`. Nvme drive will show up in a very particular way, which makes the following commands easier. 
NVMe will only identify drives mounted through the motherboard or a PCI card.  
4. NVMe partitions are named `nvme0n1p1, nvme0n1p2` so we see a few partitions coming from our origin drive, and can identify it as the OS drive, since we know it has a few parititions. 
5. The second NVMe drive is mounted through USB, so it's not given the NVMe name, since it's just considered a USB device by the system. 
6. Run the command to begin the clone `sudo dd if=/dev/nvme0n1 of=/dev/sdb bs=1M status=progress`  
7. Wait a few hours.  
8. Check in disk manager that the full drive size is being used and if not, don't forget to expand the volume. 

## 📂 Use `dd` to create files of various sizes

We can use `dd` to create files of a random size using `/dev/urandom`. This is just a side note about using `dd` in another context though. 

For example: 
```
dd if=/dev/urandom of=./hello bs=10M count=5 status=progress
5+0 records in
5+0 records out
52428800 bytes (52 MB, 50 MiB) copied, 0.055782 s, 940 MB/s
```

`status=progress` is a useful option to output what's happening, and especially useful when cloning large volumes. 

## 🚀 Resources 
- https://linux.die.net/man/1/dd
- https://snapshooter.io/blog/how-to-clone-your-linux-harddrive-with-dd 
- https://www.reddit.com/r/pop_os/comments/erzbnm/linux_cant_find_my_m2_pcie_nvme_ssd/
- https://superuser.com/questions/234199/good-block-size-for-disk-cloning-with-diskdump-dd
