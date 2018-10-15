from bs4 import BeautifulSoup

html_document = '''<div class="row row-padded">
      <div class="col-md-7 col-sm-7">
       <h2>
        Speed
       </h2>
       <p class="lead">
        Run workloads 100x faster.
       </p>
       <p class="lead">
        Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.
       </p>
      </div>
      <div class="col-md-5 col-sm-5 col-padded-top col-center">
       <div style="width: 100%; max-width: 272px; display: inline-block; text-align: center;">
        <img src="/images/logistic-regression.png" style="width: 100%; max-width: 250px;"/>
        <div class="caption" id="a1" style="min-width: 272px;">
         Logistic regression in Hadoop and Spark
        </div>
        <h1>hello</h1>
       </div>
      </div>
     </div>'''

soup = BeautifulSoup(html_document, 'lxml')

#Search firist one by class
p_tag = soup.find('p', class_ = 'lead')

print(p_tag)

#Searcg all by class
p_tag = soup.find_all('p', class_ = 'lead')

print(p_tag)

#search by id
div = soup.find_all('div',{'id':'a1'})
print(div)

#Search by string
a_string = soup.find_all('h1', string = 'hello')
print(a_string)
