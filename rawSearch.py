import json
class TFIDF():
    def __init__(self):
        with open('docs.json', 'r', encoding='utf-8') as f:
            self.docs = json.load(f)
        with open('ds.json', 'r', encoding='utf-8') as f:
            self.ds = json.load(f)
        with open('tf_idf_list.json', 'r', encoding='utf-8') as f:
            self.tf_idf_list = json.load(f)

    def search(self, q, k):
        results = []
        finals = []
        for _, document in self.docs.items():
          docs = document
          for i in range(len(docs)):
            score = 0
            for t in q.split():
              t = t.lower()
              score += self.tf_idf_list[t][str(i)] / self.ds[str(i)]
            finals.append((score, i))
        finals.sort(key=lambda x: -x[0])
        finals = finals[:k]
        results = [
            {
                "score": e[0],
                "idx": e[1],
                "text": docs[e[1]]
            }
            for e in finals
        ]
        return results




