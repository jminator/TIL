from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import tensorflow as tf

seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

data_set = np.loadtxt()

X = data_set[:, 0:17]
y = data_set[:, 17]
print("X =>", X)
print("y =>", y)

# 모델의 설정
model = Sequential()
model.add(Dense(30, input_dim= 17, activation= 'relu')) # 입력층+은닉층
model.add(Dense(12, activation='relu')) # 은닉층
model.add(Dense(8, activation='relu')) # 은닉층
model.add(Dense(1, activation='sigmoid')) # 출력층
# dense(#of nodes, input_dim=#of indep.variables, activation=activation func.)
# #of nodes는 computing power가 허락하는 한으로 적당히 넣으면 된다.
# model.add(Dense(1, input_dim=17, activation='simoid')) 이렇게 출력층+입력층만 있어도 된다.

# 모델 실행
model.fit(X, y, epochs=3, batch_size=10) 
# 총 data 470개를 10개씩 읽어서 47번 읽으면 1epochs

#결과 출력
print("\n Accuracy: %.4f" (model.evaluate(X,y)[1]))

#모델 업데이트
#모델 저장 폴더 설정
MODEL_DIR = 'C:/Users/joosu/OneDrive/Documents/_사이버대학교/3학년 2학기/딥러닝/' 
if not os.path.exists(MODEL_DIR): 
    os.mkdir(MODEL_DIR)

# 모델 저장 조건 설정
modelpath = "C:/Users/joosu/OneDrive/Documents/_사이버대학교/3학년 2학기/딥러닝/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss',
verbose=1, save_best_only=True)

# 모델 실행 및 저장
model.fit(X, y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer])

# 모델 업데이트 그래프로 확인
df = df_pre.sample(frac=0.15) # 전체 샘플 중 15%만 호출
history = model.fit(X, y, validation_split=0.33, epochs=3500, batch_size=500)

# 모델 실행 및 저장
model.fit(X, y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer])

import matplotlib.pyplot as plt
y_vloss = history.history['val_loss']  #y_vloss에 테스트셋으로 실험 결과의 오차값을 저장
y_acc = history.history['acc']  # y_acc에 학습 set으로 측정한 정확도의 값을 저장
x_len = np.arange(len(y_acc))  # x값을 지정하고 정확도를 파란색, 오차를 빨간색으로 표시
plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
plt.plot(x_len, y_acc, "o", c="blue", markersize=3)

plt.show()