import vk_api, json, time

LOGIN = ''
SERVICE_TOKEN = ''
API_VERSION = '5.131'
POST_COUNT = '1'
DELAY = 120
DOMAIN_BASE = [{'id': 'renaultru', 'name': 'RENAULT RUSSIA'}, {'id': 'nissanrussia', 'name': 'NISSAN RUSSIA'}, {'id':'mitsucarrus', 'name': 'MITSUBISHI RUSSIA'}]
PostDataBase = []

def vk_auth():
    global vk
    vk_session = vk_api.VkApi(login=LOGIN, token=SERVICE_TOKEN)
    vk_session.auth(reauth=False, token_only=True)
    vk = vk_session.get_api()

def get_info(domain_name):
    post = vk.wall.get(domain=domain_name, count=POST_COUNT, v=API_VERSION, access_token=SERVICE_TOKEN)
    return(post)

def parse_post(post_info):
    post_id = post_info["items"][0]["id"]
    post_date = post_info["items"][0]["date"]
    post_text = post_info["items"][0]["text"]
    post_data = {'id': post_id, 'date': post_date, 'text': post_text}
    post_uniq_id = str(post_id) + str(post_date)
    return(post_uniq_id, post_data)

def check_post(post_info, group_name):
    post_uniq_id = post_info[0]
    post_data = post_info[1]
    if post_uniq_id not in PostDataBase: 
        PostDataBase.append(post_uniq_id)
        post_text = post_data["text"]
        return('Post with ID: ' + post_uniq_id + ' has been added from: ' + group_name)
    else:
        return('No new posts in ' + group_name + '!')

vk_auth()

while True:
    for domain in range(len(DOMAIN_BASE)):
        group_name = DOMAIN_BASE[domain]["name"]
        post_info = get_info(DOMAIN_BASE[domain]["id"])
        parsed_post = parse_post(post_info)
        print(check_post(parsed_post, group_name))
        
    time.sleep(DELAY)