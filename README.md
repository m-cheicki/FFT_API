# FFT_API

A python API for Fast Fourier Transformation (FFT)

## How to use it

For the purpose of the demonstration, I have generated a signal by doing so :

```
SAMPLE_RATE = 1000
DURATION = 1

def generate_signal(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    y = np.sin(2*np.pi*freq*x)
    return x, y


_, signal1 = generate_signal(10, SAMPLE_RATE, DURATION)
_, signal2 = generate_signal(20, SAMPLE_RATE, DURATION)
_, signal3 = generate_signal(40, SAMPLE_RATE, DURATION)

signal2 = signal2 * 0.3
signal3 = signal3 * 1.3

signal = signal1 + signal2 + signal3
signal = signal.tolist()
```

Now that we have a signal, lets find its frequencies using the API.
You have to specify the `SAMPLE_RATE` and the `DURATION`, in seconds, of your sound, in addition to the `signal`. Here is the data we are going to give to our API :

````
SAMPLE_RATE = 1000
DURATION = 1

json_data = {
    'Signal': signal,
    'Sample_rate': SAMPLE_RATE,
    'Duration': DURATION
}
```

Finally, we make our POST request :

```
URL = "http://api.mcheicki.com/python/apis/fft/"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Charset': 'UTF-8'
}

json_data = json.dumps(json_data)
data_url = URL

r = requests.post(data_url, data=json_data, headers=headers)
print(r.text)

```

## Full example

````

import requests
import json
import numpy as np

SAMPLE_RATE = 1000
DURATION = 1

def generate_signal(freq, sample_rate, duration):
x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
y = np.sin(2*np.pi*freq*x)
return x, y

_, signal1 = generate_signal(10, SAMPLE_RATE, DURATION)
_, signal2 = generate*signal(20, SAMPLE_RATE, DURATION)
*, signal3 = generate_signal(40, SAMPLE_RATE, DURATION)

signal2 = signal2 _ 0.3
signal3 = signal3 _ 1.3

signal = signal1 + signal2 + signal3
signal = signal.tolist()

headers = {
'Content-Type': 'application/json',
'Accept': 'application/json',
'Accept-Charset': 'UTF-8'
}

json_data = {
'Signal': signal,
'Sample_rate': SAMPLE_RATE,
'Duration': DURATION
}

json_data = json.dumps(json_data)

data_url = "http://api.mcheicki.com/python/apis/fft/"

r = requests.post(data_url, data=json_data, headers=headers)
print(r.text)

```

```
