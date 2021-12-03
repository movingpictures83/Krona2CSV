import sys

class Krona2CSVPlugin:
  def input(self, filename):
       self.myPhylum = dict()
       self.myClass = dict()
       self.myOrder = dict()
       self.myFamily = dict()
       self.myGenus = dict()
       self.mySpecies = dict()
       self.myStrain = dict()

       #total = 0.0
       self.kronafile = open(filename, 'r')

  def run(self):
   for line in self.kronafile:
    self.contents = line.strip().replace(',', '').split('\t')
    self.count = int(self.contents[0])
    self.highestindex = len(self.contents)-1
    if (self.highestindex == 4):
               prefix = "(Phylum)"
    elif (self.highestindex == 5):
               prefix = "(Class)"
    elif (self.highestindex == 6):
               prefix = "(Order)"
    elif (self.highestindex == 7):
               prefix = "(Family)"
    elif (self.highestindex == 8):
               prefix = "(Genus)"
    elif (self.highestindex == 9):
               prefix = "(Species)"
    else:
               prefix = "(Unclassified)"

    if (4 > self.highestindex):
        if (self.contents[self.highestindex].startswith('(')):
            mydata = self.contents[self.highestindex]
        else:
           mydata = prefix+self.contents[self.highestindex]
    else:
        mydata = self.contents[4]
    if (mydata in self.myPhylum):
       self.myPhylum[mydata] += self.count
    else:
       self.myPhylum[mydata] = self.count

    if (5 > self.highestindex):
        if (self.contents[self.highestindex].startswith('(')):
            mydata = self.contents[self.highestindex]
        else:
            mydata = prefix+self.contents[self.highestindex]
    else:
        mydata = self.contents[5]
    if (mydata in self.myClass):
       self.myClass[mydata] += self.count
    else:
       self.myClass[mydata] = self.count


    if (6 > self.highestindex):
        if (self.contents[self.highestindex].startswith('(')):
            mydata = self.contents[self.highestindex]
        else:
            mydata = prefix+self.contents[self.highestindex]
    else:
        mydata = self.contents[6]
    if (mydata in self.myOrder):
       self.myOrder[mydata] += self.count
    else:
       self.myOrder[mydata] = self.count

    if (7 > self.highestindex):
        if (self.contents[self.highestindex].startswith('(')):
            mydata = self.contents[self.highestindex]
        else:
            mydata = prefix+self.contents[self.highestindex]
    else:
        mydata = self.contents[7]
    if (mydata in self.myFamily):
       self.myFamily[mydata] += self.count
    else:
       self.myFamily[mydata] = self.count


    if (8 > self.highestindex):
        if (self.contents[self.highestindex].startswith('(')):
            mydata = self.contents[self.highestindex]
        else:
            mydata = prefix+self.contents[self.highestindex]
    else:
        mydata = self.contents[8]
    if (mydata in self.myGenus):
       self.myGenus[mydata] += self.count
    else:
       self.myGenus[mydata] = self.count


    if (9 > self.highestindex):
        if (self.contents[self.highestindex].startswith('(')):
            mydata = self.contents[self.highestindex]
        else:
            mydata = prefix+self.contents[self.highestindex]
    else:
        mydata = self.contents[9]
    if (mydata in self.mySpecies):
       self.mySpecies[mydata] += self.count
    else:
       self.mySpecies[mydata] = self.count


    if (10 > self.highestindex):
        if (self.contents[self.highestindex].startswith('(')):
            mydata = self.contents[self.highestindex]
        else:
            mydata = prefix+self.contents[self.highestindex]
    else:
        mydata = self.contents[10]
    if (mydata in self.myStrain):
       self.myStrain[mydata] += self.count
    else:
       self.myStrain[mydata] = self.count
    #total += self.count


  def output(self, filename):
       outprefix = filename
       outphylum = open(outprefix+".phylum.csv", 'w')
       outclass = open(outprefix+".class.csv", 'w')
       outorder = open(outprefix+".order.csv", 'w')
       outfamily = open(outprefix+".family.csv", 'w')
       outgenus = open(outprefix+".genus.csv", 'w')
       outspecies = open(outprefix+".species.csv", 'w')
       outstrain = open(outprefix+".strain.csv", 'w')

       startfirst = "\"\""
       startsecond = "\"Sample\""

       firstline = startfirst
       secondline = startsecond
       for phyla in self.myPhylum:
           firstline += ",\""+phyla+"\""
           secondline += ","+str(self.myPhylum[phyla])
       outphylum.write(firstline+"\n")
       outphylum.write(secondline)


       firstline = startfirst
       secondline = startsecond
       for theclass in self.myClass:
           firstline += ",\""+theclass+"\""
           secondline += ","+str(self.myClass[theclass])
       outclass.write(firstline+"\n")
       outclass.write(secondline)

       firstline = startfirst
       secondline = startsecond
       for order in self.myOrder:
           firstline += ",\""+order+"\""
           secondline += ","+str(self.myOrder[order])
       outorder.write(firstline+"\n")
       outorder.write(secondline)


       firstline = startfirst
       secondline = startsecond
       for family in self.myFamily:
           firstline += ",\""+family+"\""
           secondline += ","+str(self.myFamily[family])
       outfamily.write(firstline+"\n")
       outfamily.write(secondline)


       firstline = startfirst
       secondline = startsecond
       for genus in self.myGenus:
           firstline += ",\""+genus+"\""
           secondline += ","+str(self.myGenus[genus])
       outgenus.write(firstline+"\n")
       outgenus.write(secondline)


       firstline = startfirst
       secondline = startsecond
       for species in self.mySpecies:
           firstline += ",\""+species+"\""
           secondline += ","+str(self.mySpecies[species])
       outspecies.write(firstline+"\n")
       outspecies.write(secondline)


       firstline = startfirst
       secondline = startsecond
       for strain in self.myStrain:
           firstline += ",\""+strain+"\""
           secondline += ","+str(self.myStrain[strain])
       outstrain.write(firstline+"\n")
       outstrain.write(secondline)
