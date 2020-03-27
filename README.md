# Introduction

This project is a collaboration with [Dr. Anas Ghrab](http://anas.ghrab.tn/en/), professor of musicology at the Music Institute, University of Sousse, Tunisia.

The goal of this project is to analyze the [Saramusik digital corpus](http://saramusik.org/) using modern tools of data science, natural language processing and machine learning. Saramusik is an online catalogue of (mostly old) Arabic texts on music, with currently a few (less than 100) electronic texts, created and maintained by Dr. Anas Ghrab.

The documents are automatically pulled from the [Saramusik online database](http://saramusik.org/). The database currently comprises a little less than 50 documents, but is set to increase to hundreds of documents within a year. 

The documents are encoded in XML format based on the [Text Encoding Initiative (TEI)](https://tei-c.org/). In addition to the textual content of the document, each xml file contains some metadata such as the author, the source of the document, and a set of **tags** that indicate the genre(s) of the document.

Some of the preliminary research questions we aim to answer are:

1. Can we group the documents into a small number of groups (*clusters*) of documents with similar content?
2. Which vocabulary terms most/best characterize the content of each cluster?
3. How do these clusters correlate with other document characteristics, such as: i) tags, ii) geographic location, and iii) time period?  In other words, do documents of the same cluster necessarily have the same tags, or belong to the same time period?
