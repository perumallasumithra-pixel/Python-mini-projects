data_file="tasks.txt"
tasks=[]
def load_task():
	try:
		file = open(data_file,"r")
		for line in file:
			tasks.append(line.strip())
		file.close()
	except FileNotFoundError:
		pass
def save_tasks():
	file=open(data_file,"w")
	for task in tasks:
		file.write(task+"\n")
	file.close()
def add_task():
	task=
