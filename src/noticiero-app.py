#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import funciones

app = Flask(__name__)

@app.route('/')
def inicio():
	return jsonify(status="Ok")

@app.route('/noticia/usuario/<usuario>')
def Noticias_1(usuario):
	n=funciones.Noticias()
	datos=n.getNoticiasUsuario(usuario)
	return jsonify(noticia=datos)

@app.route('/noticia/fecha/<fecha>')
def Noticias_2(fecha):
	n=funciones.Noticias()
	datos=n.getNoticiasFecha(fecha)
	return jsonify(noticia=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
