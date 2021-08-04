# Linux CUDA Installation 

This is a cheatsheet mainly for myself. Sorry for the poor formatting. 

## For Installation on a VM
- [Cheat Sheet](https://gist.github.com/wangruohui/df039f0dc434d6486f5d4d098aa52d07)
- Driver must exactly match the installed version on the server. 

## For Installation on a Machine
- [For Native Installation](https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/)
Best command to have Ubuntu automatically pickup the Nvidia Driver was 
```
sudo ubuntu-drivers install
```
## How to Blacklist the Nouveau Driver 
- [Noveau Blacklist](https://linuxconfig.org/how-to-disable-blacklist-nouveau-nvidia-driver-on-ubuntu-20-04-focal-fossa-linux/)

## Installation Notes for on a VM w/ GPU Passthrough 
- [Install First](http://www.teradici.com/web-help/ter1702003/2.8/Content/_Graphics Agent/Installing/Linux/installing_nvidia_linux_ubuntu.htm) 

- [ ] Install gcc and make pkg-config 
- [ ] Chmod +x 
- [ ] Run ./NVIDIA.... 
- [ ] Test that it sees the CUDA cores `nvidia-smi`

The better option was 430.30 that worked for the VGPU 

Make sure to install DKMS, which will keep the driver loaded after Kernel updates. 

## Improve NVIDIA Driver Stability through DKMS 

### Increase Kernel Stability 
After kernel updates the NVIDIA driver would need to be reinstalled after each update. DKMS will side-load the driver back in when a kernel update needs to be made to the system, which avoids the mess of reinstalling all the time. 

`sudo apt get install dkms` 
**DO NOT INSTALL SPECIFIC DRIVER VERSION FROM APT!** 

Reinstall the driver with DKMS support `sudo ./NVIDIA.run --dkms`
1. Choose YES to Would you like to register the kernel module sources with DKMS?
2. Choose NO to 32-bit compatibility modules 
3. Choose NO to update xconfig file. 

`sudo dkms status` 

```
sudo dkms status
nvidia, 460.32.03, 5.4.0-73-generic, x86_64: installed
```
🚀 Reference: https://askubuntu.com/questions/492217/nvidia-driver-reset-after-each-kernel-update 




