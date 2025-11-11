from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'
API_URL = 'https://pokeapi.co/api/v2/pokemon/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def ser_pokemon():
    pokemon_name = request.form.get('pokemon_name', '')
    
    if not pokemon_name:
        flash('Por favor, ingrese un nombre de Pokemon.', 'error')
        return redirect(url_for('index'))
try:
    response = requests.get(f"{API_URL}{pokemon_name}")
    if response.status_code == 200:
        pokemon_data = resp.json()
        return render_template('resultado.html', pokemon=pokemon_data)##puede ser pokemon.html bb
    

if __name__ == '__main__':
    app.run(debug=True)