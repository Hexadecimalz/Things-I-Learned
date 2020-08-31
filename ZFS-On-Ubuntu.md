# 💻 Things I Learned about ZFS on Ubuntu
The theoretical upper limit of files in any one directory is 2^48 (from Wikipedia).

Maximum 256 Quadrillion Zettabytes storage (itsfoss.com).

ZFS feels like an alien storage system, because it combines the file-system and volume manager into pools (itsfoss.com). 

The ZFS filesystem incorporates checking of the filesystem to verify its integrity, and can easily create parity compared to others tools in Linux such as MDADM. I created my first RAID in MDADM and it was simple, but time-consuming to format the disk for RAID and get everything online. Whereas ZFS pools can be created and destroyed with ease. 

Snapshots allow for a full or incremental backup. There are many utilities in Linux to manage snapshots. I found one that the documentation was fairly good for, but this was for a localhost backup, and not being backed up to an external server due to the quantity of data being very high. 

## What I Installed 
```
sudo apt install zfsutils-linux -y
# Ansible is not necessary, but useful.
sudo apt install ansible -y
sudo apt install python3-pip
pip3 install --upgrade zfs-autobackup
```

## 🗄 RAID 0 Configuration
```
zpool create -f data /dev/sd[b-f]
```

## 🗃 Raid 10 Configuration
```
zpool create backup\
mirror /dev/sd[g-h] \
mirror /dev/[sd[i-j]
```

### Enable Compression on `backup` pool 
`zfs set compress=lz4 backup`

Rationale: https://www.servethehome.com/the-case-for-using-zfs-compression/ 

#### Verify Compression
`zfs get compression backup`

## 🕚 Automating the Backup Schedule 

**Source:** github.com/psy0rz/zfs_autobackup 

### Set the Pool to be Backed up 
1. `sudo zfs set autobackup:zback=true data`
**Verify that the result is true**
2. `zfs get -t filesystem,volume autobackup:zback`

### Running Auto Backup Manually 

`sudo zfs-autobackup zback backup --progress --verbose`

This will create a snapshot on the target AND on the source. 

### Setup a Cron Job to Run Automatic Backup 
Setup as `root` crontab. 
```
sudo crontab -e
## Edit
@midnight sudo zfs-autobackup zback backup --progress --verbose --keep-source 1
```

Run a job at midnight to backup `data` pool, keep only the latest backup on the source drive. 

## 📸 ZFS Snapshot Management

### Remove All Snapshots 
`sudo zfs destroy -rv [pool]@%`

### List Snapshots 
`sudo zfs list -t snapshot`

### Restore a Backup 
1. Find the snapshot to restore `zfs list -t snapshot`
2. Create a new ZFS pool to restore to `sudo zpool create nv4tb /dev/nvme0n1p1`
3. Perform the restore: 
```
sudo zfs send backup/data@[snap] | sudo zfs recv -F [pool]/restore
```

### Destroy a Pool
`sudo zpool destroy [pool]`

### Import a Pool 
If the ZFS pool does not automount 
`sudo zpool import [pool]` 

### Import disks on a new system/reinstall

`zpool import -f [pool]`

## 🎁 ZFS Extras 

- Check Status: `zpool status`

- Create Different Datasets in a Pool: 
```
sudo zfs create data/someone
sudo zfs create data/images
```

## 🛰 Sources
- https://en.wikipedia.org/wiki/ZFS
- https://itsfoss.com/what-is-zfs
