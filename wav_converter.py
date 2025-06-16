import os
import sys

ffmpeg_path = sys.argv[3]
ffprobe_path = ffmpeg_path.replace("ffmpeg.exe", "ffprobe.exe")

os.environ["PATH"] = os.path.dirname(ffmpeg_path) + os.pathsep + os.environ["PATH"]

from pydub import AudioSegment

if __name__ == "__main__":

    src = sys.argv[1]
    dst = sys.argv[2]
    AudioSegment.converter = ffmpeg_path
    AudioSegment.ffprobe = ffprobe_path

    for i, fname in enumerate(os.listdir(src)):
        try:
            # convert mp3 to wav
            sound = AudioSegment.from_mp3(os.path.join(src, fname))
            print(f"Path to song {sound}")
            sound.export(os.path.join(dst, fname[:-4] + ".wav"), format="wav")
            print(f"Exported to {os.path.join(dst, fname[:-4] + '.wav')}")
        except Exception as e:
            print(f"Cannot convert {fname} to wav. Error: {e}")
            break
