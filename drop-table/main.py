from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return 'Hello World'

# @app.route('/get-drop', methods=['GET', 'POST'])
# def get_drop():
#     pass




# if __name__ == '__main__':
#     app.run(debug=True)