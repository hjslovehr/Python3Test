import requests
from bs4 import BeautifulSoup

image_set = ()
image_list = []

def get_img():
    r = requests.get('https://www.wsgxo.com/wsgxo-10554-1-1.html')
    r.encoding = 'gb2312'

    s = BeautifulSoup(r.text, 'html.parser')

    # print(r.text)

    image_set = s.select('img')

    # print(image_set)

    for item in image_set:
        # print(item)
        src = item.attrs.get('file')
        if None == src:
            continue
        
        if src.startswith('http') and src.endswith('.jpg'):
            # print(src)
            image_list.append(src)


def save_iamge():
    for img in image_list:
        print(img)

        file_name = [i for i in img.split('/') if i.endswith('.jpg')][0]
        # print(file_name)
        
        r = requests.get(img)
        with open('.\\temp\\{}'.format(file_name), 'wb') as f:
            f.write(r.content)
        
        print('Save file : ', file_name)



get_img()
save_iamge()
print(60 * '-')


# print(60 * '-')

