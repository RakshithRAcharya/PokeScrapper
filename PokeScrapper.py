import cv2
import numpy as np
import urllib.request
import time

start_time = time.time()
for i in range(168, 890):
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
end_time = time.time()

print("DONE....")
print("Time Taken: " + str(end_time - start_time) + 'sec')
