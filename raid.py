import amino
import random
import concurrent.futures
from colorama import init, Fore, Back, Style
init(autoreset=True)
nick = ["t.me/obeexz", "obee", "wassup", "$28", " python", "here", "hello", "hi", "© obee", "nick"]
print("")
print(Fore.LIGHTGREEN_EX + "рейд бот")
print("")
print(Fore.LIGHTGREEN_EX + "Разработчик - <<obee>>")
print("")
print(Fore.LIGHTGREEN_EX + "контакт: t.me/obeexz.")
print("")
wmi = input("введите почту - ")
print("")
wsw = input("введите пароль - ")
client = amino.Client()
client.login(email=wmi, password=wsw)
print("")
print(Fore.LIGHTCYAN_EX + "ваши сообщества:")
print("")
for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
	print (name, id) 
print("")
wcm = input("введите айди сообщества - ")
print("")
sub_client = amino.SubClient(comId=wcm, profile=client.profile)
print(Fore.LIGHTCYAN_EX + "ваши чаты:")
print("")
for name, id in zip(sub_client.get_chat_threads().title, sub_client.get_chat_threads().chatId):
	print(name, id)
chat = input("Chat - ")
message = input("Message - ")
msgtype = input("msgtype - ")
print("")
print(Fore.LIGHTYELLOW_EX + "Чат выбран, ожидайте начала спама...")
while True:
    sub_client.edit_profile(nickname=random.choice(nick))
    with concurrent.futures.ThreadPoolExecutor(max_workers=222877777) as executor:
        _ = [executor.submit(sub_client.send_message, chat, message, msgtype) for _ in range(5000000000000)]