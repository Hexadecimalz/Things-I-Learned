# Microsoft Office 2019 Configuration Tools 

Microsoft is relying more heavily on configuration file setup for office product installs, rather than separate installers. This controls the download, configuration, and installation. 
To make matters worse there are `Click-to-Run` versions that are more o356-ish, so they won't play well with the regular installers. It's all or nothing – thanks Microsoft!

## 👨‍🔧 How To
1. Create a config file.
2. Open up a command prompt as Admin. 
3. Run the download portion `setup.exe /download configuration.xml` either save the download or run it on install.
4. Then run `setup.exe /configure configuration.xml` to install. If you're lucky you'll get a status indicator. If not, wait a while. 
5. A handy batch file you can run as Admin instead: 
```
pushd %~dp0 
setup.exe /download configuration.xml
setup.exe /configure configuration.xml
popd
```
6. You'll need the `setup.exe` file for the install, seems to be the same for them all, so keep that in mind.

### Extra Details 

If you're running a remote install you'll need to let the remote user know, since all Office Apps will need to be closed. This has hampered most remote installs through PDQ. 

Some interesting commands that pair together are `pushd` and `popd` which temporarily goes into a directory, and `popd` will take us back to the directory that we came from. 

## 🛰 Resources
- **Create the Config:** https://config.office.com
- **Good How-To:** https://www.trustedtechteam.com/pages/office-deployment-tool-guide
- **What is `pushd %~dp0`:** https://stackoverflow.com/questions/46089044/what-does-pushd-dp0-in-cmd-file-means-i-understand-dp0-means-it-indicates
