import urllib2
import os

rawxml = urllib2.urlopen("http://www.dlrlondon.co.uk/xml/mobile/wst.xml").read()

xmllines = rawxml.split("\n")
nextline = 0
for x in xmllines:
    if nextline == 1:
        bits = x.split(" ")
        if bits[1] == "Bank" or bits[1] == "Stratford International":
            print x
            c = 0
            for bit in bits:
                c = c + 1
                if c > 3:
                    if bit.isdigit():
                        print bit
                        minstogo = int(bit)
                        if minstogo < 10:
                            # We are safe for now
                            # since we can just sox some single diget things into one
                            os.system("sox voice/intro.wav voice/"+str(minstogo)+".wav voice/mins.wav tmp/wat.wav")
                            os.system("aplay tmp/wat.wav")
        nextline = 0
    if "<div id=\"line1\">" in x:
        nextline = 1
    pass