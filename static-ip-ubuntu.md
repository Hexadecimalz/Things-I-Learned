# 🤖 Set a Static IP in Ubuntu 

Located in `/etc/netplan/*.conf`
```
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens160:
      dhcp4: false
      addresses: [*.*.*.*/**]
      gateway4: *.*.*.*
      nameservers:
        addresses: [*.*.*.*]
  version: 2

```

To apply the change then run: 

`sudo netplan apply` 

## 🚀 Resources 
Source: https://linuxconfig.org/how-to-configure-static-ip-address-on-ubuntu-18-10-cosmic-cuttlefish-linux
