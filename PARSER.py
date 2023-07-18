import vk_api
import time

LOGIN: str = ''  # Формат XXXXXXXXXXX. Номер для входа
SERVICE_TOKEN: str = ''
API_VERSION: str = '5.131'  # Версия API Вконтакте. Дефолт - 5.131
POST_COUNT: str = '1'  # Количество постов для парсинга. Дефолт - парсим 1 пост
DELAY: int = 120  # Задержка между поисками новых постов
DOMAIN_BASE: list[dict] = [{'id': 'renaultru', 'name': 'RENAULT RUSSIA'},
                           {'id': 'nissanrussia', 'name': 'NISSAN RUSSIA'},
                           {'id': 'mitsucarrus', 'name': 'MITSUBISHI RUSSIA'}]
PostDataBase: list[str] = []


def vk_auth():
    """Авторизоваться во ВКонтакте через API."""
    global vk
    vk_session = vk_api.VkApi(login=LOGIN, token=SERVICE_TOKEN)
    vk_session.auth(reauth=False, token_only=True)
    vk = vk_session.get_api()


def get_info(domain_name):
    """Получить последний пост со стены группы."""
    post: str = vk.wall.get(domain=domain_name, count=POST_COUNT,
                            v=API_VERSION, access_token=SERVICE_TOKEN)
    return post


def parse_post(post_info):
    """Распарсить пост и его содержимое."""
    post_id: str = post_info["items"][0]["id"]
    post_date: str = post_info["items"][0]["date"]
    post_text: str = post_info["items"][0]["text"]
    post_data: dict[str: str] = {'id': post_id, 'date': post_date,
                                 'text': post_text}
    post_uniq_id: str = str(post_id) + str(post_date)
    return post_uniq_id, post_data


def check_post(post_info, group_name):
    """Проверка поста на уникальность и его наличие в БД."""
    post_uniq_id: str = post_info[0]
    post_data: str = post_info[1]
    if post_uniq_id not in PostDataBase:
        PostDataBase.append(post_uniq_id)
        post_text: str = post_data["text"]
        return (f'Запись с ID «{post_uniq_id}» '
                'была добавлена из группы «{group_name}»')
    else:
        return f'В группе «{group_name}» не найдено новых записей!'


vk_auth()

while True:
    for domain in range(len(DOMAIN_BASE)):
        group_name = DOMAIN_BASE[domain]["name"]
        post_info = get_info(DOMAIN_BASE[domain]["id"])
        parsed_post = parse_post(post_info)
        print(check_post(parsed_post, group_name))

    time.sleep(DELAY)
