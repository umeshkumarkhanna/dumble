import subprocess

def shellj(command_str):
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


shellj('cd /Applications && open Slack.app')