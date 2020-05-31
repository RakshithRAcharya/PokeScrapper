import cv2
import numpy as np
import urllib.request
import time
import threading
import math

def GetPokemon(start, end):
    print("Starting to collect images from ",start," to ",end)
    for i in range(start, end):
        try:
            url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) +'.png'
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            binary_str = response.read()
            byte_array = bytearray(binary_str)
            numpy_array = np.asarray(byte_array, dtype="uint8")
            image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
            cv2.imwrite("Images/" + '{:04d}'.format(i) + '.png', image)
            print('{:04d}'.format(i) + '.png')
        except Exception as e:
            print(str(e))


start_time = time.time()
thread_count = 16
image_count = 890
thread_list = []


for i in range(thread_count):
    start = math.floor(i*(image_count/thread_count))+1
    end = math.floor((i+1)*(image_count/thread_count))+1
    thread_list.append(threading.Thread(target = GetPokemon, args = (start, end)))


for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end_time = time.time()

print("DONE....")
print("Time Taken: " + str(end_time - start_time) + 'sec')