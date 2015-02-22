import rumps, subprocess, pyaudio, wave, sys, time, os, difflib, requests, json
import speech_recognition as sr
from lxml import html

rumps.debug_mode(True)  # turn on command line logging information for development - default is off

def _bash(command_str):
	proc = subprocess.Popen(command_str, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	return_code = proc.wait()
	std_out = []
	std_err = []
	for line in proc.stdout:
		std_out.append(line.rstrip())
	for line in proc.stderr:
		std_err.append(line.rstrip())
	return (return_code, std_out, std_err)

def osascript(cmd):
	_bash("osascript -e '" + cmd + "'")
	print "osascript -e '" + cmd + "'"

@rumps.clicked('About')
def about(sender):
    _bash.call('say Dumble Abracadabra')

if __name__ == "__main__":

	data = json.loads(requests.get('https://api.github.com/gists/f07ace417e0d79fd7d79?client_id=c4a3c3c4ef3746889c43&client_secret=cff5d1d3a89253e3a8d91471b480a046ee4e1230').text)

	config = {}
	for filename in data['files']:
		if filename not in config.keys():
			config[filename] = []
		
		lines = requests.get(data['files'][filename]['raw_url']).text.split('\n')
		config[filename] += lines

	print "config: ", config

	app = rumps.App('Dumble', title='Listening...', icon='favicon.png')

	app.menu = [
		rumps.MenuItem('About', dimensions=(18, 18)),
		rumps.MenuItem('Listen', dimensions=(18, 18))
	]

	while True:
		try:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				print 'starting'
				audio = r.listen(source)
				print 'done'
				cmd = r.recognize(audio)
				print cmd

				try:
					_bash('say ' + cmd)
				except LookupError:
					_bash('say The wifi is really slow. Please try again.')
			
				if cmd in config.keys():
					print cmd
					osascript('\n'.join(config[cmd]))
					
				elif 'open' in cmd:
					app_name = cmd.replace('open ', '')
					print app_name

					osascript('activate application "' + app_name + '"')

					# for filename in os.listdir('/Applications'):
					# 	print filename
					# 	apps.append(filename)

					# closestMatch = difflib.get_close_matches(app_name, apps)
					# run('cd /Applications && open ' + closestMatch[0])

		except Exception, e:
			print e
			pass

	app.run()