import requests

def chat(username, message):

        sender = username
        bot_message = ""
        print(message)
        print("Sending message now...")
        r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": sender, "message": message})
        responses = []
        print("Bot says, ")
        for i in r.json():
                bot_message = i['text']
                responses.append(bot_message)
                print(f"{i['text']}")
        return responses

if __name__ == '__main__':
        while(1):
                message = input("input a message:")
                res = chat("zhu",message)
