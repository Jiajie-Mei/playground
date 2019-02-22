import numpy as np
import tensorflow as tf


batch_size = 2
max_step = 3
embedding_size = 4

np.random.seed(2376)

padding_mask = [
    sorted(np.random.binomial(1, 0.4, max_step), reverse=True)
    for i in range(batch_size)
]
padding_mask = tf.cast(padding_mask, tf.float32)

print(padding_mask)

fetched_embedding = np.random.normal(size=(batch_size, max_step, embedding_size))

print(fetched_embedding)

expanded_padding_mask = tf.expand_dims(padding_mask, axis=-1)

masked_embedding = tf.multiply(tf.cast(fetched_embedding, tf.float32), expanded_padding_mask)

sum_ = tf.reduce_sum(masked_embedding, axis=1)
average = tf.divide(sum_, tf.reduce_sum(padding_mask, axis=-1, keepdims=True))

with tf.Session() as sess:
    print(expanded_padding_mask.eval())
    print(masked_embedding.eval())
    print(average.eval())
