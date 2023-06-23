1. build docker container ``docker build -t vuln_app .``
2. start docker container ``docker run -d -n vuln_app -p 8000:8000 vuln_app``

you can see swagger here ``http://0.0.0.0:8000/docs``

for run requests:
1. need lib requests ``pip3 install requests``
2. run ``python3 send_requests.py --host http://example:8888 --proxy http://example:8090 --count 3``

count - how many times requests will be sent, default is 1