from datetime import datetime
def main():
	dt = datetime.now()
	print(dt) # 2026-08-24 14:28:58.444226
	print(dt.strftime("%Y/%m/%d %I:%M:%S %p")) # 2026-08-24 02:28:58 PM
	print(dt.strftime("%m/%d/%Y %H:%M:%S")) # 2026-08-24 14:28:58
	print(dt.strftime("%B %d, %Y (%A)")) # August 24, 2026 (Monday)
if __name__ == "__main__":
	main()