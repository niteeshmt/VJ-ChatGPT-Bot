from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
        "aira ai chat ",
         api_id=API_ID,"26396405"
         api_hash=API_HASH,
         bot_token="7144381603:AAEhNCp4SkhBHijzcQ15eMOobzcgY9b7Ano",
         plugins=dict(root="plugins"),
         workers=50,
         sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
            
        print('Bot Started Powered By @VJ_Botz')


    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()
