duit_awal = int(input('masukan saldo'))
if(duit_awal > 1000000):
    duit_awal = 1000000
print('duit awal', duit_awal)
print('===TOKO MAMA===')
print('1.Bakso 20.000\n2.Keju 25.000\n3.Tahu 20.000')
beli = input('<===Mau Beli Apa?')
berapa = int(input('\nberapa?'))
beli_olahan = beli.lower()

bakso = 20000
keju = 25000
tahu = 20000

if(beli_olahan == 'bakso'):
    if(duit_awal >= bakso):
         duit = duit_awal - (bakso * berapa)
         print('\nsisa saldo =', duit)
         data = input('CHECKOUT? y/n')
         if(data == 'y'):
             print('\n>==CHECKOUT==<')
             print(duit_awal, '-', bakso, 'x', berapa, '=', duit) 

    if(duit_awal < bakso):
        print('tidak cukup saldo!')
        data = input('Check saldo dan harga? y/n')
        if(data == 'y'):
            print('saldo =', duit_awal)
            print('harga =', bakso, 'x', berapa)

if(beli_olahan == 'keju'):
    if(duit_awal >= keju):
         duit = duit_awal - (keju * berapa)
         print('\nsisa saldo =', duit)
         data = input('CHECKOUT? y/n')
         if(data == 'y'):
             print('\n>==CHECKOUT==<')
             print(duit_awal, '-', keju, 'x', berapa,'=', duit) 

    if(duit_awal < keju):
        print('tidak cukup saldo!')
        data = input('Check saldo dan harga? y/n')
        if(data == 'y'):
            print('saldo =', duit_awal)
            print('harga =', keju, 'x', berapa)

if(beli_olahan == 'tahu'):
    if(duit_awal >= tahu):
         duit = duit_awal - (tahu * berapa)
         print('\nsisa saldo =', duit)
         data = input('CHECKOUT? y/n')
         if(data == 'y'):
             print('\n>==CHECKOUT==<')
             print(duit_awal, '-', tahu, 'x', berapa, '=', duit) 

    if(duit_awal < tahu):
        print('tidak cukup saldo!')
        data = input('Check saldo dan harga? y/n')
        if(data == 'y'):
            print('saldo =', duit_awal)
            print('harga =', tahu, 'x', berapa)
