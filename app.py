from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    ## Recupera as variáveis de ambiente ##
    env_vars = {
        "GREETING": os.getenv("GREETING", "Hello"),
        "TARGET": os.getenv("TARGET", "World")
    }
    return f"{env_vars['GREETING']} {env_vars['TARGET']}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)