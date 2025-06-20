
# import requests
# from flask import Flask, request, Response, jsonify

# app = Flask(__name__)

# @app.route('/tts', methods=['GET'])
# def tts():
#     raw_number = request.args.get('amount')
#     lang = request.args.get('lang', 'km')  # Default to Khmer
#     ccy = request.args.get('ccy')

#     if not raw_number:
#         return jsonify(error='Invalid number'), 400

#     try:
#         number = int(float(raw_number)) if float(raw_number).is_integer() else float(raw_number)
#     except:
#         return jsonify(error='Invalid number format'), 400

#     # Currency mapping
#     currency_map = {
#         'km': {'116': 'រៀល', '840': 'ដុល្លារ'},
#         'en': {'116': 'Riel', '840': 'Dollar'}
#     }

#     # Phrase template
#     phrase_template = {
#         'km': 'បានទទួល {number} {currency}',
#         'en': 'Received {number} {currency}'
#     }

#     # Resolve currency
#     currency_str = currency_map.get(lang, {}).get(ccy, 'Dollar' if lang == 'en' else 'ដុល្លារ')
#     phrase = phrase_template.get(lang, phrase_template['km']).format(number=number, currency=currency_str)

#     try:
#         r = requests.get(
#             "https://translate.google.com/translate_tts",
#             params={"ie": "UTF-8", "client": "tw-ob", "tl": lang, "q": phrase},
#             headers={"User-Agent": "Mozilla/5.0"}
#         )
#         if r.ok:
#             return Response(r.content, content_type='audio/mp3')
#         else:
#             return jsonify(error=f'Google TTS returned {r.status_code}'), r.status_code
#     except Exception as e:
#         return jsonify(error=str(e)), 500


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


import requests
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/tts', methods=['GET'])
def tts():
    raw_number = request.args.get('amount')
    lang = request.args.get('lang', 'km')  # Default to Khmer
    ccy = request.args.get('ccy')

    if not raw_number:
        return jsonify(error='Invalid number'), 400

    try:
        number = int(float(raw_number)) if float(raw_number).is_integer() else float(raw_number)
    except:
        return jsonify(error='Invalid number format'), 400

    # Currency mapping
    currency_map = {
        'km': {'116': 'រៀល', '840': 'ឌុលឡា', '104': 'ကျပ်'},
        'en': {'116': 'Reel', '840': 'Dollar', '104': 'Kyat'},
        'my': {'116': 'ရီးလ်', '840': '$', '104': 'ကျပ်'}
    }

    # Phrase templates
    phrase_template = {
        'km': '{number} {currency}',
        'en': 'Well Received {number} {currency}',
        'my': '{number} {currency} ဝင်ပြီ။'
    }

    currency_str = currency_map.get(lang, {}).get(ccy, 'Dollar' if lang == 'en' else 'ឌុលឡា')
    phrase = phrase_template.get(lang, phrase_template['km']).format(number=number, currency=currency_str)

    try:
        r = requests.get(
            "https://translate.google.com/translate_tts",
            params={"ie": "UTF-8", "client": "tw-ob", "tl": lang, "q": phrase},
            headers={"User-Agent": "Mozilla/5.0"}
        )
        if r.ok:
            return Response(r.content, content_type='audio/mp3')
        else:
            return jsonify(error=f'Google TTS returned {r.status_code}'), r.status_code
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
