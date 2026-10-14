import random
def main():
	print(random.random()) # 0.0 <= N <= 1.0
	print(random.uniform(-5, 5)) # -5.0 <= N <= 5.0
	print(random.randint(2, 7)) # 2 <= N <= 7
if __name__ == "__main__":
	main()