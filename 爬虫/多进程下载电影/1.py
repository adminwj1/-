import os
for num in range(13, 22):
	if not os.path.exists(str(num)):
		os.mkdir(str(num))