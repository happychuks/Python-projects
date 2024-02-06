#!/usr/bin/python3

import cmd

class Command(cmd.Cmd):
	"""this is a simple command line interpreter"""
	
	def do_sayHello(self, line):
		print("Hello there!")

	def do_EOF(self, line):
		print()
		return True

	def default(self, line):
		print(f"Unknown command entered: {line}")

if __name__ == '__main__':
	Command().cmdloop()
