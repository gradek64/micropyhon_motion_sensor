from pydub import AudioSegment
from pydub.playback import play

print('class Sound')
class Sound:
    def __init__(self):
        #get ready sounds
        self.notify_ready = AudioSegment.from_mp3('sounds/ready_now.mp3')
        self.dog_barking = AudioSegment.from_mp3('sounds/dog-barking.mp3')
        #self.let_me_sleep = AudioSegment.from_mp3('sounds/let_me_sleep.mp3')
        self.video_recording = AudioSegment.from_mp3('sounds/video_recording.mp3')


    def playSound(self,whichSound):
        if whichSound == 'notify_ready':
            play(self.notify_ready)
        elif whichSound == 'dog_barking':
            play(self.dog_barking)
        elif whichSound == 'video_recording':
            play(self.video_recording)
        else:
            print('sound not found')
        

              