#!/usr/bin/env python3

from sys import argv
from json import load
from json import dump

def load_mod_set():
	if len( argv ) < 2:
		return [ "base" ]
	with open( argv[ 1 ], 'r' ) as fh:
		return load( fh )

def load_mod_list():
	with open( 'mod-list.json', 'r' ) as fh:
		return load( fh )

def save_mod_list( data ):
	with open ('mod-list.json', 'w' ) as fh:
		dump( data, fh, indent = 4 )

def main():
	ms = load_mod_set()
	ml = load_mod_list()
	
	for index, mod in enumerate( ml[ "mods" ] ):
		enabled = mod[ "name" ] in ms
		mod[ "enabled" ] = { False: "false", True: "true" }.get( enabled )
	
	save_mod_list( ml )

	
if __name__ == "__main__":
	main()
