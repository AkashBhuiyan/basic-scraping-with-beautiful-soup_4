from bs4 import BeautifulSoup

html_document = '''<div class="row row-padded">
      <div class="col-md-7 col-sm-7">
       <h2>
        Speed
       </h2>
       <p class="lead">
        Run workloads 100x faster.
       </p>
       <p class="lead1">
        Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine.
       </p>
      </div>
      <div class="story">
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

# search for all child

# div = soup.find('div', class_ = 'story')
#
# all_div_children = div.findChildren()
# print(all_div_children)
#
# # search for parent
#
# div = soup.find('div', class_='story')
# div_parent = div.findParent()
#
# print(div_parent)

# search for sibling

first_div = soup.find('p')
remain_sibling = first_div.findNextSibling()

print(remain_sibling)


