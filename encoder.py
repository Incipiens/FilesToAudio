import wave
import numpy as np
import sys

def file_to_wave(input_file, output_file='output.wav'):
    # Read the input file in binary mode
    with open(input_file, 'rb') as f:
        data = f.read()

    # Convert binary data to numpy array of unsigned integers
    data_array = np.frombuffer(data, dtype=np.uint8)

    # Prepare wave file settings
    nchannels = 1
    sampwidth = 1  # Bytes
    framerate = 44100
    nframes = len(data_array)
    comptype = "NONE"
    compname = "not compressed"

    # Create a wave file
    with wave.open(output_file, 'w') as wf:
        wf.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
        wf.writeframes(data_array.tobytes())

    print(f"Encoded {input_file} to {output_file}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python encoder.py <input_file> <output_file.wav>")
    else:
        file_to_wave(sys.argv[1], sys.argv[2])
