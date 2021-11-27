import keras
Savedmodel = keras.models.load_model('../../Models/Diagram_Identification.h5')
Savedmodel.summary()