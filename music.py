import time
import fluidsynth

SAMPLE_RATE = 44100
DELAY = 1/SAMPLE_RATE

fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload("example.sf2")
fs.program_select(0, sfid, 0, 0)
# fs.noteon(0, 60, 30)
# fs.noteon(0, 67, 30)
# fs.noteon(0, 76, 30)
# fs.noteon(0, 90, 30)
# fs.noteon(0, 100, 30)

# time.sleep(1.0)

# fs.noteoff(0, 60)
# fs.noteoff(0, 67)
# fs.noteoff(0, 76)

# time.sleep(1.0)

# fs.delete()

def sound_engine(numArr):
    for elem in numArr:
        fs.noteon(0, elem, 30)
        time.sleep(DELAY)
        fs.noteoff(0, elem)
        time.sleep(DELAY)

f = open("music_file.txt", "rb")
fileArr = []
try:
    byte = f.read(1)
    while byte != "":
        byte = byte.decode("ascii")
        # Do stuff with byte.
        try:
            fileArr.append(int(byte))
            print(byte)
        except ValueError:
            if byte == "\x00":
                fileArr.append(0)
            else:
                print("error: byte is ", byte)
        byte = f.read(1)
finally:
    f.close()
print(fileArr[:100])