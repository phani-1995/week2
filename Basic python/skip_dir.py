import os
print([f for f in os.listdir('/home/bridgelabz/Desktop/week2/Basic python')
       if os.path.isfile(os.path.join('/home/bridgelabz/Desktop/week2/Basic python', f))])
