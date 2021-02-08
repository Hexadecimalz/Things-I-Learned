# ❤  Collect and ship logs 

Using filebeat to send logs to Kibana. 

## 🔧 Install 
Run on all nodes. Probably a good opportunity to automate these steps through Ansible. 
```
curl -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.6.0-x86_64.rpm
rpm --install filebeat-7.6.0-x86_64.rpm
systemctl enable filebeat 
```

## 🗃 Change config 
`/etc/filebeat/filebeat.yml`
```
#----- Kibana ----- 
host: "PRIVATEIP:8080"
#=== Outputs =====
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["PRIVATEIP:9200"]

  #Protocol - either `http` (default) or `https`.
  #protocol: "https"

  # Authentication credentials - either API key or username/password.
  #api_key: "id:api_key"
  username: "elastic"
  password: "PASSWORD"

```

## 📂 Filebeat Setup 
```
filebeat modules enable system
filebeat setup
systemctl start filebeat
```

## 🧪 Test that it worked 

```
curl localhost:9200/_cat/indices?v -u elastic
```

