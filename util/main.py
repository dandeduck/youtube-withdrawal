import pafy
import moviepy.editor as mpe

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    video = pafy.new('https://www.youtube.com/watch?v=OFr74zI1LBM&ab_channel=LaCha%C3%AEnedesmemes')
    video.getbestaudio().download(filepath='dick.mp3')
    video.getbestvideo().download(filepath='dick.mp4')

def mergeClips(videoPath, audioPath, outputPath):
    videoClip = mpe.VideoFileClip(videoPath)
    audioClip = mpe.VideoFileClip(audioPath)
    mergedClip = videoClip.set_audio(audioClip)
    mergedClip.write_videofile(outputPath)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
