import vk_api
from vk_api.upload import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

import some_data
import add_text_on_photo


vk_session = vk_api.VkApi(token=some_data.vk_token)
longpoll = VkBotLongPoll(vk_session, 203065829)
vk = vk_session.get_api()
upload = VkUpload(vk_session)

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('kartinochka with luv', color=VkKeyboardColor.POSITIVE)
print(1772)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            vars1 = ['luv66']
            if vars1[0] in str(event):
                print(4)
                vk.messages.send(
                    key = ('__'),
                    server = "__",
                    ts= "31",
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='da'
                   )
            if r'kartinochka with luv' in str(event):

                #for name
                id_mes = event.message['from_id']
                user = vk_session.method("users.get", {'user_ids': id_mes})
                name = user[0]['first_name'].lower()
                id = user[0]['id']
                u2 = vk_session.method('users.get', {'user_ids': id_mes,'fields': 'sex'})
                sex = u2[0]['sex']
                print(u2[0]['sex'])

                # for photo
                img, eleven_meme = add_text_on_photo.give_photo(id, name)
                photo = upload.photo_messages(img)
                owner_id = photo[0]['owner_id']
                photo_id = photo[0]['id']
                access_key = photo[0]['access_key']
                attachment = f'photo{owner_id}_{photo_id}_{access_key}'

                #message
                if sex == 2:
                    vk.messages.send(
                        key=('__'),
                        server="__",
                        ts="31",
                        keyboard=keyboard.get_keyboard(),
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message='https://www.youtube.com/watch?v=SWDTdXH6oF0'
                    )
                else:
                    if eleven_meme:
                        vk.messages.send(
                            key=('__'),
                            server="__",
                            ts="31",
                            keyboard=keyboard.get_keyboard(),
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=attachment,
                            message = 'кидать сюда https://vk.com/tareli'
                        )
                    else:
                        vk.messages.send(
                            key=('__'),
                            server="__",
                            ts="31",
                            keyboard=keyboard.get_keyboard(),
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=attachment,
                        )

            if r'имя' in str(event):
                id_mes = event.message['from_id']
                user = vk_session.method("users.get", {'user_ids': id_mes})
                name = user[0]['first_name']
                print(name)
