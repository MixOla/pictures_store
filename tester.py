from PIL import Image
import requests
import json
import time
import base64
import io

url = 'http://208.51.60.18:2020/'

# Первичный запрос для создания заявки
def initiate_processing(prompt, neg_prompt='', imgs=None, strength=0, n=1, height=512, width=512,
                        steps=50, scale=7.5, seed=None, desc=False, cpu=False):
    params = {
        'prompt': prompt,
        'neg_prompt': neg_prompt,
        'imgs': imgs,
        # 'strength': strength,
        'n': n,
        'height': height,
        'width': width,
        'steps': steps,
        'scale': scale,
        'seed': seed,
        'desc': desc,
        'cpu': cpu
        }
    response = requests.post(url+'initiate_processing', json=json.dumps(params))
    if response.status_code == 200:
        return response.text
    else:
        return 'Error! ' + str(response.status_code) + ' ' + response.text

# Запрос на проверку статуса
def get_results(order_id):
    params = {'id': order_id}
    response = requests.post(url+'get_results', json=json.dumps(params))
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error! ' + str(response.status_code) + ' ' + response.text

# Запрос для получения результатов по заявке
def check_status(order_id):
    params = {'id': order_id}
    response = requests.post(url+'check_status', json=json.dumps(params))
    if response.status_code == 200:
        return response.text
    else:
        return 'Error! ' + str(response.status_code) + ' ' + response.text


def encode_img(path):
    image = Image.open(path)
    byte_img = io.BytesIO()
    image.save(byte_img, 'PNG')
    byte_img.seek(0)
    byte_img = byte_img.read()
    base64_img = base64.b64encode(byte_img)
    return base64_img.decode('ascii')

def decode_img(ascii_img):
    decoded = base64.b64decode(ascii_img)
    img_bytes = io.BytesIO(decoded)
    return Image.open(img_bytes)


# Создание заявки
order_id = initiate_processing(
    prompt = "Quiet dark night",
    neg_prompt = '',
#    imgs = encode_img('image.png'),
#    strength = 0.7,
    n = 1,
    height = 512,
    width = 512,
    steps = 50,
    # scale = 15,
    seed = None,
    desc = False,
    cpu = False
    )
print('Order ID: ' + order_id + '.')

# Проверка готовности заявки
status = check_status(order_id)
while status != 'completed':
    print('Status: ' + status + '.')
    if status == 'non-existant':
        print('Processing error!')
        break
    time.sleep(10)
    status = check_status(order_id)

result = get_results(order_id) # Результаты
folder = './' # Каталог сохранения результатов

# Сохранение изображений
i = 1
ascii_imgs = result['imgs']
for ascii_img in ascii_imgs:
    image = decode_img(ascii_img)
    image.save(f"{folder}result {i}.png", 'PNG')
    i += 1

# Сохранение описаний
descs = result['descs']
with open(f"{folder}descriptions.txt", 'a') as f:
    for desc in descs:
        f.write(desc)
        f.write('\n')

print('Done!')
