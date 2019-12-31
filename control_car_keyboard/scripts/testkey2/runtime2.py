import time
start_time = time.time()
time.sleep(3)
print("--- %s seconds ---" % (time.time() - start_time))
print("time.time: ",time.time())
print("start_time ", start_time)
print("runtime: ",time.time() - start_time)