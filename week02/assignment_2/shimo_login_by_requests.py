import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
my_ua = ua.random
print(my_ua)

# Must have x-requested-with, if not, will get 403.
headers = {
    'user-agent': my_ua,
    'x-requested-with': 'XmlHttpRequest',
    'referer': 'https://shimo.im/login?from=home',
}

# Login with Email
# form_data = {
#     'email': 'test@qq.com',
#     'mobile': '+86undefined',
#     'password': 'test123',
# }

# Login with Mobile
form_data = {
    'mobile': '+8619012345678',
    'password': 'xxx_yyy',
}

s = requests.Session()

login_url = "https://shimo.im/lizard-api/auth/password/login"
r1 = s.post(login_url, data=form_data, headers=headers)
print('Status code of r1: ' + str(r1.status_code))

profile_url = 'https://shimo.im/profile'
r2 = s.get(profile_url, headers=headers)
print('Status code of r2: ' + str(r2.status_code))

# with open('./profile_by_requests.html', 'w') as f:
#     f.write(r2.text)
