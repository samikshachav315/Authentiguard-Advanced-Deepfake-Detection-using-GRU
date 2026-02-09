from model import build_gru_model
import numpy as np


X_train = np.random.rand(10, 30, 128)  # (samples, timesteps, features)
y_train = np.random.randint(0, 2, 10)

model = build_gru_model((30, 128))

model.fit(X_train, y_train, epochs=1, batch_size=2)

model.save("authentiguard_gru_model.h5")
