# 💾 Install Metric Beat 

Collects metrics about a system. For example, CPU and RAM usage. 

## 🔧 Installation How To 

```
curl -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-7.6.0-x86_64.rpm
rpm --install metricbeat-7.6.0-x86_64.rpm
```

## 🗃 Edit the config 
`/etc/metricbeat/metricbeat.yml`

```
Refer to config for filebeat... It's the same 

VIM sections to search 
/Kibana
/Outputs
```

## Go through Setup

Module is already enabled, so run setup. 

```
metricbeat setup
systemctl start metricbeat
```

## 🧪 Test it 

`curl localhost:9200/_cat/indices?v -u elastic` 
