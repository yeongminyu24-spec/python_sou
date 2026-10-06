from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__);

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/friend')
def api_friendFunc():
    name=request.args.get('name', '').strip(),
    age_str=request.args.get('age', '').strip()

    # 입력 검증
    if not name:
        return jsonify({"ok":False, "error":"name us required"}), 400 #  400 : Bad Request

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000);
