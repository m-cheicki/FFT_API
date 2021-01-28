import os
import sys
import numpy as np
import numpy.fft as FFT
import json 

sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])

    if environ['PATH_INFO'] == '/python/apis/fft/' or environ['PATH_INFO'] == '/python/apis/fft': 

        if environ['REQUEST_METHOD'] == 'GET':
            data_sent = 'To make a POST request, you have to pass a JSON like : json_data = {"Signal": signal,"Sample_rate": SAMPLE_RATE,"Duration": DURATION} where signal is an array of float number, the sample_rate is the sample rate (int), and the duration is the duration of the sound in seconds.'

        elif environ['REQUEST_METHOD'] == 'POST':
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            request_body = environ['wsgi.input'].read(request_body_size)
            jdata = json.loads(request_body)
            signal = jdata['Signal']
            sample_rate = jdata['Sample_rate']
            duration = jdata['Duration']
            n = sample_rate * duration
            half_sr = int(sample_rate / 2)

            fft = FFT.fft(signal)
            frequencies = np.linspace(0, sample_rate, n, endpoint=False)
            frequencies = frequencies[0:half_sr]

            magnitude = (abs(fft)[0:half_sr] / n) * 2
            magnitude[0] = magnitude[0] / 2

            mask = magnitude > magnitude.std()
            print("Signal : " + str(len(signal)))
            print("Sample rate : " + str(sample_rate))
            print("duration : " + str(duration))
            print("Mask : " + str(len(mask)))
            print("FFT : " + str(len(fft)))

            freqs = frequencies[mask]
            

            data_sent = json.dumps({"frequencies": freqs.tolist()})

        else: 
            data_sent = {'method' : 'Other'}
    else: 
        data_sent = environ['PATH_INFO']

    return [str(data_sent).encode()]
