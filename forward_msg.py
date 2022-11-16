from for_sign import *
from telethon.errors import ChatWriteForbiddenError


async def search(channels_input, key_words, channels_output): 
    try:
        for chan_out in channels_output:
            for chanel_inp in channels_input:
                async for message in client.iter_messages(chanel_inp, search=key_words, limit=20):
                    await client.forward_messages(entity=chan_out, messages=message)
        output_after_search = "Успешно выполнена отправка"
    except ChatWriteForbiddenError:
        output_after_search = "У вас нет доступа к одному из каналов для публикации"
    except ValueError:
        output_after_search = "Такой пользователь или канал не существует"
    finally:
       pass # print(output_after_search)



with client:
    client.loop.run_until_complete(search(channels_input=tuple(["python2day", "Python_per_month"]), 
        key_words="python", 
        channels_output=tuple(["ponyatnenkoebat", "me"]))) #передавать в виде кортежа ОБЯЗАТЕЛЬНО