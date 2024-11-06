from datasets import load_dataset
import numpy as np
import numpy as np
import math
from collections import Counter
from scipy.sparse import csr_matrix, save_npz, load_npz

class TFIDF_search:
    def __init__(self):
        self.dataset = load_dataset('ILT37/viwiki', split='train')

    def clean_word(self,w):
        letters = set('aáàảãạăaáàảãạăắằẳẵặâấầẩẫậbcdđeéèẻẽẹêếềểễệfghiíìỉĩịjklmnoóòỏõọôốồổỗộơớờởỡợpqrstuúùủũụưứừửữựvwxyýỳỷỹỵz0123456789')
        new_w = ''
        for letter in w:
            if letter.lower() in letters or letter == '.':
                new_w += letter.lower()
        return new_w

    def preprocessing(self, docs):
        new_docs = []
        new_doc = ' '
        for i in range(len(docs)):
            doc = docs[i]
            doc = doc.replace('\n', ' ').replace('==', ' ')
            words = doc.split()
            for j in range(len(words)):
                word = self.clean_word(words[j])
                words[j] = word
            new_doc = new_doc.join(words)
            new_docs.append(new_doc)
        return new_docs
    
    def load_data(self):
        self.docs = self.preprocessing(self.dataset['text'])
        return self.docs

    def document_generator(self, chunk_size = 10000):
        for i in range(0, len(self.docs), chunk_size):
            yield self.docs[i:i+chunk_size]

    def preprocess(self, doc):
        return doc.lower().split()

    def compute_tf(self, tokenized_doc):
        term_count = Counter(tokenized_doc)
        total_terms = len(tokenized_doc)
        for term, count in term_count.items():
            tf = {term: count / total_terms}
        return tf

    def compute_df(self):
        df = Counter()
        for doc in self.load_data():
            unique_term = set(self.preprocess(doc))
            for term in unique_term:
                df[term] +=1
        return df

    def inverse_idf(self):
        for term, count in self.compute_df().items():
            idf = {term: math.log(len(self.docs)/count + 1)}
        return idf

    def save_tf_idf(self):
        terms = list(self.inverse_idf().keys())
        term_indices = {term: i for i, term in enumerate(terms)}
        rows, cols, data = [], [], []
        for doc_batch in self.document_generator(chunk_size=10000):
            for doc_index, doc in enumerate(doc_batch):
                tokenized_doc = self.preprocess(doc)
                tf = self.compute_tf(tokenized_doc)
                for term , tf_val in tf.items():
                    rows.append(doc_index)
                    cols.append(term_indices[term])
                    data.append(tf_val*self.inverse_idf()[term])
        tfidf = csr_matrix( (data, (rows, cols)), shape=(len(self.docs), len(terms)))
        save = save_npz("tf_idf.npz", tfidf)
        print("Saved successfully to npz file")
        return save

tf_idf = TFIDF_search()
print(tf_idf.save_tf_idf())