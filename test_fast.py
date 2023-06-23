import requests


class TestFast:

    def __init__(self):
        self.host = 'http://45.66.8.232:8888'
        proxies = {'http': 'http://45.66.8.232:8090',
                   'https': 'http://45.66.8.232:8090',
                   }
        self.session = requests.session()
        self.session.proxies.update(proxies)
        self.session.verify = False

    def test_send_requests_and_check_results(self):
        # command injection
        self.session.get(f'{self.host}/ping?host=1.1.1.1')
        # csrf
        self.session.get(f'{self.host}/transfer_form')
        # file inclusion
        self.session.get(f'{self.host}/page/%3Chtml%3E123%3C%2Fhtml%3E')
        # file upload
        files = [('file', ('file', open('file_for_test', 'rb'), 'application/octet-stream'))]
        self.session.post(f'{self.host}/upload_file', files=files)
        # sql injection
        self.session.get(f'{self.host}/users?id_=1')
        # sql injection (bind)
        self.session.get(f'{self.host}/users_bind?id_=1')
        # xss
        self.session.get(f'{self.host}/search?query=1')


TestFast().test_send_requests_and_check_results()


