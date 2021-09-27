import datetime

class SystemInfo:
	def __init__(self):
		pass
	@staticmethod
	def get_time():
		"""
		This method returns the time when the user asks.
		"""
		answer = datetime.datetime.today().strftime("%I:%M %p")
		print(answer)
		return answer
