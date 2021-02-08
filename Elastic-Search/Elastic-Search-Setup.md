# 🦙 Elastic Search Setup

Building a multi-node cluster (1x master and 2x nodes). Nodes running CentOS 7. 

## Installation 
```
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.0-x86_64.rpm
rpm --install elasticsearch-7.6.0-x86_64.rpm
systemctl daemon-reload
systemctl enable elasticsearch
## Modify each config file for all nodes as specified below
vim /etc/elasticsearch/elasticsearch.yml
## JVM options for ram were set 
vim /etc/elasticsearch/jvm.options
systemctl start elasticsearch
systemctl status elasticsearch
```
 
Need to modify the etc config on the master and the nodes. 
```
cluster.name: playground
node.name: master-1 / data-1 / data-2
#Set Network to an array
network.host [_local_, _site_] 
discovery.seed_hosts: [PRIVATE_IP]
---Various--- 
node.master: true/false
node.data: false/true (true = node)
node.ingest: false/trtue (true = master)
node.ml: false (set on data nodes, for machine learning)
```

### 🔗 How to know if the node joined? 

#### Using the log file 
`tail -f /var/log/elasticsearch/playground.log`

then run on each node 

`systemctl start elasticsearch` 

verify in the master if the nodes report back as joined. The log file will report back that the node/s joined.  

### 🐱‍👓 Using cat 

For example try 

```
$: curl localhost:9200
{
  "name" : "master-1",
  "cluster_name" : "playground",
  "cluster_uuid" : "xQRgxPacSu-Cqb5KPsCtTw",
  "version" : {
    "number" : "7.6.0",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "7f634e9f44834fbc12724506cc1da681b0c3b1e3",
    "build_date" : "2020-02-06T00:09:00.449973Z",
    "build_snapshot" : false,
    "lucene_version" : "8.4.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```
**Verify Nodes** 
```
curl localhost:9200/_cat/nodes 
172.31.98.255   7 85 0 0.02 0.03 0.05 d  - data-2
172.31.102.251 18 79 1 0.00 0.01 0.05 im * master-1
172.31.109.122  9 85 8 0.24 0.30 0.17 d  - data-1
```

To get some extra verbosity
`curl localhost:9200/_cat/nodes?v`

**See More Cats** 🐱
`localhost:9200/_cat`
