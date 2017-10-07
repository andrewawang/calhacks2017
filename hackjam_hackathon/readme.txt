Introduction:
Hello, this is a project made for a hackathon hosted at Berkeley, so please pardon the messy and illegible code (but it won at least!).
This project uses a webcam to track the motion of an object and uses the data from the webcam to move the mouse. bringing the apple close to the webcam causes the mouse to left click, while bringing it far away and dragging up scrolls up, and bringing it far away and dragging down scrolls down.

Required files:
Most of the files are in the mouse folder however it requires opencv2 and python to run.

Instructions:
Run colormouse.py and a window will pop up showing you the output of your webcam. Adjusting the slides allows you to isolate specific colors while blacking out the rest of the webcam feed. We found that using bright and uncommon colored objects (we picked a bright green apple, creating the apple mouse!) made it easier to isolate those objects in our webcam feed.
You can use any brightly colored object you want as long as it's around the size of an apple. The program uses absolute sizing to determine what actions it should perform, so using a very large object would require you to step farther away to perform the same action as a small object from up close.

Once only your desired object is showing in the webcam feed, continue and start waving the object around.
Moving the object around 1 to 2 feet away from the camera causes the cursor to move along with it.
Moving the object very close to the camera causes the mouse to click at its current position.
Moving the object away, 3+ feet depending on the size of the object, and moving up will cause the mouse to scroll up, and moving down while far away causes the mouse to scroll down.

Credits:
Made by An Wang, Chris Lu, and Vasu M. Vikram.