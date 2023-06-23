import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Host URL')
parser.add_argument('--proxy', help='HTTP proxy URL')
parser.add_argument('--count', help='count runs', default=1)

args = parser.parse_args()

host = args.host
proxies = {
    'http': args.proxy,
    'https': args.proxy
}

session = requests.session()
session.proxies.update(proxies)
session.verify = False


def send_requests():
    print('start sending')
    # command injection
    session.get(f'{host}/ping?host=1.1.1.1')
    # csrf
    session.get(f'{host}/transfer_form')
    # file inclusion
    session.get(f'{host}/page/%3Chtml%3E123%3C%2Fhtml%3E')
    # file upload
    files = [('file', ('file', open('file_for_test', 'rb'), 'application/octet-stream'))]
    session.post(f'{host}/upload_file', files=files)
    # sql injection
    session.get(f'{host}/users?id_=1')
    # sql injection (bind)
    session.get(f'{host}/users_bind?id_=1')
    # xss
    session.get(f'{host}/search?query=1')
    print('sent')


for _ in range(int(args.count)):
    send_requests()
