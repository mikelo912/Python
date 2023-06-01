from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('nma36VbQhr6iJMCgVvRx/DSOg23LctYL6UCc5TYYuitWsi97qhhAbm4862DaWELjCvoPzx+oAlgHRk0fa11XAgEWMlfaCO8IiLgErK0zJY3Djb4WC3FLYiQXjLN1SOkF0Ml14zckNqt7kHXQFmnzqQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ba0722de258de77c231d94c994578d59')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'





def getInfo(word):
    
    content = {"蘋果":"醫生的最大敵人","皮衣":"有名的黃先生","聯成":"電腦補習班"}
    
    return content.get(word,"我無法理解你說的")








@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    linemsg = event.message.text
    
    msgtype = 1

    if "空氣" in linemsg:
        response = getBike()   
    elif '圖片' in linemsg:
        msgtype = 2
    elif '貼圖' in linemsg:
        msgtype = 3
    elif '位置' in linemsg:
        msgtype = 4
    else:
        response = getInfo(linemsg)        

    if msgtype == 1:
        message = TextSendMessage(text=response)
    elif msgtype == 2:
        message = ImageSendMessage(original_content_url='https://pbs.twimg.com/media/DTOt6gCVwAAjtq8.jpg',preview_image_url='https://pbs.twimg.com/media/DTOt6gCVwAAjtq8.jpg')
    elif msgtype == 3:
        message = StickerSendMessage(package_id=8525,sticker_id=16581292)
    elif msgtype == 4:
        message = LocationSendMessage(title='我在哪裡',address='台中一中',latitude=24.1501454,longitude=120.6846957)
        
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
from ntpbike import getBike
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
