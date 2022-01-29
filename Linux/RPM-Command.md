# RPM Commands 
The RedHat Package Manager (RPM) can be used to install and query packages on a system, although it's largely been replaced by more versatile package managers such as Yum and DNF. 

## RPM commands 
```
# query packages owning a file 
rpm -qf FILE 

# list files in package 
rpm -ql package 

# show configuration of a packages 
rpm -qc mypackage

# show scripts in a package
rpm -qp --scripts mypackagefile.rpm 

# query all 
rpm -qa package 
```

## How to query a Package? 
1. `yum install dnf-utils -y`
2. `yumdownloader httpd`
3. `rpm -qp --script package.rpm`  

## Resources
`man rpm` 