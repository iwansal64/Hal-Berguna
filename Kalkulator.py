data = int(input(''))
data_operasi = input('+,-,*,:   ')
data2 = int(input(''))

if(data_operasi == '+'):
    hasil = data + data2
    print(data, '+', data2, '=', hasil)  

if(data_operasi == '-'):
    hasil = data - data2
    print(data, '+', data2, '=', hasil)

if(data_operasi == ':'):
    hasil = data / data2
    print(data, '+', data2, '=', hasil)


if(data_operasi == '*'):
    hasil = data * data2
    print(data, '+', data2, '=', hasil)