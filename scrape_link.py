from bs4 import BeautifulSoup

html_document ='''<div class="row row-padded" style="margin-bottom: 15px;">
      <div class="col-md-7 col-sm-7">
       <h2>
        Runs Everywhere
       </h2>
       <p class="lead">
        Spark runs on Hadoop, Apache Mesos, Kubernetes, standalone, or in the cloud. It can access diverse data sources.
       </p>
       <p>
        You can run Spark using its
        <a href="/docs/latest/spark-standalone.html">
         standalone cluster mode
        </a>
        , 
      on
        <a href="https://github.com/amplab/spark-ec2">
         EC2
        </a>
        , 
      on
        <a href="https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html">
         Hadoop YARN
        </a>
        , 
      on
        <a href="https://mesos.apache.org">
         Mesos
        </a>
        , or 
      on
        <a href="https://kubernetes.io/">
         Kubernetes
        </a>
        .
      Access data in
        <a href="https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html">
         HDFS
        </a>
        ,
        <a href="https://alluxio.org">
         Alluxio
        </a>
        ,
        <a href="https://cassandra.apache.org">
         Apache Cassandra
        </a>
        ,
        <a href="https://hbase.apache.org">
         Apache HBase
        </a>
        ,
        <a href="https://hive.apache.org">
         Apache Hive
        </a>
        , 
      and hundreds of other data sources.
       </p>
      </div>'''

# collect the link from <a> tag
soup = BeautifulSoup(html_document, 'lxml')
a_tags = soup.find_all('a')
print(a_tags)
for a in a_tags:
    print(a['href'])