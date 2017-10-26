from flask import Flask
from flask import request

application = Flask(__name__)

@application.route("/api/v1.0/wordsum2vec", methods=['GET'])
def get_permutations():

    string_arg = request.args.get('file')

    return str(string_arg)



if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True, port=8080)
