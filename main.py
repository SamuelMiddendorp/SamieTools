from lib.helpers import *
import lib.open_file_module as ofm
def main():
	try:
		while True:
			x = input("")
			try:
				method = getattr(ofm, x)
				try:
					method()
				except:
					pass
			except:
				print("Invalid command")		
	except KeyboardInterrupt:
		print("Exiting...")

if __name__ == "__main__":
    main()