import os
 
 
imgs = ['autumn.jpg', 'it-alps.jpg', 'railroad.jpg', 'seljalandsfoss.jpg', 'trees.jpg', 'canyon.jpg', 'ocean.jpg', 'road.jpg', 'storm-approaching.jpg', 'hills.jpg', 'sunrise.jpg']
 
with open('passwords.txt', 'r') as arquivo:
	passwd = arquivo.readlines()
 	
	for img in imgs:
		for pwd in passwd:
	 		os.system(f'steghide extract -sf {img} -p {pwd}')
 		
