import tkinter as tk

elements={'hydrogen':1,'helium':2,'lithium':3,'beryllium':4,'boron':5,'carbon':6,'nitrogen':7,'oxygen':8,'flourine':9,'neon':10,'sodium':11,'magnesium':12,'aluminum':13,'silicon':14,'phosphorus':15,'sulfur':16,'chlorine':17,'argon':18,'potassium':19,'calcium':20,'scandium':21,'titanium':22,'vanadium':23,'chromium':24,'manganese':25,'iron':26,'cobalt':27,'nickel':28,'copper':29,'zinc':30,'gallium':31,'germanium':32,'arsenic':33,'selenium':34,'bromine':35,'krypton':36,'rubidium':37,'strontium':38,'yttrium':39,'zirconium':40,'niobium':41,'molybdenum':42,'technetium':43,'ruthenium':44,'rhodium':45,'palladium':46,'silver':47,'cadmium':48,'indium':49,'tin':50,'antimony':51,'tellurium':52,'iodine':53,'xenon':54,'cesium':55,'barium':56,'lanthanum':57,'cerium':58,'praseodymium':59,'neodymium':60,'promethium':61,'samarium':62,'europium':63,'gadolinium':64,'terbium':65,'dysprosium':66,'holmium':67,'erbium':68,'thulium':69,'ytterbium':70,'lutetium':71,'hafnium':72,'tantalum':73,'tungsten':74,'rhenium':75,'osmium':76,'iridium':77,'platinum':78,'gold':79,'mercury':80,'thallium':81,'lead':82,'bismuth':83,'polonium':84,'astatine':85,'radon':86,'francium':87,'radium':88,'actinium':89,'thorium':90,'protactinium':91,'uranium':92,'neptunium':93,'plutonium':94,'americium':95,'curium':96,'berkelium':97,'californium':98,'einsteinium':99,'fermium':100,'mendelevium':101,'nobelium':102,'lawrencium':103,'rutherfordium':104,'dubnium':105,'seaborgium':106,'bohrium':107,'hassium':108,'meitnerium':109,'darmstadtium':110,'roentgenium':111,'copernicium':112,'nihonium':113,'flerovium':114,'moscovium':115,'livermorium':116,'tennessine':117,'oganesson':118}

def button_call(atom):
	try:
		type(int(atom))
		final_stage=atom
	except ValueError:
		type(atom)
		atom.strip()
		final_stage=elements.get(atom.lower().strip(), 1)
	config=int(final_stage)
	if config<=2:
		first_row(config)
	elif config>2 and config<=9:
		second_row(config)
	elif config>=10 and config<=17:
		third_row(config)
	elif config>=18 and config<=35:
		fourth_row(config)
	elif config>=36 and config<=53:
		fifth_row(config)
	elif config>=54 and config<=85:
		sixth_row(config)
	else:
		seventh_row(config)

def first_row(result):
	super=str.maketrans("12","¹²")
	configuration.config(text="1s"+str(result).translate(super))

def second_row(result):
	super=str.maketrans("123456","¹²³⁴⁵⁶")
	test=result-2
	if test<=2:
		addin=test
		configuration.config(text="1s²2s"+str(addin).translate(super)+" or\n[He]2s"+str(addin).translate(super))
	else:
		addin=test-2
		configuration.config(text="1s²2s²2p"+str(addin).translate(super)+" or\n[He]2s²2p"+str(addin).translate(super))

def third_row(result):
	super=str.maketrans("123456","¹²³⁴⁵⁶")
	test=result-10
	if test==0:
		configuration.config(text="1s²2s²2p⁶ or\n[Ne]")
	elif test<=2 and test>0:
		addin=test
		configuration.config(text="1s¹2s²2p⁶3s"+str(addin).translate(super)+" or\n[Ne]3s"+str(addin).translate(super))
	else:
		addin=result-12
		configuration.config(text="1s¹2s²2p⁶3s²3p"+str(addin).translate(super)+" or\n[Ne]3s²3p"+str(addin).translate(super))

def fourth_row(result):
	super=str.maketrans("1234567890","¹²³⁴⁵⁶⁷⁸⁹⁰")
	test=result-18
	if test==0:
		configuration.config(text="1s²2s²2p⁶3s²3p⁶ or\n[Ar]")
	elif test>0 and test<=2:
		addin=test
		configuration.config(text="1s²2s²2p⁶3s²3p⁶4s"+str(addin).translate(super)+" or\n[Ar]4s"+str(addin).translate(super))
	elif test>2 and test<=12:
		addin=test-2
		if addin==9:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s¹ or\n[Ar]3d¹⁰4s¹")
		elif addin==10:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s² or\n[Ar]3d¹⁰4s²")
		else:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d"+str(addin).translate(super)+"4s² or\n[Ar]3d"+str(addin).translate(super)+"4s²")
	else:
		addin=test-12
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p"+str(addin).translate(super)+" or\n[Ar]3d¹⁰4s²4p"+str(addin).translate(super))

