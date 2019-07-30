import vk_api
from vk_api.audio import VkAudio


login, password = '#', '#'
vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth()
except vk_api.AuthError as error_msg:
    print(error_msg)

vkaudio = VkAudio(vk_session)

with open('audio_list.txt', 'w') as file:
    for track in vkaudio.get():
        file.write("{} - {}\n".format(track['artist'], track['title']))
    
print('Done')
