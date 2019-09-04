import numpy as np
import sklearn.cluster
import nltk
import distance
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))

text = """A virus injected directly into the bloodstream could be used to treat people with aggressive brain tumours, a study has found. Scientists from the University of Leeds and The Institute of Cancer Research in London have found that the naturally occurring virus could act as an effective immunotherapy in patients with brain cancer or other cancers that have spread to the brain. They showed that a type of virus called reovirus could cross the blood-brain barrier to reach tumours, where it is hoped they will replicate and kill the cancer cells. They also found that the virus was able to 'switch-on' the body's own defence systems to attack the cancer. The reovirus therapy could be used in conjunction with other cancer therapies to make them more potent - and a clinical trial is currently underway. Since the virus infects cancer cells and leaves healthy cells alone, patients receiving the treatment reported only mild flu-like side effects. Up to now, scientists thought it was unlikely that the virus would be able to pass from the blood into the brain because of the blood-brain barrier, a protective membrane around the brain. That would have meant that the only way they could get the virus into the brain was to inject it directly into the brain - which is challenging, would not be suitable for all patients, and cannot be regularly repeated. The research demonstrated that the virus could be administered through a single-dose intravenous drip. Nine patients took part in the study. They had cancers that had either spread to the brain from other parts of the body or were fast-growing gliomas, a type of brain cancer that is difficult to treat, and has a poor prognosis. All patients were due to have the tumours removed surgically. In the days before the surgeons operated, the patients were given the virus drip. Once the tumours were removed, samples were taken and analysed for signs that the virus had been able to reach the cancer, sometimes deep within the brain. In all nine patients, there was evidence that the virus had reached its target. The researchers also found that the presence of reovirus stimulated the body's own immune system, with white blood cells or 'killer' T-cells being attracted to the tumour site to attack the cancer. This is the first time it has been shown that a therapeutic virus is able to pass through the brain-blood barrier, and that opens up the possibility this type of immunotherapy could be used to treat more people with aggressive brain cancers, said Adel Samson, from University of Leeds. This study was about showing that a virus could be delivered to a tumour in the brain. Not only was it able to reach its target, but there were signs it stimulated the body's own immune defences to attack the cancer, said Samson."""
text = text.lower()
words = text.split(" ") #Replace this line
filtered = [w for w in words if not w in stopWords]
words = np.asarray(filtered) #So that indexing with a list will work
lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])

affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
affprop.fit(lev_similarity)
for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)
    #print(" - *%s:* %s" % (exemplar, cluster_str))
    print cluster_id,cluster_str
