import tensorflow as tf

a= tf.placeholder("float")
b= tf.placeholder("float")
c= tf.multiply(a,b)
sess= tf.Session()  #Session() 은 생성자 클래스가 존재해야한다.

print(sess.run(c, feed_dict={a:3, b:3}))
