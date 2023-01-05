import sounddevice as sd
from scipy.io.wavfile import write

def record_sample_and_save(save_path, n_times=100):
        for i in range( n_times):
            input(f'Press enter to record sample {i+1}/{n_times}')
            fs = 44100
            seconds = 2
            myrecording = sd.rec(int(seconds * fs), samplerate = fs,channels=1)
            sd.wait()
            write(save_path + str(i) + ".wav",fs,myrecording)

def prepare_data():

    n_times = 5
    root_path = "data/audio_data/"
    
    print("Recording the wake word")
    record_sample_and_save(root_path + "wake_word/",n_times)
    print("\n")
    print ("Recording the background sounds")
    record_sample_and_save(root_path + "background/",n_times)
    print("Finished...")

prepare_data()
