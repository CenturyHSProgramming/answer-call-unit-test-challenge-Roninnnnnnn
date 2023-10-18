# answerCall.py
# by Ronin Erkson

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)


def answerCall(caller_code, sameAreaCode, cur_time):
    response = False
    time = cur_time.split(":")
    hour = int(time[0])
    if hour <= 6 or hour >= 22:
        return response
    if caller_code == "T":
        return response
    if sameAreaCode:
        return True
    if caller_code == "F" or caller_code == "R":
        return True
    return response

if __name__ == '__main__':
    print(answerCall("U", False, "09:00"))
    print("How am I now?")
