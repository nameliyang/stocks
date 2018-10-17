from flask import Flask, request, jsonify

from stock import daily
app = Flask(__name__)
# 测试数据暂时存放
tasks = []


@app.route('/get_k_data', methods=['POST'])
def add_task():
    code = request.json['code']
    start = request.json['start']
    end = request.json['end']
    response = daily.get_k_data(code, start, end)
    return response


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8383, threaded=True)

