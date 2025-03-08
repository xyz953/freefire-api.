from flask import Flask, request, jsonify

app = Flask(__name__)

uid_data = {
    "123456": {"name": "JohnDoe", "level": 50, "rank": "Diamond"},
    "987654": {"name": "JaneSmith", "level": 45, "rank": "Platinum"},
}

@app.route('/get_uid_info', methods=['GET'])
def get_uid_info():
    uid = request.args.get('uid')
    if uid in uid_data:
        return jsonify({"status": "success", "data": uid_data[uid]})
    else:
        return jsonify({"status": "error", "message": "UID not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)