'''Author:Pema Gurung
Date: 6-9-17'''
# removing tags
text = """<div>
<h1>Title</h1>
<p>A long text........ </p>
<a href=""> a link </a>
</div>"""


#USING RE
import re
cleanr = re.compile('<.*?>')
cleantext = re.sub(cleanr, '', text)
print ("USING RE:",cleantext)


#using w3lib package
import w3lib.html
clean=w3lib.html.remove_tags(text)
print ("w3lib package:",clean)
