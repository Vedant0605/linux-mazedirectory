import pickle
import os
import time



ANSWER_SKIP_PENALTY = 7
FLAG_BONUS = 5
HINT_PENALTY = 3
CORRECT_ANSWER_POINTS = 10






with open("Depend.pkl","rb") as file:
	dict1=pickle.load(file)
	dictQ=pickle.load(file)
	dictans=pickle.load(file)
	dicthint=pickle.load(file)
	dictflag=pickle.load(file)

class temp:
	def __init__(self,name,score,attempts,timelist):
		self.name=name
		self.timelist=timelist
		self.score=score
		self.attempts=attempts
		try:
			for x in range(7):
				if self.timelist[x]>1547180000:
					self.timelist[x]=0
		except:
			pass
		self.TotalTime=0
		for x in self.timelist:
			self.TotalTime=self.TotalTime+x

	def disp(self):
		print(f"Name:{self.name}")
		print(f"Score:{self.score}")
		print(f"Attempts:{self.attempts}")
		for i, x in enumerate(self.timelist):
			print(f"Q Time: {x}")
		print(f"Totaltime:{self.TotalTime}")
def main():
	attempts=1
	x=1
	adflag=0
	points=0
	name=input("Enter your name:")
	lsttime=[]
	t = time.time()
	while x!=8:
		t=time.time()
		print(f"Your Question:{dictQ[str(x)]}\n\nEnter Hint to get a hint(-3 points)\n")
		inp=input("Answer:")
		if inp.lower()=='adminexit':
			obj=temp(name,points,attempts,lsttime)
			for z in range(0,20):
				try:
					with open(f"score{z}.pkl","rb") as f:
						pass
				except:
					with open(f"score{z}.pkl","wb") as file:
						pickle.dump(obj,file)
						break
			x=8
			adflag=1
		else:
			if inp.lower()=='hint':
				points-=HINT_PENALTY
				os.system('clear')
				print(dicthint[str(x)])
			elif inp.lower()=='Answer skip'.lower():
				points-=ANSWER_SKIP_PENALTY
				flk=''
				print(f"\nGo to ",dict1[str(x)],"\n")
				while flk.lower()!="skip":
					flk=input("Enter the flag:")
					if flk==dictflag[str(x)]:
						points+=FLAG_BONUS
						os.system("clear")
						break
					elif flk.lower()=='skip':
						os.system('clear')
						print("\nFlag skipped\n")
					else:
						print("Incorrect flag!\nTo copy from terminal, select the flag and ctrl+shift+c")
				x=x+1
			else:
				if inp.lower()==dictans[str(x)].lower():
					os.system('clear')
					print(f"\nCorrect Answer!\nGo to ",dict1[str(x)],"\n")
					points+=CORRECT_ANSWER_POINTS
					lsttime.append(time.time() - t)
					print(f"\nTime taken for this Question: {time.time() - t} Seconds\n")
					fl=''
					while fl.lower()!="skip":
						fl=input("Enter the flag:")
						if fl==dictflag[str(x)]:
							points+=5
							os.system("clear")
							break
						elif fl.lower()=='skip':
							os.system('clear')
							print("\nFlag skipped\n")
						else:
							print("Incorrect flag!\nTo copy from terminal, select the flag and ctrl+shift+c")
					x=x+1
				else:
					os.system('clear')
					print("Wrong answer!")
					attempts+=1
	print("Congratulations!")
	if adflag==1:
		pass
	else:
		obj=temp(name,points,attempts,lsttime)
		for z in range(0,20):
			try:
				with open(f"score{z}.pkl","rb") as f:
					pass
			except:
				with open(f"score{z}.pkl","wb") as file:
					pickle.dump(obj,file)
					break
def read1():
	TOTAL=20
	objlst=[]
	for x in range(TOTAL):
		m='obj'+str(x)
		objlst.append(m)
	try:
		for x in range(TOTAL):
			with open(f'score{x}.pkl','rb') as file:
				objlst[x]=pickle.load(file)
			objlst[x].disp()
			print("\n\n")
	except:
		pass




def intro():
	text = """
	Each answer carries 10 points and each correct flag give you +5 points


	Enter In 'Answer skip' to skip the question with a 7 point penalty.
	Enter skip at flag prompt to skip flag (No +5 bonus).
	Enter hint to get a hint with a 3 point penalty.

	ENTER START:
	"""
	#print(text)
	inp = ""
	while inp.lower() != "start":
		inp = input(text)
		os.system('clear')

	main()


intro()
os.system('rm Depend.pkl')
read1()
