from datetime import datetime
import time

if __name__ == "__main__":
    # get now time
    now = datetime.now()
    # convert time into timestamp
    timstart = datetime.timestamp(now)
    print("now is ", now,"<<<>", timstart)

    now_end = datetime.now()
    timend = now_end.timestamp()

    print('second ===>', int(timend - timstart))

    seconds = 100
    minutes, seconds =  divmod(seconds,60)
    hours, minutes = divmod(minutes, 60)
    print("%02d:%02d:%02d" % (hours, minutes, seconds))