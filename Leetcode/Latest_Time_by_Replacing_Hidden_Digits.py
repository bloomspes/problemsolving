# You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).
# The valid times are those inclusively between 00:00 and 23:59.
# Return the latest valid time you can get from time by replacing the hidden digits.


class Solution:
    def maximumTime(self, time: str) -> str:
        hh, mm = time.split(":")
        hh, mm = list(hh), list(mm)

        if hh[0] == "?" and (hh[1] == "?" or int(hh[1]) < 4):
            # if int(hh[1]) < 4:
            hh[0] = "2"
        elif hh[0] == "?":
            hh[0] = "1"

        if hh[1] == "?":
            if hh[0] == "2":
                hh[1] = "3"
            else:
                hh[1] = "9"

        if mm[0] == "?":
            mm[0] = "5"

        if mm[1] == "?":
            mm[1] = "9"

        return ":".join(["".join(hh), "".join(mm)])
