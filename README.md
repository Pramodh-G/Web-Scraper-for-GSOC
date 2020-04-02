# Web-Scraper-for-GSOC
a web scraper program written so that one can find out who from IITK is offering projects in GSOC.

## Pre-Requisites : 
    - Python Interpreter (for version #### 3.6.9 or greater)

this repo contains 2 python scripts,them being:

## 1) webscraper.py :
                     this is a script that takes a link having a template like https://summerofcode.withgoogle.com/archive/2019/projects/
                     
## 2) JSONcsvCompare.py :
                          this is a script comparing the projects in the link with a list students in IITK.
                      
## Installation and Running :

- clone this repo.

- to run webscraper.py,run

```python
python3 webscraper.py
```
   Then input the url you want to scrape.
   for example:
```python
python3 webscraper.py
https://summerofcode.withgoogle.com/archive/2019/projects
```
this generates an output.csv file. 

- to run JSONcsvCompare.py,run

```python
python3 JSONcsvCompare.py
```
then input the names "output.csv" and "students.json".Make sure that both these files are in the same directory as the python script.

for example:
```python
python3 JSONcsvCompare.py
output.csv
student.json
```  
                       
                     
