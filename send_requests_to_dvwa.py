import requests

host = 'http://45.66.8.232:8888'
proxies = {'http': 'http://45.66.8.232:8090',
           'https': 'http://45.66.8.232:8090',
           }
s = requests.session()
s.proxies.update(proxies)
print(s.proxies)
s.verify = False

s.headers.update(
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=07uktq4is0j0on1sk5bbpjb1f5; security=low",
        "Upgrade-Insecure-Requests": "1",
    }
)

s.get(f'{host}/vulnerabilities/brute/')

r = s.get(f'{host}/vulnerabilities/brute/?username=aa&password=aa&Login=Login')
print(r.status_code)

# s.get(f'{host}/vulnerabilities/exec/')

s.post(f'{host}/vulnerabilities/exec/', data='ip=1.1.1.1&Submit=Submit')

# s.get(f'{host}/vulnerabilities/csrf/')

s.get(f'{host}/vulnerabilities/csrf/?password_new=1&password_conf=1&Change=Change')

# s.get(f'{host}/vulnerabilities/fi/?page=include.php')

s.get(f'{host}/vulnerabilities/fi/?page=file1.php')

s.get(f'{host}/vulnerabilities/fi/?page=file2.php')

s.get(f'{host}/vulnerabilities/fi/?page=file3.php')

# s.get(f'{host}/vulnerabilities/upload/')

s.get(f'{host}/vulnerabilities/captcha/')

# s.get(f'{host}/vulnerabilities/sqli/')

s.get(f'{host}/vulnerabilities/sqli/?id=11&Submit=Submit')

# s.get(f'{host}/vulnerabilities/sqli_blind/')

s.get(f'{host}/vulnerabilities/sqli_blind/?id=11&Submit=Submit')

# s.get(f'{host}/vulnerabilities/weak_id/')

s.post(f'{host}/vulnerabilities/weak_id/')

# s.get(f'{host}/vulnerabilities/xss_d/')

s.get(f'{host}/vulnerabilities/xss_d/?default=English')

# s.get(f'{host}/vulnerabilities/xss_r/')

s.get(f'{host}/vulnerabilities/xss_r/?name=111')

# s.get(f'{host}/vulnerabilities/xss_s/')

s.post(f'{host}/vulnerabilities/xss_s/', data='txtName=111&mtxMessage=111&btnSign=Sign+Guestbook')

s.post(f'{host}/vulnerabilities/xss_s/', data='txtName=&mtxMessage=&btnClear=Clear+Guestbook')

# s.get(f'{host}/vulnerabilities/csp/')

s.post(f'{host}/vulnerabilities/csp/', data='include=1111111')

s.get(f'{host}/vulnerabilities/csp/1111111')

# s.get(f'{host}/vulnerabilities/javascript/')

s.post(f'{host}/vulnerabilities/javascript/',
       data='token=8b479aefbd90795395b3e7089ae0dc09&phrase=ChangeMe1&send=Submit')
