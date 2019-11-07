def to_dict(path, data):
    file = open(path, 'a')
    file.write(data)
    file.close


def from_dict(path):
    file = open(path, 'a+')
    dat_file = file.read()
    return dat_file

_dict = {'2019-11-04':[2,12]}
path = '/home/shreesh/Project/Performance-Stat/assets/temp/data_test.txt'

dat = from_dict(path)
to_dict(path, str(_dict))

print(type(dat))