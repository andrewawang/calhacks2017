import multiprocessing
import time
import fluidsynth

data = (
    ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
    ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)



def mp_worker((inputs, the_time)):
    print " Processs %s\tWaiting %s seconds" % (inputs, the_time)
    time.sleep(int(the_time))
    print " Process %s\tDONE" % inputs
    
    fs = fluidsynth.Synth()
    fs.start()

    sfid = fs.sfload("example.sf2")
    fs.program_select(0, sfid, 0, 0)
    fs.noteon(0, 60, 30)
    fs.noteon(0, 67, 30)
    fs.noteon(0, 76, 30)

    time.sleep(1.0)

    fs.noteoff(0, 60)
    fs.noteoff(0, 67)
    fs.noteoff(0, 76)

    time.sleep(1.0)
    fs.delete()
    
def mp_handler():
    p = multiprocessing.Pool(2)
    p.map(mp_worker, data)

if __name__ == '__main__':
    mp_handler()
    
