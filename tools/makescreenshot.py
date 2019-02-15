import pyscreenshot
import requests

def take_screen():
    image = im = pyscreenshot.grab()
    im.save("C:\\Users\\username\\Pictures\\screenshot.jpg") #insert your username instead of username
    im.show()
    file = {
        "file": open("C:\\Users\\username\\Pictures\\screenshot.jpg", "rb") #insert your username instead of username
    }
    key = {'api_key': 'hjsdg79qqerwg34uighölvng79'}
    requests.post("http://127.0.0.1:1337/api/upload", data=key, files=file)


if __name__ == '__main__':
    take_scren()
