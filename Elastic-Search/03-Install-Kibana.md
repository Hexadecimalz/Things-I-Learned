# 📊 Installing Kibana and connecting to an Elasticsearch Cluster 

We only need to run this on the master server. Separate beats will connect to the main server. 

## 🔧 Install 
Grab the rpm file and install. 
```
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.6.0-x86_64.rpm 
rpm --install kibana-7.6.0-x86_64.rpm
systemctl enable kibana 
systemctl start kibana && systemctl status kibana
```

## 🗃 Change configuration as necessary 

**Location:** `/etc/kibana/kibana.yml`

```
server.port: 8080 
server.host: "PRIVATE IP"

elasticsearch.username: "kibana"
elasticsearch.password: "PASSWORD"
```

Kibana will will log its status to `/var/log/messages`

## ❔ Did it work? 

Go to the public IP address and you should be prompted with a login screen `IP:8080` 

- **Username:** elastic
- **Password:** {set earlier}

## 🖥Checkout dev tools and use the console to list out nodes 

For example in the console type 
```
GET _cat/nodes?v
```
