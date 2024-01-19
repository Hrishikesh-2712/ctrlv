from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep
import json
from channels.layers import get_channel_layer
from collections import defaultdict

class WSConsumer(AsyncWebsocketConsumer):
    connected_user = defaultdict(list) # {group1:[user1, user2], group2:[user1, user2]}
    channel_layer = get_channel_layer()

    async def broadcast_other(self, data, group):
        if self.connected_user.get(group) == None:
            return
        if len(self.connected_user.get(group))==0:
            self.connected_user.pop(group)
            return
        # current group
        for user in self.connected_user.get(group):
            if self.scope['cookies']['csrftoken'] != user[0]:
                await user[1].send(data)
                
                
    async def connect(self):
        self.group_name = self.scope["url_route"]["kwargs"]["group"]
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        
        print(self.scope['user'], self.scope['user'].id, 'connected')
        
        if self.scope['cookies'].get('csrftoken')!=None:
            # self.connected_user[self.scope['cookies']['csrftoken']] = self
            self.connected_user[self.group_name].append((self.scope['cookies']['csrftoken'],self,))
        else:
            await self.send(json.dumps({"connection": "failed", "reason":"cookies are blocked", "error":True}))
            return
        await self.send(json.dumps({"connection": "success"}))
        await self.connected_user.get(self.group_name)[0][1].send(json.dumps({"fetch": True}))
        await self.channel_layer.group_send(self.group_name,{"type":"comit","text":{"data":json.dumps({'fetch':True})}})

    async def receive(self, text_data):
        # await self.send(f'echo {text_data}')

        # await self.broadcast_message(self.group_name, text_data)
        # await self.channel_layer.group_send(self.group_name,{"type":"comit","text":{"data":text_data}})

        await self.broadcast_other(text_data, self.group_name)

    async def disconnect(self, close_code):
        pass
        # try:
            # self.connected_user[self.group_name].pop(scope['cookies']['csrftoken']])
        # except:
        #     print("cannot delete id from connected user")


    async def comit(self, event):
        message = event["text"]['data']
        await self.send(text_data=message)

    