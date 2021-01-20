from flask import Flask, request, jsonify, render_template
import numpy as np
import numpy.fft as FFT

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET'])
def homepage():
    return "homepage"


@app.route('/api/', methods=['POST', 'GET'])
def api():
    data_sent = None
    if request.method == 'POST':
        data = request.get_json()

        signal = data['Signal']
        sample_rate = data['Sample_rate']
        duration = data['Duration']
        n = sample_rate * duration
        half_sr = int(sample_rate / 2)

        fft = FFT.fft(signal)

        frequencies = np.linspace(0, sample_rate, n, endpoint=False)
        frequencies = frequencies[0:half_sr]

        magnitude = (abs(fft)[0:half_sr] / n) * 2
        magnitude[0] = magnitude[0] / 2

        mask = magnitude > magnitude.std()
        freqs = frequencies[mask]

        data_sent = {'frequencies ': freqs.tolist()}

    else:
        data_sent = "GET"

    return data_sent


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