def fifth_row(result):
	super=str.maketrans("1234567890","¹²³⁴⁵⁶⁷⁸⁹⁰")
	test=result-36
	if test==0:
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶ or\n[Kr]")
	elif test>0 and test<=2:
		addin=test
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶5s"+str(addin).translate(super)+" or\n[Kr]5s"+str(addin).translate(super))
	elif test>2 and test<=12:
		addin=test-2
		if addin==9:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰5s¹ or\n[Kr]4d¹⁰5s¹")
		elif addin==10:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰5s² or\n[Kr]4d¹⁰5s²")
		else:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d"+str(addin).translate(super)+"5s² or\n[Kr]4d"+str(addin).translate(super)+"5s²")
	else:
		addin=test-12
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰5s²5p"+str(addin).translate(super)+" or\n[Kr]4d¹⁰5s²5p"+str(addin).translate(super))

def sixth_row(result):
	super=str.maketrans("1234567890","¹²³⁴⁵⁶⁷⁸⁹⁰")
	test=result-54
	if test==0:
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰5s²5p⁶ or\n[Xe]")
	elif test>0 and test<=2:
		addin=test
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰5s²5p⁶6s"+str(addin).translate(super)+" or\n[Xe]6s"+str(addin).translate(super))
	elif test>2 and test<=16:
		addin=test-2
		if addin==1:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰5s²5p⁶5d¹6s² or\n[Xe]5d¹6s²")
		elif addin==2:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹5s²5p⁶5d¹6s² or\n[Xe]4f¹5d¹6s²")
		elif addin==3 and addin<=7:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f"+str(addin).translate(super)+"5s²5p⁶5d¹6s² or\n[Xe]4f"+str(addin).translate(super)+"6s²")
		elif addin==8:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f⁷5s²5p⁶5d¹6s² or\n[Xe]4f⁷5d¹6s²")
		else:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f"+str(addin).translate(super)+"5s²5p⁶6s² or\n[Xe]4f"+str(addin).translate(super)+"6s²")
	elif test>16 and test<=26:
		addin=test-16
		if addin==8:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d⁹6s¹ or\n[Xe]4f¹⁴5d⁹6s¹")
		elif addin==9:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰6s¹ or\n[Xe]4f¹⁴5d¹⁰6s¹")
		else:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d"+str(addin).translate(super)+"6s² or\n[Xe]4f¹⁴5d"+str(addin).translate(super)+"6s²")
	else:
		addin=test-26
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰6s²6p"+str(addin).translate(super)+" or\n[Xe]4f¹⁴5d¹⁰6s²6p"+str(addin).translate(super))

def seventh_row(result):
	super=str.maketrans("1234567890","¹²³⁴⁵⁶⁷⁸⁹⁰")
	test=result-86
	if test==0:
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰6s²6p⁶ or\n[Rn]")
	elif test>0 and test<=2:
		addin=test
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰6s²6p⁶7s"+str(addin).translate(super)+" or\n[Rn]7s"+str(addin).translate(super))
	elif test>2 and test<=16:
		addin=test-2
		if addin==1 or addin==2:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰6s²6p⁶6d"+str(addin).translate(super)+"7s² or\n[Rn]6d"+str(addin).translate(super)+"7s²")
		elif addin==3:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰5f²6s²6p⁶6d¹7s² or\n[Rn]5f²6d¹7s²")
		elif addin==4:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰5f³6s²6p⁶6d¹7s² or\n[Rn]5f³6d¹7s²")
		elif addin==5:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰5f⁴6s²6p⁶6d¹7s² or\n[Rn]5f⁴6d¹7s²")
		else:
			configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰5f"+str(addin).translate(super)+"6s²6p⁶7s² or\n[Rn]5f"+str(addin).translate(super)+"7s²")
	elif test>16 and test<=26:
		addin=test-16
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰5f¹⁴6s²6p⁶6d"+str(addin).translate(super)+"7s² or\n[Rn]5f¹⁴6d"+str(addin).translate(super)+"7s²")
	elif test>26 and test<=32:
		addin=test-26
		configuration.config(text="1s²2s²2p⁶3s²3p⁶3d¹⁰4s²4p⁶4d¹⁰4f¹⁴5s²5p⁶5d¹⁰5f¹⁴6s²6p⁶6d¹⁰7s²7p"+str(addin).translate(super)+" or\n[Rn]5f¹⁴6d¹⁰7s²7p"+str(addin).translate(super))
	else:
		configuration.config(text="Either the element doesn't exist or it is too big to know right now.")
window=tk.Tk()
window.title("Electron Configuration-v1.0.0")
window.geometry("650x175")

request=tk.Label(window, text="How many electrons are in the atom?", font=("Arial",20))
atom=tk.Entry(window, font=("Arial",20))
button=tk.Button(window, text="Configure", font=("Arial",20), command=lambda:button_call(atom.get()))
configuration=tk.Label(window,text="", font=("Arial",20))

request.pack()
atom.pack()
button.pack()
configuration.pack()

window.mainloop()