#! /usr/bin/env python

from subprocess import call


class Archive:
	
	def __init__(self, directory):
		self.directory = directory

	def compress(self):
		call(["tar", "czf", self.directory + '.tar.gz', self.directory])

def main():
	archive = Archive("fakedirectory")
	archive.compress()

if __name__ == "__main__":
    main()
