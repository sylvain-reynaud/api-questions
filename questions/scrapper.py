import requests as rq
from bs4 import BeautifulSoup

HOST = "http://ici-grenoble.org"
DEBUG = False

def get_questions_from_website():
    r = rq.get(HOST + "/infospratiques/par-themes.php")
    s = BeautifulSoup(r.content, "html.parser")
    sujets = s.find("nav", id="sujets")
    themes = [(e.text.strip(), e.attrs['href']) for e in sujets.find_all("a")]
    # print(themes)

    questions = []

    for theme in themes:
        # print(theme)
        r = rq.get(HOST + theme[1])
        s = BeautifulSoup(r.content, "html.parser")
        section = s.find("section", id="sectionQR")
        questions_theme = [(e.text.strip(), e.attrs['href']) for e in section.find_all("a")]
        for question in questions_theme:
            # print(question)
            r = rq.get(HOST + '/infospratiques/' + question[1])
            s = BeautifulSoup(r.content, "html.parser")
            section = s.find("section", id="principal")
            corps = str(section)
            corps = corps[:corps.index('<h2')].replace('\n', '')
            # print(corps)

            q = {
                "theme": theme[0],
                "question": question[0],
                "corps": corps
            }
            questions.append(q)
            if DEBUG:
                return questions
    return questions
