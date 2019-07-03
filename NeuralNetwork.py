# @Bright, create a Neural Network model and paste the code within this space.
# i would advise to avoid recurrent neural networks. Due to poor training data, RNNs may be to our disadvantage
# name the main model name : _model


'''
The following training data below should be used for a deep neural with at least 5 layers and 
trained to about a billion epochs for precision as only one instance of each prediction exists.
# This training data is aminly for testing.


_training_data = ['i am interested in programming what would you recommend i choose',
                  'hi',
                  'goodbye',
                  'i want to become a software engineer, what university do you recommend',
                  'where is the best country to study computer scoience',
                  'weldone']

_labels = [3, 0, 5, 1, 2, 4]



# The following training_data may be fine with the average neural network:

 _training_data = ['i am interested in programming what would you recommend i choose',
                  'i have an interest in electronics',
                   'where could i study computer science',
                   'what country',
                   'hey',
                   'goodbye',
                   'i want to become a software engineer, where do i go',
                   'i have an issue comprehending biology',
                   'what is the best university in the world',
                   'i dont like math but i love to draw what tould you recommend i choose',
                   'thank you',
                   'hi',
                   'hi, i want to become a software engineer, where do i go']
 _labels = [3, 3, 1, 2, 0, 5, 1, 4, 1, 3, 5, 0, 1]



'''

'''
To avoid diminishing return, you may need to devide the labels by a particular number. 
Assign that number to a variable and name it 'gradient_bias', as it would be imported in the main app (app.py).


# to preprocess the training data of your choice:

X = np.array([encode(sentences, word_bank) for sentences in _training_data]) # returns 2-dimentional array of training_samples
Y = np.array(_labels).reshape(len(_labels), 1) / gradient_bias
'''
