import requests
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/tts', methods=['GET'])
def tts():
    number = request.args.get('amount')
    ccy = request.args.get('ccy')
    ccyStr = 'dollar'
    
    print(ccy)
    if not number:
        return {'error': 'Invalid number'}, 400

    if ccy == '116':
        
        print(ccyStr)
        ccyStr = '៛'
  
    print(ccyStr)
    
    phrase = f"បានទទួល {number} {ccyStr}"
    tts_url = "https://translate.google.com/translate_tts"
    params = {
        "ie": "UTF-8",
        "client": "tw-ob",
        "tl": "km",
        "q": phrase
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(tts_url, params=params, headers=headers)
        if r.status_code == 200:
            return Response(r.content, content_type='audio/mp3')
        else:
            return {'error': f'Google TTS returned {r.status_code}'}, r.status_code
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

