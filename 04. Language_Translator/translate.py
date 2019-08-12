from googletrans import Translator
translator = Translator()
text="""पूरे देश में 24x7 बिजली देने के लिए केंद्र सरकार जल्द ही एक स्कीम लेकर आ रही है, जिसका ऐलान सोमवार को पीएम मोदी करेंगे। इस स्कीम को सौभाग्य के नाम से जाना जाएगा। उर्जा मंत्री आरके सिंह ने जानकारी देते हुए कहा कि दीनदयाल उपाध्याय के जन्मदिन पर यह स्कीम शुरू की जाएगी। केंद्र सरकार राज्यों के बिजली बोर्ड को ट्रांसफार्मर, मीटर, तार जैसे उपकरण लगाने पर सब्सिडी देगी।
"""
hi=translator.translate(text, dest='hi')
en=translator.translate(text, dest='en')
print(hi)
print(en)

'''
from googletrans import Translator
translator = Translator()
text="""おはようございます """
ja=translator.translate(text,dest='ja')
en=translator.translate(text,dest='en')
print(ja)
print(en)
'''

'''
el    : Greek,
eo    : Esperanto,
en    : English,
af    : Afrikaans,
sw    : Swahili,
ca    : Catalan,
it    : Italian,
iw    : Hebrew,
sv    : Swedish,
cs    : Czech,
cy    : Welsh,
ar    : Arabic,
ur    : Urdu,
ga    : Irish,
eu    : Basque,
et    : Estonian,
az    : Azerbaijani,
id    : Indonesian,
es    : Spanish,
ru    : Russian,
gl    : Galician,
nl    : Dutch,
pt    : Portuguese,
la    : Latin,
tr    : Turkish,
tl    : Filipino,
lv    : Latvian,
lt    : Lithuanian,
th    : Thai,
vi    : Vietnamese,
gu    : Gujarati,
ro    : Romanian,
is    : Icelandic,
pl    : Polish,
ta    : Tamil,
yi    : Yiddish,
be    : Belarusian,
fr    : French,
bg    : Bulgarian,
uk    : Ukrainian,
hr    : Croatian,
bn    : Bengali,
sl    : Slovenian,
ht    : Haitian Creole,
da    : Danish,
fa    : Persian,
hi    : Hindi,
fi    : Finnish,
hu    : Hungarian,
ja    : Japanese,
ka    : Georgian,
te    : Telugu,
zh-TW : Chinese Traditional,
sq    : Albanian,
no    : Norwegian,
ko    : Korean,
kn    : Kannada,
mk    : Macedonian,
zh-CN : Chinese Simplified,
sk    : Slovak,
mt    : Maltese,
de    : German,
ms    : Malay,
sr    : Serbian
'''
