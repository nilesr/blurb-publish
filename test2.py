import subprocess, glob, PIL.Image
size = "3138x4093"
subprocess.call(("convert -size "+size+" xc:white canvas.png").split())
for f in glob.glob("*.png"):
    try:
        idx = int(f.split("-")[1][:2])
    except:
        print("Failed for image " + f)
        continue
    geometry = []
    image = PIL.Image.open(f)
    if idx % 2 == 1:
        geometry = ["-geometry", "+" + str( int(size.split("x")[0]) - image.width ) + "+0"]
    subprocess.call(["convert", "-compress", "none", "canvas.png", f, *geometry, "-composite", f.replace(".png", "-2.png")])
