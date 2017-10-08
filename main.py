import settings
import generator
import generatorBass
import threading
import time
import object_tracking

settings.init()

musicThread = threading.Thread(target=generator.run)
musicThread.start()
bassThread = threading.Thread(target=generatorBass.run)
bassThread.start()
object_tracking.cam_run()
