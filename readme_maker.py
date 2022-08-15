"""Kattis analyzer"""

import os
from string import ascii_uppercase, digits
from datetime import date

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

folders_to_search = digits + ascii_uppercase
files, without_ids, wrong_file_name = set(), set(), set()

# checking files in local repository:

for directory in folders_to_search:
    if os.path.exists(f"{os.getcwd()}/{directory}"):
        for file in os.listdir(f"{os.getcwd()}/{directory}"):
            with open(f"{os.getcwd()}/{directory}/{file}", "rt", encoding="utf-8") as opened:
                for i, line in enumerate(opened.readlines()):
                    if i == 2 and line.startswith("# "):
                        problem_id = line.replace("# ", "").strip()
                        files.add(problem_id)
                        break
                else:
                    without_ids.add(file)

            if file[:-3] != problem_id:
                # in case of FileExistsError just check it manually
                os.rename(f"{os.getcwd()}/{directory}/{file}", f"{os.getcwd()}/{problem_id[0].upper()}/{problem_id}.py")
                wrong_file_name.add(file)

    else:
        os.mkdir(f"{os.getcwd()}/{directory}")

if without_ids:
    print("Check files without proper id, there are ", len(without_ids), "such file(s)", without_ids)
if wrong_file_name:
    print("Check files with name different than id, there are", len(wrong_file_name), "such files(s)", wrong_file_name)

print("Total number of files analyzed:", len(files))

# scrapping all needed problem data from Kattis

all_problems, problems_html, pages = [], [], 0

while True:
    print(f"Downloading: page {pages}, downloaded problems {len(problems_html)}")
    downloaded = len(problems_html)

    URL = "https://open.kattis.com/problems" + f"?page={pages}"
    req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})

    page = urlopen(req).read()
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find("table", attrs={"class": "table2"})
    problems_html.extend(table.tbody.find_all("tr"))

    pages += 1

    if downloaded == len(problems_html):
        break

# cleaning downloaded data

difficulty = ""

for problem in problems_html:
    td = problem.find_all("td")

    minimum = td[5].text

    for i in ["easy", "medium", "hard"]:
        if minimum.endswith(i):
            difficulty = i
            minimum = minimum.replace(i, "")

    if "-" in minimum:
        minimum, maximum = minimum.split("-")
    else:
        maximum = minimum

    problem_id = str(td[0].a["href"].replace("/problems/", ""))

    all_problems.append(
        (
            problem_id,
            td[0].text,
            "https://open.kattis.com/problems/" + problem_id,
            minimum,
            maximum,
            difficulty,
            str(td[0].a["href"].replace("/problems/", "") in files),
        )
    )

# prepare local file with all problems data

with open("all.txt", "wt", encoding="utf-8") as handle:
    for problem in all_problems:
        handle.write("|".join(problem) + "\n")

# preparing readme.md with all solved problems

problems_done = list(filter(lambda x: x[6] == "True", all_problems))
date = date.today()
points = round(sum(map(lambda x: float(x[4]), problems_done)), 2)

with open("readme.md", "wt", encoding="utf-8") as handle:
    handle.write("# Welcome to the repository of solved challenges from Kattis Problems Archive\n")
    handle.write(f'### Total number of problems in this repository: {len(problems_done)}\n')
    handle.write(f'### Total number of points possible to obtain: {points}\n')
    handle.write(f'### Date of the last update: {date}\n\n\n')
    handle.write("Problem Id | Problem Title | Points | Difficulty | Solution\n")
    handle.write("--- | --- | --- | ---- | ---\n")
    for (problem_id, title, link, minimum, maximum, difficulty, done) in all_problems:
        if done == "True":
            row = f'[{problem_id}]({link} "{title}") | {title} | {maximum} | {difficulty} |' \
                  f' [Python 3](../main/{problem_id[0].upper()}/{problem_id}.py)\n '
            handle.write(row)
