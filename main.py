import numpy as np


def read_filelist(signal):
    count = 0
    while True:
        for item in range(10):
            yield '%s%d%d' % (signal, count, item)
        # if count == 5 and single_pass == 1:
        #     break


def number_generator(prop_of_aux, single_pass=0):


    # while True:
    #     yield read_filelist('main').next()

    main_data_gen = read_filelist('main')
    if prop_of_aux is None:
        return main_data_gen.next()
    else:
        data_gen = [main_data_gen, read_filelist('aux')]
        # draw examples from aux_data with the probability of prop_of_aux
        while True:
            return data_gen[np.random.binomial(1, prop_of_aux)].next()

#
# gen = number_generator(None)
#
# for item in gen:
#     print(item)
elem = number_generator(0.5)
while True:
    print(elem)
