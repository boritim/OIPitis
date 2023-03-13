import csv
import webbrowser
import requests
import time


def take_2000_posts(token, domain):
    token = token
    version = 5.131
    domain = domain
    count = 100
    offset = 0
    file = open(f'{domain}.csv', 'w+', encoding="utf-16")
    all_posts = csv.writer(file)
    all_posts.writerow(['text'])

    while offset < 2000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        try:
            data = response.json()['response']['items']

            for item in data:
                if item['text'] != '':
                    all_posts.writerow([item['text']])
                    # all_posts.writerow('-----')
                    offset += 1

        except Exception as exception:
            print('Something Went Wrong (Check Domain or API Key)')
            raise Exception(exception)

        time.sleep(0.5)

    file.close()


if __name__ == '__main__':
    try:
        DOMAIN = 'jumoreski'
        TOKEN = "vk1.a.c7pdj0HD2M_K43snGEaNgobJyNPnaO6q2lEQzzFJSP_5jmDYe6MOloNcaB7C2vNDN-FtMKrGT13Fcom9eIdSltTMMVXRPVMQNXzn7mMz9zPwjfnF5Z-27_ezsJjIcVzfWss9dGSSVOTFNGMkbvTVILl7hx8XH4kSKjGowaaRYWNVkrCJnJzkAeq08JACiq11"
        take_2000_posts(TOKEN, DOMAIN)

    except Exception as e:
        print(f'Got an exception: {e}')
