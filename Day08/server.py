import tensorflow as tf
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

X = tf.placeholder(dtype = tf.float32, shape = [None,4])
X = tf.placeholder(dtype = tf.float32, shape = [None,1])
a = tf.Variable(tf.random_normal([4,1]), dtype=tf.float32)
b = tf.Variable(tf.random_normal([1]), dtype=tf.float32)

y = tf.matmul(X,a) + b
saver = tf.train.Saver()

sess = tf.Session()
sess.run(tf.global_variables_initializer())

saver.restore(sess, 'model/saved.ckpt')

@app.route('/', methods=['GET','POST'])  # '/'로 들어오게 되면 호출
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        avg_temp = float(request.form['avg_temp'])
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

    data = [[avg_temp, min_temp, max_temp, rain_fall],]
    new_data = np.array(data, dtype=np.float32)
    result = sess.run(y, feed_dict = {X:new_data})
    price = result[0]
    return render_template('index.html',price=price)

if __name__ == '__main':
    app.run(debug=True)