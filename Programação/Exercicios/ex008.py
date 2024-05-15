dm =float(input('Uma distância em metros: '))
dkm = dm/1000
dhm = dm/100
ddam = dm/10
ddm = dm*10
dcm = dm*100
dmm = dm*1000

print('A medidade {}m corresponde a \n {}km \n {}hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'.format(dm, dkm, dhm, ddam, ddm, dcm, dmm))