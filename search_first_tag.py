from bs4 import BeautifulSoup

html_document = '''<div class="row row-padded">
      <div class="col-md-7 col-sm-7">
       <h2>
        Speed
       </h2>
       <p class="lead">
        Run workloads 100x faster.
       </p>
       <p>
        Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.
       </p>
      </div>
      <div class="col-md-5 col-sm-5 col-padded-top col-center">
       <div style="width: 100%; max-width: 272px; display: inline-block; text-align: center;">
        <img src="/images/logistic-regression.png" style="width: 100%; max-width: 250px;"/>
        <div class="caption" style="min-width: 272px;">
         Logistic regression in Hadoop and Spark
        </div>
       </div>
      </div>
     </div>'''

soup = BeautifulSoup(html_document, 'lxml')

#search for first tag

fist_p_tag = soup.find('p')
first_img_tag = soup.find('img')

number_of_div = len(soup.find('div'))

print(fist_p_tag)
print(first_img_tag)
print(number_of_div)