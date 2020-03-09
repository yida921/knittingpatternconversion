class Stitch():
    def __init__(self):
        self.name = None
        self.opposite = None
        self.count = -1

    def name(self):
        return self.name

    def opposite(self):
        return self.opposite

    def __str__(self):
        if self.count != -1:
            if type(self.count) == type(" ") and ":" not in self.count:
                # for k3, p5 etc
                return self.name+str(self.count)
            else:
                # for R1:
                return self.name+str(self.count)
        #for *
        return self.name

    def opp(self):
        if self.count != -1:
            if type(self.count) == type(" ") and":" not in self.count:
                return self.opposite+str(self.count)
            else:
                return self.opposite+str(self.count)
        return self.opposite

    def __eq__(self, obj):
        if isinstance(obj, Stitch):
            if self.name == obj.name and self.count == obj.count:
                return True
        return False

    @staticmethod
    def id(s):
        head = s.rstrip('0123456789:')
        tail = s[len(head):]
        if head == "k":
            return Knit(s)
        elif head == "p":
            return Purl(s)
        elif head == "*":
            return Star(s)
        elif head == "r" or head =="R":
            return RowNum(s)
        elif head == "ssk":
            return Ssk(s)
        elif head == "k2tog":
            return K2tog(s)
        elif head == "p2tog":
            return P2tog(s)
        elif head == "p2tog-tbl":
            return P2togTbl(s)
        elif head == "yo":
            return Yo(s)
        #TODO add more stitches

class Knit(Stitch):
    def __init__(self, stitch):
        self.name = "k"
        self.opposite = "p"
        self.count = stitch[1:] if len(stitch[1:]) != 0 else 1

    def __eq__(self, obj):
        if isinstance(obj, Knit):
            if self.name == obj.name and self.count == obj.count:
                return True
        return False


class Purl(Stitch):
    def __init__(self, stitch):
        self.name = "p"
        self.opposite = "k"
        self.count = stitch[1:] if len(stitch[1:]) != 0 else 1

    def __eq__(self, obj):
        if isinstance(obj, Purl):
            if self.name == obj.name and self.count == obj.count:
                return True
        return False


class Star(Stitch):
    def __init__(self, stitch):
        self.name = "*"
        self.opposite = "*"
        self.count = -1

    def __eq__(self, obj):
        if isinstance(obj, Star):
            if self.name == obj.name and self.count == obj.count:
                return True
        return False


class RowNum(Stitch):
    def __init__(self, stitch):
        self.name = "r"
        self.opposite = "r"
        self.count = stitch[1:]+" "

    def __eq__(self, obj):
        if isinstance(obj, RowNum):
            if self.name == obj.name and self.count == obj.count:
                return True
        return

class K2tog(Stitch):
    def __init__(self, stitch):
        self.name = "k2tog"
        self.opposite = "p2tog"
        self.count = stitch[5:] if len(stitch[1:]) != 0 else 1

class P2tog(Stitch):
    def __init__(self, stitch):
        self.name = "p2tog"
        self.opposite = "k2tog"
        self.count = stitch[5:] if len(stitch[1:]) != 0 else 1

class Ssk(Stitch):
    def __init__(self, stitch):
        self.name = "ssk"
        self.opposite = "p2tog-tbl"
        self.count = stitch[3:] if len(stitch[1:]) != 0 else 1

class P2togTbl(Stitch):
    def __init__(self, stitch):
        self.name = "p2tog-tbl"
        self.opposite = "ssk"
        self.count = stitch[9:] if len(stitch[1:]) != 0 else 1

class Yo(Stitch):
    def __init__(self, stitch):
        self.name = "yo"
        self.opposite = "yo"
        self.count = stitch[2:] if len(stitch[1:]) != 0 else 1
