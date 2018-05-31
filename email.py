from gmail import *
oof = GMail('Demo User <parkingcontestfocs@gmail.com>','thisisastrongpassword')
msg = Message('Test Message',to='Matt Compton <mcompton2002@gmail.com>',text='Hello')
oof.send(msg)
