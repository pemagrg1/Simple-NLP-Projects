#pip install pdfminer,cStringIO,re,docx2txt,dateparser

# -*- coding: utf-8 -*-
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re
import docx2txt
from dateparser.search import search_dates


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

pema = "RESUME-2.pdf"
myfile_name=pema
is_pdf = ".pdf" in myfile_name
text = docx2txt.process(myfile_name) if not is_pdf else convert_pdf_to_txt(myfile_name)

regex_mobile = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
regex_email = r'[\w\.-]+@[\w\.-]+'
regex_github = r'Github:\W.*'
regex_linkedin = r'Linkedin:\W.*'

regex_mobile_search = re.search(regex_mobile, text, re.IGNORECASE)
if regex_mobile_search:
    mobile = regex_mobile_search.group(0).replace("Mobile","").replace("E-MAIL","")
    mobile = mobile.encode('utf-8').replace(" • ","").replace(")","")
else:
    mobile = "-"

regex_email_search = re.search(regex_email, text, re.IGNORECASE)
if regex_email_search:
    email = regex_email_search.group(0).replace("E-MAIL","")
else:
    email = "-"

experience = ""
experience_date =""
try:
    regex_experience = r'EXPERIENCE(.*?\n)*COLLEGE-PROJECTS'
    experience_date = re.search(regex_experience, text, re.IGNORECASE)
    if experience_date:
        experience = (experience_date.group(0)).replace("COLLEGE-PROJECTS","")
        exp_date = search_dates(experience.decode('ascii','ignore'))
        if exp_date:
            experience_date = exp_date
        else:
            experience_date = "None"
    else:
        experience = None
except Exception, e:
    print e

if experience is None:
    try:
        exp1 = ((text.split("Experience"))[1].split("\n\n\n")[0])
        if exp1:
            experience = exp1
            exp_date = search_dates(experience)
            if exp_date:
                experience_date = exp_date
            else:
                experience_date = "None"
        else:
            experience = None
    except Exception, e:
        print e
new_experience_date =""
if len(experience_date) % 2 == 0:
    new_experience_date = experience_date
else:
    experience_date_list =['Present']
    for i in experience_date:
        experience_date_list.append(i)
    new_experience_date = experience_date_list

print "===MOBILE==\n",mobile
print "===email==\n",email
print "===Exp date==\n",new_experience_date 
print "===experience==\n",experience.replace("\n","")
