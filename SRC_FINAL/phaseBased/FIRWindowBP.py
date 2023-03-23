import numpy as np
import scipy.signal as signal


def FIRWindowBP(delta,  fl, fh ):
    timeDimension = 3
    len = delta.shape[2]

    # leng = shape(delta,2)
    # fl = 15
    # fh = 25
    fl = fl*2           #Scale to be fraction of Nyquist frequency
    fh = fh*2
    B = signal.firwin(len, cutoff = [fl, fh], window = 'blackmanharris', pass_zero = False)
    # M = shape(delta,0)
    M = delta.shape[0]
    batches = 20
    batchSize = np.ceil(M/batches)
    #B = B(1:leng)
    temp = fft(ifftshift(B))
    #transferFunction(1,1,:) = temp
    for k in range(1,batches):
        idx in range((1+batchSize*(k-1)) , (min(k*batchSize, M)))
        freqDom = fft(delta(idx,:,:), [], timeDimension)
        freqDom = freqDom. * tile(transferFunction, (shape(freqDom,0), shape(freqDom, 1)))
        del_temp = (ifft(freqDom,[],timeDimension))
        del_temp = del_temp.astype('float32')
        delta(idx,:,:) = del_temp.real
    return delta