import tensorflow as tf
import numpy as np


if __name__ == '__main__':

    batch_size = 2
    M = 3
    N = 4
    K = 5

    a = tf.random_normal([batch_size, N, M])
    b = tf.random_normal([M, K])
    c = tf.tensordot(a, b, axes=[-1, 0])

    with tf.Session() as sess:

        res = sess.run([a, b, c])
        for item in res:
            print(item, item.shape)

    val_a = res[0]
    val_b = res[1]

    print(np.matmul(val_a, val_b))

