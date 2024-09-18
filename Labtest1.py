import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter,filtfilt


def avg_aqi(smooth_signal):
    smooth_signal = smooth_signal_reshape(24,60)
    avg = np.mean(smoooth_signal)
    return avg



    
def main():
    np.random.seed(42)

    aqi_readings =  np.random.normal(50,20,1440)
    
    noise = np.random.normal(0,6,1440)


    noisy_aqi = (aqi_readings + noise)

    b, a = butter(0,0.05,btype="low")
    smooth_signal = signal.filtfilt(b,a,noisy_aqi)

    avg = avg_aqi(smooth_signal)
    print(f"Average Aqi readings: {avg}")
    

    threshold = 100
    above_threshold = smooth_signal > threshold
    exceeds_15_min = np.convolve(above_threshold, np.ones(15), mode='same') >= 15



    plt.fill_between(time,smooth_signal, where=exceeds_15_min, color='orange', label="AQI > 100 for >15 min", alpha=0.3)

    plt.figure(figsize=(10,0))
    plt.plot(noisy_aqi,label="noisy_aqi")
    plt.plot(smooth_signallabel="smooth_signal")
    plt.xlabel("Noisy Signal")
    plt.ylabel("Smooth Signal")
    plt.title("Data graph")
    plt.show()

    
main()
    
