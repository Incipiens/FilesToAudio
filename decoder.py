import wave
import numpy as np
import sys

def wave_to_file(input_wave, output_file):
    # Open the wave file
    with wave.open(input_wave, 'rb') as wf:
        # Read frames and convert to byte array
        data = wf.readframes(wf.getnframes())
        data_array = np.frombuffer(data, dtype=np.uint8)

    # Write the binary data to output file
    with open(output_file, 'wb') as f:
        f.write(data_array.tobytes())

    print(f"Decoded {input_wave} to {output_file}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python decoder.py <input_wave.wav> <output_file>")
    else:
        wave_to_file(sys.argv[1], sys.argv[2])
