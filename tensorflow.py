import tensorflow as tf 
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Attention 
from tensorflow.keras.models import Model 
from tensorflow.keras.preprocessing.sequence import pad_sequences 
# Define Transformer-based NMT model
encoder_inputs = Input(shape=(None,)) 
decoder_inputs = Input(shape=(None,)) 
embedding = Embedding(input_dim=vocab_size, output_dim=256) 
encoder_embedding = embedding(encoder_inputs) 
decoder_embedding = embedding(decoder_inputs) 
encoder_lstm = LSTM(256, return_sequences=True, return_state=True) 
encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding) 
decoder_lstm = LSTM(256, return_sequences=True, return_state=True) 
decoder_outputs, _, _ = decoder_lstm(decoder_embedding, 
initial_state=[state_h, state_c]) 
attention = Attention()([decoder_outputs, encoder_outputs]) 
decoder_dense = Dense(vocab_size, activation='softmax') 
outputs = decoder_dense(attention) 
model = Model([encoder_inputs, decoder_inputs], outputs) 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy') 
model.summary() 
