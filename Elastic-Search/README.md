# 📓 Elasticsearch Cluster Notes

Here are notes from a crash course I took about Elasticsearch. These are notes that I took setting up a cluster consisting of 3 servers on CentOS 7. 
The setup was straightforward, although I encountered one big problem due to a typo in the configuration file that I made, which I also documented along the way. 

At the end of the project I was able to use the Kibana dashboard to look at logs on the hosts to see metrics through metric beat, and also look at SSH and sudo commands from
system beat. What was of particular interest were a large amount of unsuccessful SSH attempts made to hosts, since this was on AWS with a public IP a lot of failed attempts to
login to the hosts were made. 
