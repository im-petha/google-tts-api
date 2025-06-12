import requests
from flask import Flask, request, Response, jsonify
from flask_compress import Compress

app = Flask(__name__)

@app.route('/tts', methods=['GET'])
def tts():
    number = request.args.get('amount')
    ccy = request.args.get('ccy')
    if not number:
        return jsonify(error='Invalid number'), 400

    ccy_map = {'116': 'រៀល'}
    ccy_str = ccy_map.get(ccy, 'ដុល្លា')
    # phrase = f"បានទទួល {number} {ccy_str}"
    phrase = f"{number} {ccy_str}"

    try:
        r = requests.get(
            "https://translate.google.com/translate_tts",
            params={"ie": "UTF-8", "client": "tw-ob", "tl": "km", "q": phrase},
            headers={"User-Agent": "Mozilla/5.0"}
        )
        return Response(r.content, content_type='audio/mp3') if r.ok else (
            jsonify(error=f'Google TTS returned {r.status_code}'), r.status_code)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
