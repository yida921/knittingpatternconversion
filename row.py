from stitch import Stitch
import re

class Row:
    def __init__(self, string):
        self.string = string
        self.l = self.makestitches(string)

    def l(self):
        return self.l[:]

    def makestitches(self, string):
        """ makes self.l, list of stitches"""
        newstring = string.replace(" ", "").replace("*", ",*,")
        splitlist = re.split(r"[,:]", newstring)
        str_list = list(filter(None, splitlist))
        out = []
        for s in str_list:
            out.append(Stitch.id(s))
        return out

    def opposite(self):
        """returns new row flipped as a string"""
        new = []
        for s in self.l:
            if len(new) >1 and s.name is "*" and new[-1] == ", ":
                new.pop()
            new.append(s.opp())
            if new[-1][len(new[-1])-2:] != ": " and new[-1] != "*":
                new.append(", ")
        return Row("".join(new))

    def __str__(self):
        """ something like R1: *k3, p3* """
        out = [str(self.l[0])[:-1]+": "]
        for st in range(1, len(self.l)):
            s = self.l[st]
            if s.count != -1 and type(s.count) == type(" ") and ":" not in s.count:
                out.append(str(s))
                out.append(", ")
            else:
                if len(out)>0 and out[-1] == ", ":
                    out.pop()
                out.append(str(s))
        if out[-1] == ", ":
            out = out[:len(out)-1]
        return "".join(out)

    def __eq__(self, other):
        if isinstance(other, Row):
            return self.__str__() == str(other)
        return False
