# This is a custom python package to handle CRUD Operations
import csv
def createBlog(*args):
    blog = {
        'title':args[0],
        'author':args[1],
        'body':args[2],
        'date':f'{args[3]}'
    }
    with open('./blogs.csv','r+') as f:
        writer = csv.DictWriter(f)
        writer.writerow(blog)