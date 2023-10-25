from flask import Flask

app = Flask(__name__)

@app.route('/')
def mensaje():
    return "¡Hola mundo!"

@app.route('/dojo')
def dojo():
    return "¡Dojo!"

@app.route('/say/<string:nombre>')
def saludo(nombre):
    return f"¡Hola, {nombre}!"

@app.route('/repeat/<int:veces>/<string:palabra>')
def repetir_palabra(veces, palabra):
    resultado = f"<p>{palabra}</p>" * veces
    return resultado

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__ == "__main__":
    app.run(debug=True)