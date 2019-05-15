import _pickle as pickle

fn="articleLinks.dat"
with open(fn, 'wb') as filehandle:
    pickle.dump([], filehandle)

with open(fn, 'rb') as filehandle:
    print(pickle.load(filehandle))
