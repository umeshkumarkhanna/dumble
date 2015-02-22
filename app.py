import rumps
import subprocess
import pyaudio
import wave
import speech_recognition as sr
import sys
import time
import os
import difflib

rumps.debug_mode(True)  # turn on command line logging information for development - default is off

def run(command_str):
	'''
	Given a shell command string, executes the command, waits for it to exit, then returns the
	return code, standard output, and standard error as a 3-tuple. The two outputs are returned
	as lists of str outputs, one line at a time in the order that they were printed.
	Command string input is executed in the default shell without question, the caller should ensure
	that the command is trusted for security reasons (not recommended to run arbitrary user input).
	'''

	proc = subprocess.Popen(command_str, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	return_code = proc.wait()
	std_out = []
	std_err = []
	for line in proc.stdout:
		std_out.append(line.rstrip())
	for line in proc.stderr:
		std_err.append(line.rstrip())
	return (return_code, std_out, std_err)


@rumps.clicked('About')
def about(sender):
    subprocess.call(['say', 'Dumble Abracadabra'])

@rumps.clicked('Listen')
def listen():
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 3
	WAVE_OUTPUT_FILENAME = "output.wav"

	if sys.platform == 'darwin':
	    CHANNELS = 1

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	print "* recording"

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print "* done recording"

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

	r = sr.Recognizer()
	with sr.WavFile("output.wav") as source: # use "test.wav" as the audio source
	    audio = r.record(source) # extract audio data from the file
	    cmd = r.recognize(audio)
	    print cmd

	    if 'open' in cmd:
	    	app_name = cmd.replace('open ', '')
	    	print app_name
	    	apps = []

	    	for filename in os.listdir('/Applications'):
	    		print filename
	    		apps.append(filename)

    		closestMatch = difflib.get_close_matches(app_name, apps)
    		run('cd /Applications && open ' + closestMatch[0])

	try:
		subprocess.call(['say', cmd])
		# app.title = cmd
		# time.sleep(2.5)
		# app.title = 'Opening...'

	except LookupError:                                 # speech is unintelligible
	    subprocess.call(['say', 'The wifi is really slow. Please try again.'])

if __name__ == "__main__":

	app = rumps.App('Dumble', title='Listening...', icon='favicon.png')

	app.menu = [
		rumps.MenuItem('About', dimensions=(18, 18)),
		rumps.MenuItem('Listen', dimensions=(18, 18))
	]

	with sr.Microphone() as source:
		while 1:
			try:
				listen()
			except:
				time.sleep(3)
				pass
	app.run()
	