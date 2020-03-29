import time
import threading
from random import randrange


# Class for eating table, (shared variable)
class Table:
	def __init__(self, forks):
		# Array to represent the forks on table
		# 1 if the fork is busy
		# 0 if the fork is available
		self.forks = [0] * forks  

# Class for Process
class Process:
	def __init__(self, i):
		self.i = i  # The position of philosopher in the table
		self.right = 0  # right empty fork
		self.left = 0  # left empty fork
		print(f"Philosopher {i} created!")

	def rem(self, table):
		print(f"P: {self.i} is waiting")
		time.sleep(randrange(5)) # wait randome time
		self.tryin(table)

	def tryin(self, table):
		print(f"P: {self.i} is trying to eat")
		while True:
			# Check if the right fork es available
			if table.forks[self.i % len(table.forks) - 1] == 0:
				table.forks[self.i % len(table.forks) - 1] = 1;

				# Check if the left fork es available
				if table.forks[self.i + 1 % len(table.forks) - 1] == 0:
					table.forks[self.i + 1 % len(table.forks) - 1] = 1
					self.crit(table) # Enter Critical Region
					break
				
				# Give up and free the right fork
				else:
					table.forks[self.i] = 0

	def crit(self, table):
		print(f"P: {self.i} eating... in table {table.forks}")
		time.sleep(4)
		self.exit(table)

	def exit(self, table):
		# Free the forks left and right
		table.forks[self.i % len(table.forks) - 1] = 0
		table.forks[self.i + 1 % len(table.forks) - 1] = 0
		print(f"P: {self.i} finished")
		self.rem(table)


# Run program
if __name__ == '__main__':

	f = 5  # The number of forks in table
	n = 5  # The philosopher of forks in table

	table = Table(f)  # New eating table with f forks
	eaters = [Process(i) for i in range(n)] * n  # Create n philosophers
	print("\nInitial Table: ", table.forks)

	# Threading for multi-processing
	for eater in eaters:
		x = threading.Thread(target=eater.rem, args=(table,))
		x.start()




