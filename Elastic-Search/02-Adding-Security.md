# Adding Security 🔐

Here we enable security. As noticed after setup `curl` does not require any authentication for information, so we setup a cetificate and enable authentication. 

## 🧃Setup Certs
This is to *minimally* secure a cluster. Better security would be a separate certificate per node.  

**Step 1: Create a cert storage location** 
```
#mkdir on all 3 servers
mkdir /etc/elasticsearch/certs

```

**Step 2:**  **Generate a cert**
Elastic Search Binaries located in `/usr/share/elasticsearch/bin` and we'll need to use them to setup a cert. 

```
./elasticsearch-certutil cert --name playground --out /etc/elasticsearch/certs/playground
```
If you setup a password, you must add the password to the elasticsearch keystore. 

**Step 3: Copy to nodes**
Copy the certs over to tmp `cp certs/playground /tmp/` and chown the folder, so it can be moved over for the user you have the password for: `chown cloud_user:cloud_user playground`

Run `scp` as the regular sudo privileged user: `scp playground privateip:/tmp` 
Copy over the folder now to elastic search `cp /tmp/playground /etc/elasticsearch/certs/`

chmod the cert, so it's writable by the elastic search user. `chmod 640 playground` from the `certs` directory. 

**Step 4: Tell Elastic about the Search in Config**
Create a new section at the bottom of `elasticsearch.yml`
```
# ------- Security ---- 
# 
xpack.security.enabled: true 
xpack.security.transport.ssl.enabled: true 
xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.keystore.path: certs/playground
xpack.security.transport.ssl.truststore..path: certs/playground
```

Paste into nodes use `:set paste` VIM to prevent things getting commented out 

Restart Elastic Search `systemctl restart elasticsearch`

In my experience the restarting of the service failed from `journalctl -xe` I got the following result: 

```
-- The result is failed.
Feb 06 18:18:12 ********* systemd[1]:
Unit elasticsearch.service entered failed state.
Feb 06 18:18:12 ********* systemd[1]:
elasticsearch.service failed.
Feb 06 18:18:12 ********* polkitd[651]:
Unregistered Authentication Agent for 
unix-process:13026:1680505 (system bus name :1.914, object path /org/free
```
**How did I fix it?** 
1. Checked the logs in `/var/log/elasticsearch/playground.log`
2. Realized I made a typo
3. Fixed it across all 3 hosts
4. `!systemctl` and it restarts 
5. Google didn't help 😑

**Step 5: Generate a Password**
```
$: /usr/share/elasticsearch/bin/elasticsearch-setup-passwords interactive
```

**Step 6: Test that authentication is enforced**
```
$: curl localhost:9200/_cat/nodes?v -u elastic
Enter host password for user 'elastic':
```
Results (minus verbosity) 
```
Enter host password for user 'elastic':
x.x.x.x 19 88 0 0.00 0.01 0.05 d  - data-1
x.x.x.x 17 55 0 0.03 0.02 0.05 im * master-1
x.x.x.x  20 87 0 0.02 0.04 0.05 d  - data-2
```

## 🚀 References
- Modify Elastic Search Keystore: https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-keystore.html (for example, to add a certificate password to the keystore)
