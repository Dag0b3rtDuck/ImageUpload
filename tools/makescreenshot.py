import pyscreenshot
import requests

def take_scren():
    image = im = pyscreenshot.grab()
    im.save("C:\\Users\\timoz\\Pictures\\screenshot.jpg")
    im.show()
    file = {
        "file": open("C:\\Users\\timoz\\Pictures\\screenshot.jpg", "rb")
    }
    key = {'api_key': 'hjsdg79qqerwg34uighölvng79'}
    requests.post("http://127.0.0.1:1337/api/upload", data=key, files=file)


if __name__ == '__main__':
    take_scren()
