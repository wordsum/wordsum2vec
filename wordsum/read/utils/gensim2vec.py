# Open Story License
#
# Story: wordsum-python
# Writer: Kalab J. Oster(TM)
# Copyright Holders: Kalab J. Oster(TM)
# copyright (C) 2017 Kalab J. Oster(TM)
#
# Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
# if the humans or intelligent agents keep this Open Story License with the Story,
# and if the Story you tell remains free,
# and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.

import gensim
import logging
import os


'''
Train the model with lists of lists of sentences.

TODO: either by object or parameters set remaining Word2Vec parameters and check.
'''
def train_sentences(sentences):
    logging.debug("sentences: ", sentences)

    if not sentences is None:
        model = gensim.models.Word2Vec(sentences, size=100, alpha=0.025, window=5, min_count=1, max_vocab_size=None, sample=0.001,
                                       seed=0, workers=1, min_alpha=0.0001, sg=0, hs=0, negative=5, cbow_mean=1, iter=20, null_word=0,
                                       trim_rule=None, sorted_vocab=1, batch_words=10000, compute_loss=False)
    else:
        print("No sentences")
        model = None

    return model


'''
save the model locally to later use.
'''
def save_gensim2vec_model_binary(model, path, file):

    if not model is None:
        model.save(path + os.path.sep + file + ".bin")
    else:
        print("No model to save.")


'''
save the model to text file.
'''
def save_gensim2vec_model_text(model, path, file):

    if not model is None:
        model.wv.save_word2vec_format(fname=path + os.path.sep + file + ".txt", fvocab=None, binary=False)
    else:
        print("No model to save.")


