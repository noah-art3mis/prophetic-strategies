import gensim

model = gensim.models.word2vec.Word2Vec.load("word2vec.model")

question = "hello"
qv = model.encode(question)
model.wv.similarity()