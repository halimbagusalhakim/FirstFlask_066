from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form.get('nama')
    kelas = request.form.get('kelas')
    nim = request.form.get('nim')
    return f"""
    <h1>Data Mahasiswa</h1>
    <p><strong>Nama:</strong> {nama}</p>
    <p><strong>Kelas:</strong> {kelas}</p>
    <p><strong>NIM:</strong> {nim}</p>
    <a href="/">Kembali ke Form</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
