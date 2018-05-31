from gmail import *

class heff:
  def __init__(self):
    self.oof = GMail('Parking Contest <parkingcontestfocs@gmail.com>','thisisastrongpassword')
  def set_msg(self,recv,subj,cont):
    self.msg = Message(subj,to=recv,text=cont)
  def send(self):
    self.oof.send(self.msg)
    
if __name__ == "__main__":
  e = heff()
  e.set_msg('mcompton2002@gmail.com','Hello?','Hello world?')
  e.send()
