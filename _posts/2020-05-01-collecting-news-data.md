---
thumbnail: '/img/thumbnail-5.png'
keywords: ['https', 'article', 'www', 'websites', 'tijd']
layout: post
date: 2020-05-01 00:00:00 +0100
type: blog
title: "Collecting News Data"
---

We have been collecting data for the NWS Data project from Flemish news paper websites since December 2017. The following websites were included:


- [De Morgen](https://www.demorgen.be/)
- [De Standaard](https://www.standaard.be/)
- [De Tijd](https://www.tijd.be/)
- [Gazet van Antwerpen](https://www.gva.be/)
- [Het Belang van Limburg](https://www.hbvl.be/)
- [Het Laatste Nieuws](https://www.hln.be/)
- [Het Nieuwsblad](https://www.nieuwsblad.be/)
- [Metro](https://nl.metrotime.be/)

The core of the collection script reads the RSS-feeds of the websites every hour. All articles that have not yet been
seen are then collected. From the RSS-feeds themselves we can get the following fields:


- Which website published the article
- The link to the article
- The time of publication
- The title of the article
- An abstract of the article

Using the link to the article, a crawler that was made specifically for each new paper website, is deployed. This 
crawler extends the above information with the full text of the article. We also generate a unique identifier for the
article. The data packet is then written to a JSON file with one object per line for lazy loading.

So far the news paper articles make up some of the data used in 
[De Politieke Barometer](https://www.politiekebarometer.be/). We are also currently working on a rich dataset for a 
subset of the websites that adds information on cross-media visibility, news story placement and social media metrics. 
