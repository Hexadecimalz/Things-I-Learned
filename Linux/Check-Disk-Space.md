# Check Disk Space 
Here are the most common commands I've used recently to check disk space: 
- System Check: `du -ch --max-depth=2 / | less` 
- Clean out yum cache: `rm -rf /var/cache/yum` 
- Find: `find / -size +10000k` 
- Systemd-Journald: `journalctl --vacuum-time 1s` 


## Other Options 
The utility `ncdu` came up in several searched as well as a nice graphical utility to see what's taking up disk space. This tool would be practical before disk space is at critical levels, but if it's already gone, then that just won't work. 

You could also try: 

`find / -type f -exec wc -c {} \; | sort -n`

This can take a while searching through all files one-by-one. `wc` will print the size of the files in bytes and piping it to sort will gives us the smalles first first and the biggest ones last. 

Say you want to list the largest files first, that can be accomplished by reversing the result: 

`find / -type f -exec wc -c {} \; | sort -n -r`