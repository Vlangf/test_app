1. build docker container ``docker build -t vuln_app .``
2. start docker container ``docker run -d -n vuln_app -p 8000:8000 vuln_app``

you can see swagger here ``http://0.0.0.0:8000/docs``

Create .env file with env vars:
```
WALLARM_API_TOKEN_NODE=
WALLARM_API_CA_VERIFY=
NGINX_BACKEND=
WALLARM_API_HOST=
WALLARM_API_TOKEN_SCANNER=
TARGET_URL=
WALLARM_TESTING_POLICY_ID=
OAS_SCANNER_TAG=
```


for run requests:
1. need lib requests ``pip3 install requests``
2. run ``python3 send_requests.py --host http://vuln_app_host:port --proxy http://example:8090 --count 3``

count - how many times requests will be sent, default is 1

#

first start node & app
```
docker-compose up app node
```

then you can start tester container
```
docker-compose run tester bash
```


