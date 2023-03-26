from flask import Flask, request, url_for
from holamundo import SaludoGenerico

app = Flask(__name__)

@app.route("/")
def home():
    mensaje = saludo()
    return f"""
        <html>
        <body>
            <h1>Bienvendidos</h1>
            <h2>{mensaje}</h2>
        </body>
        </html>
    """

def saludo():
    return SaludoGenerico()

if __name__ == '__main__':
   app.run(debug=True)