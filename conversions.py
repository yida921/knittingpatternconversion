from row import Row
from stitch import Stitch
import re

def flattoitr(pattern):
    """
    input string for pattern
    make a pattern for in the round
    """
    patternlist = cleanpattern(pattern)
    patternr = patternrows(patternlist)
    #doconversionhere
    new = []
    for row in range(len(patternr)):
        r = patternr[row]
        if row%2 == 1:
            r = r.opposite()
        new.append(r)
    return rowpatterns(new)


def itrtoflat(pattern):
    """
    opposite of flat to in the round
    """
    patternlist = cleanpattern(pattern)
    patternr = patternrows(patternlist)
    #doconversionhere
    new = []
    for row in range(len(patternr)):
        r = patternr[row]
        if row%2 == 1:
            r = r.opposite()
        new.append(r)
    return rowpatterns(new)

def upsidedown(pattern):
    """
    take a pattern and make it work the other way
    opposite of itself
    TODO how to do this
    http://thebuttonship.blogspot.com/2016/03/turning-lace-patterns-upside-down.html
    https://www.tienchiu.com/2004/08/reversing-knitting-patterns/
    """

def patternrows(patternlist):
    """
    takes a list of strings(per row) and returns a list of rows
    """
    for r in range(len(patternlist)):
        string = patternlist[r]
        patternlist[r] = Row(string)
    return patternlist

def cleanpattern(pattern):
    """
    TODO: patterns have a lot of irregularity, so this makes it so that the code works with it
    removes dupes ie. R1-4 becomes 4 diff rows
    idk how this is going to happen to this is gon be empty af rn
    returns a list of strings (per row)
    """
    out = pattern.lower().replace("[", "(").replace("]", ")").replace("knit", "k").replace("purl", "p").replace("row ", "r")
    out = out.split("\n")
    new = []
    for row in out:
        if "-" in row[:row.index(":")]:
            rowcounts = row.split("-")
            startr = int(rowcounts[0][1:])
            patternpiece = rowcounts[1].split(":")
            endr = int(patternpiece[0])
            for rnum in range(startr, endr+1):
                new.append(cleanrow("r"+str(rnum)+": " + patternpiece[1], new))
        else:
            new.append(cleanrow(row, new))
    return new

def cleanrow(row, rowlist):
    """
    handles various cleaning isnide row (rn just "times")
    """
    outone = row.split(":")
    out = re.split(r',\s*(?![^()]*\))', outone[1])
    for s in out:
        if "times" in s:
            repeat = s[s.index("(")+1:s.index(")")]
            times = s[s.index(")")+1:s.index("times")].replace(" ", "")
            r = [repeat for i in range(int(times))]
            if "," not in r:
                news = r[0]+times
            else:
                news = ", ".join(r)
            if "*" == s[0]:
                out[out.index(s)] = "*"+news
            elif "*" == s[-1]:
                out[out.index(s)] = news+"*"
            else:
                out[out.index(s)] = news
        if "repeat" in s:
            rowfind = int(s[s.index("repeat")+8:])-1
            repeatrow = str(rowlist[rowfind])
            out[out.index(s)] = repeatrow.split(": ")[1]
    return outone[0] + ": "+", ".join(out)

def rowpatterns(patternr):
    """
    takes list of rows and makes it stirng format
    managed repeating rows
    for now, does not condense rows beyond repeating rows one by one
    TODO further condensing (+ specs)
    TODO implement checks like rows in order 1,2, 3, etc
    """
    out = []
    outtrack = []
    for ro in range(len(patternr)):
        r = patternr[ro]
        if r in outtrack:
            out.append(str(r))
            # out.append("repeat r"+str(outtrack[outtrack.index(r)].l[0])[1:]) TODO this doesnt work
        else:
            out.append(str(r))
            outtrack.append(r)
    if len(out) == 1:
        return str(out[0])
    return "\n".join(out)
