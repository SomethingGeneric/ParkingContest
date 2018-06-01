from gmail import *

class EmailMsg:
  def __init__(self):
    x = open('passwd')
    passwd = x.read()
    x.close()
    self.oof = GMail('BCC Student Parking <parkingcontestfocs@gmail.com>',passwd)
  def set_msg(self,recv,subj,cont):
    self.msg = Message(subj,to=recv,text=cont)
  def send(self):
    self.oof.send(self.msg)
    
if __name__ == "__main__":
  e = EmailMsg()
  e.set_msg('mcompton2002@gmail.com','Hello?','Hello world?')
  e.send()
