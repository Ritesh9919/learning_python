import time

attemt = 0
wait_time = 1
max_attemts = 5


while attemt < max_attemts:
    print("attemts", attemt + 1, "-", "wait time: ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attemt +=1
    
