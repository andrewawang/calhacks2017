import settings
import generator
import generatorBass
import generatorViolin
import threading
import time
from vision import object_tracking

settings.init()

pianoThread = threading.Thread(target=generator.run)
pianoThread.start()
saxThread = threading.Thread(target=generatorBass.run)
# saxThread.start()
violinThread = threading.Thread(target=generatorViolin.run)
violinThread.start()
object_tracking.cam_run()
