# RHCSA Resources

Here are some resources I colleted while studying for RHCSA. This is not a cheatsheet, although it has a few general tips near the end. The purpose of this document for me was to list out links to interesting topics or questions that came up while studying or scheduling the exam. For example, why does scheduling a cron job open up in a temp file? Why is it that we need the execute bit set to traverse a directory? 

## RHCSA Links 

- 💲 [VIM Shortucts](https://www.elsewebdevelopment.com/ultimate-vim-keyboard-shortcuts/) 

- 💲 [Move to the end of a line in Vim](https://stackoverflow.com/questions/105721/how-do-i-move-to-end-of-line-in-vim)
    - `$` (end of line) or `A` (end of line and append)

- 💲 [Learn Vim (the smart way)](https://github.com/iggredible/Learn-Vim)
    
- 💲 [01 Vim](https://www.youtube.com/watch?v=C-14ZyHsilc)
   
- 💲 [02 Vim](https://www.youtube.com/watch?v=4eRtrhD3u2k)
        
- 💲 [Write an already open file with sudo privilege in Vim](https://stackoverflow.com/questions/2600783/how-does-the-vim-write-with-sudo-trick-work)
  - `:w !sudo tee %`

- 🔔 [Windows Terminal: Turn off the Bell](https://stackoverflow.com/questions/36724209/disable-beep-in-wsl-terminal-on-windows-10) 
  - Best option was to disable the WSL app in the Sound mixer completely. Some of the VIM hacks would work, but only on the same host, SSH into a new host and all progress is lost. In Windows Terminal, check out the Advanced tab for 'Bell notification style' and choose 'flash taskbar', which also may be effective in silencing the bell. 

- 🏃🏻‍♀️ [Check if service is running in Bash](https://www.cyberciti.biz/faq/bash-check-if-process-is-running-or-notonlinuxunix/)

- 🦵🥾 [Interrupt Boot (fastest method!)](https://github.com/ahaitoute/RHCSA-notitie/blob/master/2-Operate%20running%20systems/3-Interrupt%20the%20boot%20process%20in%20order%20to%20gain%20access%20to%20a%20system.md)
  - Use `sudo reboot -f`   to reboot the machine after performing these tasks. 

- 🥽 [Getting UUID from blkid command in many interesting ways](https://stackoverflow.com/questions/13565658/right-tool-to-filter-the-uuid-from-the-output-of-blkid-program-using-grep-cut/16277809)
   - `lsblk -no /dev/sdb1`
    
- ❔ [Grep in an IF statement](https://unix.stackexchange.com/questions/48535/can-grep-return-true-false-or-are-there-alternative-methods)
  - `if grep -q PATTERN file.txt; then`
   
- ❔ [Why do you need the execute bit to traverse a directory?](https://unix.stackexchange.com/questions/21251/execute-vs-read-bit-how-do-directory-permissions-in-linux-work)

- 📁 [What's Thin Provisioning?](https://www.youtube.com/watch?v=bpZKjeK0uTQ)

- [🐦Sed, Awk 🦅, and Grep 🦆](https://arstechnica.com/gadgets/2021/08/linux-bsd-command-line-101-using-awk-sed-and-grep-in-the-terminal/)
    
- 🐦 [Sed - An Introduction and tutorial by Bruce Barnett](https://www.grymoire.com/Unix/Sed.html)
    
- 🦅 [Understanding AWK](https://earthly.dev/blog/awk-examples/)
     Comments from HN: https://news.ycombinator.com/item?id=28707463 

- 🌌 [Ansible Techniques](https://zwischenzugs.com/2021/08/27/five-ansible-techniques-i-wish-id-known-earlier/)

- 🦎 [DistroTest.net (test a distro)](https://distrotest.net)

- 🤓 [Explain Shell (terminal commands)](https://explainshell.com)

- 👟 Speed Up terminal
    - https://unix.stackexchange.com/questions/387149/ubuntu-terminal-go-to-mouse-cursor-position
    - https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Bindable-Readline-Commands 

- [🎁 SCP ](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

- [🎭 systemctl calls mask, unmask, etc.](https://askubuntu.com/questions/816285/what-is-the-difference-between-systemctl-mask-and-systemctl-disable)

- [👷🏻‍♂️ Dummy interfaces with modprobe](https://unix.stackexchange.com/questions/335284/how-can-we-create-multiple-dummy-interfaces-on-linux)
    
- ⛅ [LVM Cheat Sheet from How-To Geek](https://www.howtogeek.com/howto/40702/how-to-manage-and-use-lvm-logical-volume-management-in-ubuntu/)

- ⛅ [LVM : A Step by Step Guide ](https://edumotivation.com/what-is-lvm-logical-volume-manager/)

- 🌊 [Stratis from Redhat](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_file_systems/managing-layered-local-storage-with-stratis_managing-file-systems)
    
- 🌊 [Stratis Cheat Sheet](https://computingforgeeks.com/stratis-storage-management-cheatsheet/)
    
- 📂 [Mounting devices with a systemd Mount](https://forum.endeavouros.com/t/root-mounting-any-device-using-systemd-mount-and-automount/7696)

- ⛑ [Youtube: RHCSA Exam Setup from RedHat](https://www.youtube.com/watch?v=LX3VMIAuPzg)
        
- ⛑ [Red Hat Exam Scheduler (3-day delay between buying voucher and scheduling)](https://rhtapps.redhat.com/individualexamscheduler/#/Dashboard)
     
- ⛑ [Getting ready for your RedHat Remote Exam](https://www.redhat.com/rhdc/managed-files/tr-remote-exams-preparation-ebook-f27382-202103-en_1.pdf)
    
- 🌩 [Vagrant Cloud](https://app.vagrantup.com/boxes/search)
    
- ⛓ [Youtube: Routing Tables Explained](https://www.youtube.com/watch?v=g8eP4fhrx3I)
  
- 🐚 [Shellcheck (check syntax in bash)](https://www.shellcheck.net)
    
- 🐚 [Shell Aliases](https://www.cyberciti.biz/tips/bash-aliases-mac-centos-linux-unix.html)
  
- 🐚 [Effective Shell](https://effective-shell.com)
 
- 🐚 [Run Bash from VSCODE](https://stackoverflow.com/questions/42606837/how-do-i-use-bash-on-windows-from-the-visual-studio-code-integrated-terminal)
   
- 🗄 [Manual Partitioning CentOS/RHEL](https://docs.centos.org/en-US/centos/install-guide/CustomSpoke-ppc64/)
    - /boot parition 1024MiB Minimum 
    - /root 10GiB Minimum 
    - swap 1024MiB Minimum
        - 2-8GB Swap equal to the amount of ram 
        - 8-64GB Swap at 50% of ram 

- 🏆 [RHCSA Cheatsheet](https://github.com/ruthealee/RHCSA-cheat-sheet/blob/master/CheatSheet)
    
- 🕕 [Crontab Opens in /tmp?](https://unix.stackexchange.com/questions/197504/shall-i-save-my-crontab-file-in-tmp/197506)
  
- 🕕 [Give Timestamp to .bash_history](https://www.howtoforge.com/adding-date-and-time-to-your-bash-history) 
   - `echo "export HISTTIMEFORMAT=\"%h/%d - %H:%M:%S\"" >> /etc/bashrc`
  
- 🏆 [Subnetting Cheatsheet](https://nsrc.org/workshops/2009/summer/presentations/day3/subnetting.pdf) 
     
- 🐳 [Rootless Containers (don't SSH in as sudo/su)](https://access.redhat.com/discussions/6029491)
     
- 🧹 [`which` is not POSIX compatible](https://hynek.me/til/which-not-posix/)
   - `type -P ls` worked well 
    
     
## 🦆 Grep 
- Grep looking for a term: `grep -i dnf /var/log/messages`💡 i = include, case-insensitive 
- grep looking NOT FOR: `grep -v dnf /var/log/messages`💡 v = inVert (don't include)
- Recursive search for "student": `grep -R student /etc `🔎 R = recursive 
- Recursive search and filter errors: `grep -R student /etc/ 2>/dev/null`
- Grep multiple items 1: `grep -E 'panpan|grizz|icebear' /etc/passwd`
- Grep multiple items 2: `grep -e 'iguana' -e 'lizard' ~/file`🐻 [e|E] = Everyone! 
- Grep line beginning with word, exclude errors: `grep '\<root\>' /etc/passwd 2>/dev/null`
- Grep multiple elements from multiple files `grep 'duck\|elephant\|horse' /etc/{passwd,group,shadow}` 🧙🏻‍♂️
- `grep -A5` : shows 5 files after the matching regex 
- `grep -B4` : shows 4 lines before the matching regex  


## 🔮 Tidbits 

1. Cool way to search 
`find $(locate *.*.example)` 

2. Use semi-colon on a the prompt to run multiple commands, rather than && 
- Run two commands one after the other:`ls -al ; ls -ald`
- Run one command and run the second only if the first was successful:`sudo yum update -y && sudo reboot` 
- Try to run a command, run the second one if the first one fails (also filters out errors)`cat /etc/centos-release 2>/dev/null || cat /etc/lsb-release 2>/dev/null` 

3. Show uuid for a block device more easily, and print to /etc/fstab
```
# option #1 use d5w when in vim to remove the extra dev name 
blkid -s UUID /dev/device >> /etc/fstab

# option #2 
echo -e "UUID=\"$(lsblk -no UUID /dev/sde1)\"\t/mount\txfs\tdefaults\t0 0"

# option #3
blkid -s UUID /dev/sde1 | awk -F : '{print $2}'

# option #4 
echo -e "$(blkid -s UUID /dev/sde1 | awk -F : '{print $2}')\t/mount\txfs\tdefaults\0 0 "

# option #5 simplify the awk
echo -e "$(blkid -s UUID /dev/sde1 | awk '{print $2}')\t/mount\txfs\tdefaults\0 0 "
```

3. VDO Mount Options (if not using systemd mount) 
```
# /etc/fstab
_netdev,defaults,x-systemd.device-timeout=0,x-systemd.requires=vdo.service
```

## 👟 Command Line Speed 
- `Control + A`  → Go to beginning of a line 
- `Control + E`  → Go to end of a line 
- `Control + ⇐` → Backwards 1 word, or opposite forward 1 word
- `Control + W`  → Delete 1 word back 
- `Control + K`  → Delete everything in front of the cursor
- `Control + U`  → Delete entire line 
- `Control + P`  → Previous command 

See also: https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Bindable-Readline-Commands 
