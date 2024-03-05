from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def HTsentwp(title):
    reqUrl = "https://xc7.tech/wp-json/wp/v2/posts/"

    headersList = {
        "Authorization": "Basic YWRtaW46MjJoaDJoaGFhYQ==",
        "Content-Type": "application/json"
    }

    payload = {
        "title": title,
        "content": "To be Updated",
    }

    try:
        response = requests.post(reqUrl, headers=headersList, data=json.dumps(payload))
        responseData = response.json()
        return responseData['id']
    except Exception as e:
        print("Error:", e)
        return None

@app.route('/')
def create_post():
    title = request.args.get('t')
    if title:
        post_id = HTsentwp(title)
        if post_id:
            return jsonify({'post_id': post_id}), 200
        else:
            return jsonify({'error': 'Failed to create post.'}), 500
    else:
        return jsonify({'error': 'Title is missing in the request.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
  
