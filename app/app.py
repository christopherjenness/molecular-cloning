from flask import Flask
from flask import request
from flask import render_template
from .. import sequences

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/DNA/', methods=['GET'])
def DNA_home():
    return render_template('insert_dna.html')


@app.route('/DNA/', methods=['POST'])
def dna_sequence_input():
    seq = request.form['sequence']
    dna = sequences.DNASequence(seq)
    return render_template('DNA.html', seq=dna)


@app.route('/protein/', methods=['GET'])
def protein_home():
    return render_template('insert_protein.html')


@app.route('/protein/', methods=['POST'])
def protein_sequence_input():
    seq = request.form['sequence']
    protein = sequences.ProteinSequence(seq)
    return render_template('protein.html', seq=protein)


if __name__ == '__main__':
    app.run(debug=True)
