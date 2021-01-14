import numpy as np
import numpy.fft as FFT


SAMPLE_RATE = 1000
DURATION = 1
N = SAMPLE_RATE * DURATION


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

fft = FFT.fft(signal)

frequencies = np.linspace(0, SAMPLE_RATE, N, endpoint=False)
frequencies = frequencies[0: int(SAMPLE_RATE / 2)]

magnitude = (abs(fft)[0:int(SAMPLE_RATE/2)] / N) * 2
magnitude[0] = magnitude[0] / 2

mask = magnitude > magnitude.std()
freqs = frequencies[mask]

print(freqs)
