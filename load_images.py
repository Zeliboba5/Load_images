import requests


def create_users(s):
    url = 'http://localhost:5000/signup'
    payload = {'username': 'Admin', 'password': '12345'}
    s.post(url, data=payload)


def load_images(s):
    url = 'http://localhost:5000/image/new'
    for i in range(0, 9):
        payload = {'title': 'Very funny image' + str(i), 'description': 'Even more funny description' + str(i)}
        files = {'file': open('images/' + str(1) + '.jpg', 'rb')}
        s.post(url, data=payload, files=files)


if __name__ == '__main__':
    s = requests.session()
    create_users(s)
    load_images(s)
