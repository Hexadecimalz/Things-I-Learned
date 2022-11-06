# Recursive Replacement

This one was inexplicably tough, but has come up a few times for sure. Of course, one of the more complex find commands can do this easily enough. For example, replacing a server address recursively through all files or something like that.

```
find . -type f -name '*' -exec sed -i 's/BYE/hi/g' {} \;
```

## Resources
[StackExchange](https://unix.stackexchange.com/questions/269279/find-and-replace-words-in-text-file-recursively)
