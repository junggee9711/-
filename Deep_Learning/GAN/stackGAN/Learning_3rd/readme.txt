1. 훈련 전에,
   tensorboard = tf.summary.create_file_writer("logs/".format(time.time()))
   를 선언 했던 code 를 지우고,

   writer = tf.summary.create_file_writer("logs/".format(time.time()))  <-- epoch 반복 for 문 안에 writer 를 선언
   write_log(writer, 'discriminator_loss', np.mean(dis_losses), epoch)
   write_log(writer, 'generator_loss', np.mean(gen_losses[0]), epoch)
        
2. learning rate (lr) 을 0.0002에서 0.00008 로 바꿈

3. epochs 를 500 에서 200으로 바꿈
