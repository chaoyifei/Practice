import requests
import itchat

KEY = 'd3a7b8f3fd0c487ca267bd86f25940db'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):

    defaultReply = 'I received: ' + msg['Text']

    reply = get_response(msg['Text'])

    return reply or defaultReply


itchat.run()

itchat.auto_login(hotReload=True)