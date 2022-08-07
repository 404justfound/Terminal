import Help
import ip

print("""
███████╗██╗░░░░░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░██████╗░██╗░░░██╗  ██████╗░░█████╗░░██████╗██╗░░██╗
██╔════╝██║░░░░░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔════╝██║░░██║
█████╗░░██║░░░░░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░███████║██████╔╝░╚████╔╝░  ██████╦╝███████║╚█████╗░███████║
██╔══╝░░██║░░░░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██╔══██║██╔══██╗░░╚██╔╝░░  ██╔══██╗██╔══██║░╚═══██╗██╔══██║
███████╗███████╗███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░██║░░██║██║░░██║░░░██║░░░  ██████╦╝██║░░██║██████╔╝██║░░██║
╚══════╝╚══════╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝""")

location = 'C:/Windows/System32'

print("""ELEMENTARY FOUNDATIONS [Version Beta 0.1]
(c)Elementary Corporation. All rights reserved""")

ip.infoip()

cmd = True
while cmd:
	type_cmd = input(location + '> ')

	if (type_cmd == 'Exit'):
		cmd = False

	if (type_cmd == 'exit'):
		cmd = False

	if (type_cmd == "help"):
		Help.cmds()

	if (type_cmd == "Help"):
		Help.cmds()

	if (type_cmd == "man"):
		Help.cmds()

	if (type_cmd == "Man"):
		Help.cmds()

	if (type_cmd == "?"):
		Help.cmds()

	if (type_cmd == "about"):
		Help.about()

	if (type_cmd == "About"):
		Help.about()

	if (type_cmd == "infoip"):
		ip.infoip()