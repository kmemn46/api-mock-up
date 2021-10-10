from flask import Flask, jsonify, request
import random

app = Flask(__name__)
 
@app.route("/api-mock", methods=["POST"])
def api_mock():

    # パラメータ取得
    request_data = request.form["image_path"]
    print(request_data)

    # 返却用Json
    response_success = {
        "success": True,
        "message": "success",
        "estimated_data":{
            "class": 3,
            "confidence": 0.8683
        }        
    }
    response_error = {
        "success": False,
        "message": "Error:E50012",
        "estimated_data":{}
    }
    response = [response_success, response_error]

    # ランダムで返却
    return jsonify(random.choice(response))

if __name__ == "__main__":
    print(" * Flask starting server...")
    app.run()