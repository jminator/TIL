
from keras.models import Sequential
from keras.layers.core import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# seed값 설정
seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

df = pd.read_csv('C:/Users/joosu/OneDrive/Documents/_사이버대학교/3학년 2학기/딥러닝/iris.csv',
names = ["sepal_length", "sepal_width","petal_length","petal_width","species"])

#그래프로 확인
sns.pairplot(df, hue='species')
plt.show()

dataset = df.values
X = dataset[:, 0:4].astype(float)
y_obj = dataset[: ,4]

#문자열을 숫자로 변환
e = LabelEncoder()
e.fit(y_obj)
y = e.transform(y_obj)
y_encoded = np_utils.to_categorical(y)

print(e)
print(y)
print(y_encoded)

# 모델 설정
model = Sequential()
model.add(Dense(32, input_dim=4, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax')) # output의 종류가 3개이므로 마지막 node는 3이다.
# 시각화 해봤을때 구분선이 잘 그려질 것 같다면 dense가 그리 깊지 않아도 된다.


# 모델 컴파일
model.compile(loss='categorical_crossentropy', #softmax와 거의 짝을 이루는 함수이다.
optimizer='adam',
metrics=['accuracy'])

# 모델 실행
model.fit(X, y_encoded, epochs=10, batch_size = 10) 
# 총 150개의 data를 10번 분석해라 즉 1500번 읽어라. 
# batch_size가 작아질수록 큰 computing power요구
# epochs = 반복횟수
model.fit(X, y_encoded, validation_split=0.2, epochs=10, batch_size=10)

#결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X,y_encoded)[1]))