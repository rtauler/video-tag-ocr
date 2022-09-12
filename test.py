import os, time, shutil
from gen_frames import gen_frames

# iterate through videos dir and create folders with it's
directory = "videos"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f.endswith(".mp4"):
        print(f)
        # generate dir and 3 frames
        gen_frames(f)

        # enter in current filename dir and delete unnecessary frames
        currentdir, _ = os.path.splitext(filename)
        print(currentdir)

        os.rename(
            directory + "/" + currentdir + "/" + "0-00-00.20.jpg",
            directory + "/" + currentdir + ".jpg",
        )
        shutil.rmtree(directory + "/" + currentdir)
