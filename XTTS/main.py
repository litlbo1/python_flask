import torch
from TTS.api import TTS
from flask import Flask, request, jsonify

app = Flask(__name__)

# device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

@app.route('/')
def test():
    return "Hello)"

@app.route('/postjson', methods=['POST'])
def post_json():
    data = request.get_json()  # Получаем JSON из запроса
    # Проверяем, есть ли ключ 'messages' и он является списком
    if 'messages' in data and isinstance(data['messages'], list):
        # Итерируем каждое сообщение в списке
        for message in data['messages']:
            # Проверяем, есть ли ключ 'key' в сообщении
            if 'key' in message:
                value = message['key']  # Получаем значение для ключа 'key'
                print(value)
                tts.tts_to_file(text=value, speaker_wav="Amina.wav", language="ru", file_path="output.wav")  # Выводим значение в консоль
                return jsonify({"message": "Значение 'key' получено", "yourValue": value}), 200
        return jsonify({"error": "Нет ключа 'key' в сообщениях"}), 400
    else:
        return jsonify({"error": "Нет ключа 'messages' в JSON или 'messages' не является списком"}), 400

if __name__ == '__main__':
    app.run(port=5000)





