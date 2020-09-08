# GlusterFS Notes 
This is for version 7. Gluster allows multiple disk volumes to be combined into 1 and to be shared across hosts.
The example I have written up is using 2x hosts, but more would be better, see split brain from RedHat in the references. 
## 💻 Installation 
```
sudo apt install software-properties-common
sudo add-apt-repository ppa:gluster/glusterfs-7
sudo apt update -y
sudo apt install glusterfs-server -y
sudo systemctl start glusterd && \
sudo systemctl enable glusterd && \
sudo systemctl status glusterd
sudo apt install zfsprogs -y
## Version check
glusterfsd --version
```

## 🔥 Firewall 
The firewall was a problem to be able to get pings to work between hosts and to get them to talk to each other. 
I highly recommend checking out this repo on github: https://github.com/geerlingguy/ansible-role-glusterfs Geerlingguy has created a slick Ansible role to do all of this, and setup firewall rules. 

## 📑 Modify Hosts File 
If you don't know where hosts is on Linux it's in `/etc/hosts` 
I've provided some dummy IPs, but you'll need to supply your own, as well as your own hostnames. I was using the hostname of the machine, but it doesn't matter too much. 
```
192.168.1.10 gfs01
192.168.1.11 gfs02
```
## 💾 Disks
Format all the disks as `xfs` I did this with fdisk. The disk list was as follows: `/dev/sd[b-h]` 

## 🧱 Create Mount Points 
Gluster relies on bricks to create a volume, so as I understand it each brick will build a volume in the end. 

**Perform this command on ALL GLUSTER SERVERS:** 
`mkdir -p /data/glusterfs/gvolume/brick{1..7}`

## 🖌 Create the Gluster Volume
I had problems at the prompt with Gluster not accepting line breaks in the command, so we have
this single liner. Also has trouble with iterating with bash {1..2}, so I don't recommend that either,
so we're stuck with ugly.

I have set this as a blockquote, rather than code, because we need line breaks. 

1. >gluster volume create gvolume replica 2 transport tcp gfs01:/
data/glusterfs/gvolume/brick1/brick gfs01:/
data/glusterfs/gvolume/brick2/brick gfs01:/
data/glusterfs/gvolume/brick3/brick gfs01:/
data/glusterfs/gvolume/brick4/brick gfs01:/
data/glusterfs/gvolume/brick5/brick gfs01:/
data/glusterfs/gvolume/brick6/brick gfs01:/
data/glusterfs/gvolume/brick7/brick gfs02:/
data/glusterfs/gvolume/brick1/brick gfs02:/
data/glusterfs/gvolume/brick2/brick gfs02:/
data/glusterfs/gvolume/brick3/brick gfs02:/
data/glusterfs/gvolume/brick4/brick gfs02:/
data/glusterfs/gvolume/brick5/brick gfs02:/
data/glusterfs/gvolume/brick6/brick gfs02:/
data/glusterfs/gvolume/brick7/brick force

2. **Start the Volume:** `gluster volume start gvolume`
3. **Mount the Volume:** `mount -t glusterfs gfs01:/gvolume /mnt/glusterfs`
4. **Get Info:** `gluster volume info gvolume`

## 🎢 AutoMount 
On ALL GLUSTER SERVERS setup `/etc/fstab` as follows: 
```
/dev/sdb /data/glusterfs/gvolume/brick1 xfs _netdev 0 0
/dev/sdc /data/glusterfs/gvolume/brick2 xfs _netdev 0 0
/dev/sdd /data/glusterfs/gvolume/brick3 xfs _netdev 0 0
/dev/sde /data/glusterfs/gvolume/brick4 xfs _netdev 0 0
/dev/sdf /data/glusterfs/gvolume/brick5 xfs _netdev 0 0
/dev/sdg /data/glusterfs/gvolume/brick6 xfs _netdev 0 0
/dev/sdh /data/glusterfs/gvolume/brick7 xfs _netdev 0 0
```

### Verify that it works
Unmount your volume and try 
```
mount -a
df -h
```

## 🚀 References
- https://access.redhat.com/documentation/enus/red_hat_gluster_storage/3.1/html/administration_guide/sect-managing_split-brain
- https://www.scaleway.com/en/docs/how-to-configure-storage-with-glusterfs-on-ubuntu/
- https://gist.github.com/githubfoam/edc4765a2bacbc2e44398e28bfce708b
- https://github.com/geerlingguy/ansible-role-glusterfs
