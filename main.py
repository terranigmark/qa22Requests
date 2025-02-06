import data
import test_functions as tf


response_put = tf.update_product(99, data.galaxy_s24_updated)

print(response_put)
print(response_put.json())