from flask import Flask

app = Flask(__name__)

@app.route("/phone/number")
def index():
	with open('upload.txt') as f:
		return f


@app.route("/phone/register", methods=['POST'])
def register():
	phone_number = request.files['the_file']
	with open('upload.txt', 'w') as f:
		f.write(phone_number)
	return "注册成功!"