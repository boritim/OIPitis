import csv
import webbrowser
import requests
import time

# webbrowser.open_new('https://oauth.vk.com/authorize?client_id=51578672&display=page&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.131&state=123456')

# https://oauth.vk.com/blank.html#access_token=vk1.a.c7pdj0HD2M_K43snGEaNgobJyNPnaO6q2lEQzzFJSP_5jmDYe6MOloNcaB7C2vNDN-FtMKrGT13Fcom9eIdSltTMMVXRPVMQNXzn7mMz9zPwjfnF5Z-27_ezsJjIcVzfWss9dGSSVOTFNGMkbvTVILl7hx8XH4kSKjGowaaRYWNVkrCJnJzkAeq08JACiq11&expires_in=86400&user_id=89207761&state=123456

def take_2000_posts():
    token = "vk1.a.c7pdj0HD2M_K43snGEaNgobJyNPnaO6q2lEQzzFJSP_5jmDYe6MOloNcaB7C2vNDN-FtMKrGT13Fcom9eIdSltTMMVXRPVMQNXzn7mMz9zPwjfnF5Z-27_ezsJjIcVzfWss9dGSSVOTFNGMkbvTVILl7hx8XH4kSKjGowaaRYWNVkrCJnJzkAeq08JACiq11"
    version = 5.131
    domain = 'jumoreski'
    count = 100
    offset = 0
    all_posts = []

    while offset < 100:
        response = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'domain': domain,
                            'count': count,
                            'offset': offset
                        }
                        )
        data = response.json()['response']['items']
        offset += 100

        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts

def file_writer(all_posts):
    with open('jumoreski.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(['text'])
        for post in all_posts:
            if (post['text']) != "":
                a_pen.writerow([post['text']])
                a_pen.writerow(['-----'])



if __name__ == '__main__':
    all_posts = take_2000_posts()
    file_writer(all_posts)



