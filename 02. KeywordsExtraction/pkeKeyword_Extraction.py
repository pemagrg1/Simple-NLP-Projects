import pke

# initialize keyphrase extraction model, here TopicRank
extractor = pke.unsupervised.TopicRank()
text = "Who is Barrack Obama"
# text = """काठमाडौं । अदालतले तोकेको दण्ड जरिबाना समयमा नबुझाउने व्यक्तिलाई सार्वजनिक सेवामा रोक लगाइने भएको छ । जिल्ला अदालत नियमावली २०७५ को नियम ८७ बमोजिम अदालतको दण्ड जरिबाना असुल हुन बाँकी व्यक्तिको लगत विवरणसहित सार्वजनिक सेवामा रोक लगाउने व्यवस्था गर्न लागिएक"""
f="test.txt"
file1 = open(f,"w")
file1.write(text)
file1.close()

extractor.load_document(input=f, language='en')
# keyphrase candidate selection, in the case of TopicRank: sequences of nouns
# and adjectives (i.e. `(Noun|Adj)*`)
extractor.candidate_selection()
# candidate_selection(self, pos=None, stoplist=None)
# candidate weighting, in the case of TopicRank: using a random walk algorithm
extractor.candidate_weighting()

# N-best selection, keyphrases contains the 10 highest scored candidates as
# (keyphrase, score) tuples
keyphrases = extractor.get_n_best(n=10)
print(keyphrases)
