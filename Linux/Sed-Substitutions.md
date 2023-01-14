# 🦆 Sed Substitutions

Did you know you can create a sed script and run it at the command line? 

``` #sedscript
#!/usr/bin/sed 

s/cool_token=(.+)/TOKEN IS \1/g
```

and here is an example file 

``` replaceme.txt
cool_token=mytoken1
cool_token=mytoken2
cool_token=mytoken3
```

to run it at the command line you can use a few different options 

- `-E` use extended regular expressions 
- `-f` use a sed script 
- `-i` if you want to replace the contents of the file permanently (i.e. you are confident your script is going to work without issue)

First, test that your regular expression worked before replacing anything in the file. The following command prints changes to standard out, but will not make any permanent changes to your file/s. 

`sed -E -f sedscript replaceme.txt` 

If the changes printed to standard out look acceptable, then you can permanently replace the changes easily enough as well. 

`sed -E -i -f sedscript replaceme.txt` 

## 🤔 Can it Recurse? 

But say we want to replace recursively down to directories in the directory we're in? 
We can use the find command do this, but we need to be careful that we exclude the script itself, or it will end up replacing the text in its own file, which makes it hard for it to continue matching the pattern you've set once it loses the text it was referencing. 

```
find . -type f -not -name "sed*" -exec sed -E -i -f sedscript2 {} +
```

## ☝🏼 But what's the `\1`? 

This is a truly useful part of regex. The parenthesis in our original regular expression (this one `cool_token=(.+)`) is called a capture group and this allows us to capture the text we find in the expression an repurpose it, such as changing how we display the value. For example, stripping the title from an HTML tag and sticking it into a markdown document. 

## Capture Group Printing with Perl 

We can also do some cool things with Perl that we cannot do so easily with Grep without involving Awk or other tools that might make things complex when it comes to capture groups. 

```example.txt 
title: Rime of the Ancient Mariner
author: Samuel Taylor Coleridge 
```

We can then run the following at the terminal on this file to get a neat way to work with the text: 

```
$ perl -lne '/(.+):\s(.+)/ && print "$1 is $2"' example.txt
#### Result below 
title is Rime of the Ancient Mariner
author is Samuel Taylor Coleridge
```

Notice that the colon and space are part of the expression, but not part of the capture group, so they get discarded as part of our operation to only use the capture groups. You might think of it like separating the bone from the tasty bits. We need the whole bird to arrive at dinner, but eventually we just settle down to get the meat of what we wanted.


## 🔭 References 
- [victoria.dev](https://victoria.dev/blog/how-to-replace-a-string-with-sed-in-current-and-recursive-subdirectories/)