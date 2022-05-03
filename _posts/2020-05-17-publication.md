---
place: Proceedings of the 12th Web as Corpus Workshop
redirect: /files/KreutzDaelemans-3.pdf
layout: redirect-internal
date: 2020-05-17
type: publication
authors: ['Tim Kreutz', 'Walter Daelemans']
title: "Streaming Language-Specific Twitter Data with Optimal Keywords"
keywords: ['tweets', 'twitter', 'phrases', 'language', 'languages']
---

Introduction
============

Twitter data has frequently been used to study the public reaction to
specific topics or events @leetaru2013. In Natural Language Processing
this trend is mirrored in popular subtasks like sentiment mining and
event detection, and the appeal of tweets for these purposes is
understandable; they comprise abundant, open and mostly unfiltered
public feedback @barnaghi2016.

But collecting tweets for diverse purposes is no straightforward task.
Researchers ultimately make design choices on which keywords, hashtags
and users to search, without any gold standard reference to test the
resulting data snapshot. Additionally, not all tweets are made available
to the search index @twitter2019-1. Twitter is free to put any
restrictions on their results, whether it is on the maximum number of
hits or on how far back search results go.

As an alternative to the retrospective search approach, the Twitter
Streaming API @twitter2019-2 has been used to collect high-volume
language-specific corpora in real-time. By filtering the stream on a
list of frequent yet distinct keywords for a specific language, it is
possible to achieve high coverage of a reference set. Such lists of
keywords have been created for Dutch @tjongkimsang2013, Italian
@basile2013, German @scheffler2014, Hindi, Telugu and Bengali
@choudhary2018.

This paper offers three main improvements to the previous work. First,
we compare methods for selecting optimal keywords for creating
language-specific Twitter corpora. Second, we closely replicate the
real-world performance of these methods in our experimental setup so
that the limitations of the resulting corpora are known for any
downstream task. Third, although we conform to the Twitter Developer
Agreement @twitter2019-3 and will not share the language-specific
corpora, we do provide the lists of optimized keywords for the top 50
languages on Twitter and the code to generate lists for other languages.

Background
==========

Distribution of large collections of tweets is disallowed under the
Twitter Developer Agreement and Policy @twitter2019-3. Initiatives to
share large general-purpose Twitter collection, such as the Edinburgh
Twitter Corpus @petrovic2010 have been shut down under this regulation.

Consequently, studies on Twitter data have moved away from large scale
general-purpose collections to data snapshots designed for a specific
downstream task. Three main filtering approaches can be distinguished in
previous work.

Location-based Filtering

Twitter introduced an opt-in for sending location information with
tweets in 2009. This has allowed researchers to study language use
alongside fine-grained geographic distinctions.

Location-based filtering has proven invaluable for creating datasets for
dialectology with relatively low effort @eisenstein2010 [@huang2016].
show that location-based filtering can successfully be deployed for
studying language spread across country borders.

Location-based filtering is less suitable for creating language-specific
corpora. design filters based on the coordinates of major cities where
speakers of a target language are prominent. The resulting collections
were relatively pure for Arabic (99.9%) and Farsi (99.7%) but not for
Urdu (61.0%). Since a very low percentage (between 0.7% and 2.9%
depending on the country) of Twitter users enable location sharing,
filtering by location yields very low coverage @barbaresi2016.

User-based Filtering

Filtering by username is useful in cases where a very specific group of
users is targeted. collected tweets by Flemish politicians to analyze
which political issues were most often communicated, and whether this
aligned with their parties’ agenda.

used user-based filtering in conjunction with location-based filtering
to find tweets by Austrian Twitter users. The resulting collection had
mostly English (42.2%) language tweets.

Word-based Filtering {#section2.3}

Word-based filtering best suits the purpose of creating
language-specific corpora. was able to collect a near-complete snapshot
of German twitter messages by tapping the Streaming API for German
stopwords. They removed words from the list that are also frequent in
other languages (such as ‘war’ and ‘die’ for English) and extended it
with other frequent and distinctive German words. To test for coverage,
the collection obtained through word-based filtering was compared to
collections retrieved with location-based and user-based filtering
during the same time period. Only around 5% of German tweets was missing
from the collection obtained through word-based filtering.

Handpicked lists of filter words were also used for collecting Dutch
tweets @tjongkimsang2013. The authors add Twitter-specific terms, such
as trending Dutch hashtags, to their keywords but report that a lot of
other-language tweets still slip through the filter.

A more systematic approach can be found in . Cross-language homographs
were detected using Google Ngrams and removed from a list of most
frequent Italian words. Using only the top 20 of the remaining terms
yielded enough data for the eventual purpose of creating an Italian
corpus for sentiment analysis.

Toward Optimal Filtering

Previous work on word-based filtering has mostly been deployed as an
intermediate step for a downstream task. These papers understandably
deploy some heuristic method of selecting keywords, and usually do not
compare the resulting snapshot with a reference set.

instead focus solely on obtaining optimized keywords. Their list of
optimized keywords for Dutch outperforms the hand-picked list in in both
precision and recall. From intrinsic evaluation it is also clear that
the optimized list benefits from being generated on the domain it is
trying to retrieve.

We extend the work of by comparing additional optimization methods and
applying these to languages other than Dutch. In the process of
developing optimal lists that can be used to collect language-specific
Twitter corpora for the 50 most common languages on Twitter, we provide
the statistics that can be cited as limitations for these collections.

Data
====

To generate optimal keywords over Twitter data, we design an
experimental setup that mirrors the performance of the keywords on the
real-time stream.

Twitter API Constraints

The Twitter API imposes a 1% rate limit, and will automatically sample
down to the rate limit when more tweets pass the filter @twitter2019-2.
This puts a hard limit on the number of tweets that can be obtained for
the more dominant languages on Twitter. Language prevalence can be used
to determine the maximum coverage any filtering can achieve.

Language Prevalence

We collected tweets using the Twitter sprinkler @twitter2019-2 over a
period of six months from October 2017 to March 2018. The Twitter
Sprinkler is an access point of the Twitter Streaming API that can yield
1% of all tweets at any time. Filtering of the complete datastream can
be done by giving keyphrases, geo-locations, or user handles. We did not
apply any filtering to best approximate a random sample. This resulted
in roughly 570 million tweets.

Although Twitter predicts its own IETF language tags for most tweets, we
found on initial inspection that a pre-trained FastText language
identification model @joulin2017 identified a larger part of the tweets.
We think it is key to assign labels to difficult and even code mixed
tweets. These non-trivial cases crop up in the real-world setting and
cannot be ignored for generating keyphrases and for reporting their
performance.

The FastText (large) 176 ISO-tag model was used to assign silver labels
to each tweet. The tags come from a combination of the ISO 639-1 and ISO
639-2 standards found on the FastText website @fasttext. Table [table1]
shows the language prevalence of the five most and the five least
identified languages. FREQ is the relative frequency over our entire
dataset. MEAN is the relative frequency averaged per hour and better
reflects language prevalence normalised over time. MEAN can be used to
determine how many tweets cannot be retrieved due to the 1% rate limit.
MAX shows the maximum hourly relative frequency. Languages that never
surpass the 1% rate limit throughout the day can theoretically be
collected in full.

The Table [table1] rankings partially correspond to earlier analyses of
the language composition of Twitter. Two notable differences are the
increase in the number of Arabic tweets, and a decline in English
language tweets compared to a 2011 study @hong2011. We expect these
differences to be due to increased popularity of Twitter in Arabic
countries while the U.S. user base stagnated @semiocast2011
[@bloomberg2019]. However, differences can also be due to the FastText
model identifying more tweets (roughly 9%) than the IETF labels used in
.

Experimental Setup

After removing retweets, 10,000 tweets were sampled for the 50 most
frequent languages. Non-target language tweets were added conform to the
language distributions. For example, since Spanish tweets represent
roughly 9.52% of the stream, we sampled 105,042 ($\frac{10000}{0.0952}$)
other-language tweets. Since more infrequent languages greatly inflate
the number of other-language tweets supplemented in their dataset, we
opted for a cut-off after the 50 most frequent languages.

We created development and test data in a similar way, by sampling
roughly 5,000 target language tweets and adding other language tweets
based on their distribution.

While creating separate data sets for each of the targeted languages may
seem extraneous, we opted for this approach because it would guarantee
that key phrase lists would be sampled from roughly the same number of
tweets for each language. This way, the quality of key phrases can never
be attributed to differences in data size.

Preprocessing

In preparation of generating and testing keywords, tweets are parsed
according to Twitter documentation @twitter2019-3. Tweets were
lowercased and any punctuation except @ (for mentions of other users)
and \# (for hashtag topic markers) were removed.

Methods
=======

The Twitter API allows an input of up to 400 60-byte strings.
Disjunctive search is performed between the 400 inputs, and any tweet
matching the conjunctive presence of tokens in an input is retrieved
@twitter2019-3. From now on, string inputs will be referred to as *key
phrases*.

We generate token *powersets*; exhaustive combinations of tokens present
in the target language tweets. The notion is that each token combination
generated from a tweet can be used as a key phrase to retrieve that
tweet from the stream. Each key phrase is thus associated with a set of
target- and other-language tweets, and in extension a recall and
precision score.

Maximum Coverage of Tweets

Optimal key phrases maximally cover the set of target language tweets,
whilst limiting the number of other-language tweets retrieved. The
latter consideration is especially important considering the 1% rate
limit. Key phrases that confuse target language tweets with other
(dominant) languages can lead to results that are not only impure, but
also incomplete due to down-sampling.

Formally, we consider a collection of key phrases $K$, generated from a
target language $l$, $K^l = \{K^{l}_1, K^{l}_2, ..., K^{l}_n\}$ and a
parallel collection $T$ of sets of tweets identified by those phrases,
$T = \{T_1, T_2, ..., T_n\}$. We compare algorithms for selecting up to
400 phrases from $K$ to optimize a variety of objectives to target set
$T^l$.

[H]

<span> $bestscore\gets0$ $bestphrase\gets None$ <span> </span>
$bestphrase$ </span> <span> $O\gets\varnothing$ <span> Remove tweets
covered by $O$ from every set in $T$.\
Add to $O$. </span> $O$ </span>

[figure1]

Scoring Functions {#section4.2}

In its classic setting a maximum coverage problem optimizes recall over
a target set. Since we also care about precision, we design scoring
functions to reflect this objective alongside the naive optimization of
recall and precision:

1.  [scoring1]Optimize Recall ($R$)

2.  [scoring2]Optimize Precision ($P$)

3.  Optimize Recall, but ensure a precision threshold of .9 for each
    phrase ($R_p$)

4.  [scoring4]Optimize Precision, but ensure a recall threshold of .01
    for each phrase ($P_r$)

5.  Weight Precision^$\beta$^ by Recall. Higher $\beta$ adds more
    importance to precision ($P^\beta*R$)

Although F-score seems like another likely candidate for scoring key
phrases, its reliance on a balanced recall and precision, even in
adaptations like F-beta where precision receives more weight, make it
unsuitable. We demonstrate the pitfall of reliance on recall
sufficiently with scoring functions [scoring1] and [scoring4].

Greedy Selection

We consider only a greedy approach to selecting key phrases, due to the
huge number of candidates. Greedy optimization of maximum coverage
problems is shown to be the best approximation algorithm in polynomial
time @feige1998. The greedy algorithm iteratively picks a key phrase
according to a scoring function from the preceding list. The covered
tweets are then removed and scores are recalculated before picking the
next phrase (Figure [figure1]).

Baselines

Naive scoring functions [scoring1] and [scoring2] can be expected to
perform poorly for the task of creating language-specific Twitter
corpora. We expect optimization over recall to select the stopwords that
best identify a target language in addition to other generic terms such
as partial URLs. Optimizing precision conversely can yield some terms
occurring in only a few tweets.

For more reasonable baseline behavior we draw from previous work in
word-based filtering of tweets in Section [section2.3] First, keyword
lists are compiled from the 400 most frequent tokens in a target
language training set in line with . These lists are then filtered for
cross-language homographs for the second baseline. However, making
corrections for each language by hand as seen for Dutch
@tjongkimsang2013 and German @scheffler2014 would require significant
language expertise and time investment. We instead assure that none of
the 400 selected words are present in the 1000 most frequent terms of
non-target languages. This automatic filtering of frequent terms is
comparable to what has been done for Italian @basile2013.

Results
=======

In this section we first qualitatively analyze the key phrases selected
by the different scoring functions. Some expected drawbacks of each of
the greedy selection approaches have been formulated in the previous
section, and are tested by manual inspection.

We do not assume that scoring functions perform uniformly for each
target language. Specifically, we expect a prevalence effect whereby
language that are more common on Twitter would benefit from higher
precision phrases as confusion with other languages is more costly.
False positives fill up the stream permitted by the Twitter rate limit
and would lower overall performance. For rarer languages, this is less
important. The $P^\beta*R$ scoring function will be grid-searched for
individual languages on the development data to choose a $\beta$ value.

Languages that have drastically different performance from the mean
warrant closer inspection with confusion matrices. We hypothesize that
languages that have multiple very closely related languages in the data
set score lower due to frequent confusion with those languages.
Alternatively, relatively bad performance can be due to
under-representation in the data. Languages that are less common on
Twitter run a higher risk of selecting false positives with their key
phrases.

Finally, we compare the best greedy selection algorithm with the
proposed baseline methods on the test data.

Phrase Lists

Consider the outcome for English of the 50 phrases based on recall and
precision in Figure [figure2].

[figure2]

As expected, the top 50 phrases selected based on their recall contain
stopwords and partial URLs. We find some other interesting
Twitter-specific terms such as the hashtag \`\`*\#iheartawards*“ and
chat speak \`\`*lol*”, \`\`*twt*“ and \`\`*ng*”.

The phrases selected by precision instead contain n-grams that combine
stop words with partial URLS and less frequent words that are more
distinct for English.

Prevalence effect

Positioned between the precision and recall scoring functions is the
selection procedure that weights precision by itself and by recall. By
taking an exponentiation of precision we increase its effect in the
optimization function, which may be prudent after seeing the
non-distinctive selections by recall in the previous section.

The importance of increasing the weight of precision over recall may
differ between languages. Instead of looking at any individual language
we test three configurations ($P^1$, $P^2$ and $P^8$) on languages
binned by their frequency rank from Table [table1].

Figure [figure3] shows that a $\beta > 1$ increases performance for the
most common language on Twitter. In the ranks 20-30, however, scoring
key phrases on their precision weighted by recall performs best. There
are no big differences between values of $\beta$. We opt to use $P^2*R$
for the top 25 languages and $P*R$ for the less common languages in our
final scoring function.

coordinates <span> (1,0.022)(2,0.368)(3,0.699)(4,0.597)(5,0.802)
</span>;

coordinates <span> (1,0.142)(2,0.729)(3,0.670)(4,0.559)(5,0.800)
</span>;

coordinates <span> (1,0.168)(2,0.737)(3,0.638)(4,0.523)(5,0.800)
</span>;

Development Set Performance

Table [table2] lists the macro averaged performance for each of the
proposed scoring functions. Besides recall we shows *bound recall*,
which is the performance of the key phrases under the Twitter rate
limit.

Since optimizing recall yields a lot of non-distinctive terms, the
retrieved set of tweets proves impure and recall drops when we take the
1% rate limit into account. This is also the case when optimizing
precision but respecting a minimum recall threshold of .01.


The three other scoring functions perform better. Simply selecting key
phrases on their precision leads to a high precision overall. The
yielded 400 high-precision phrases also cover a reasonably large part of
the target language tweets (58.67%). The function that selects phrases
on the basis of their precision but only considers those with a
precision higher than 90% performs comparably.

The best overall strategy is scoring phrases on their precision weighted
recall with a variable $\beta$. Most importantly, this scoring function
has the highest recall, even when subject to the Twitter rate limit. We
argue that this is usually the objective of collecting Twitter data for
a particular target language. For experiments on the test set, we use
those lists of key phrases yielded by optimizing in this manner.

Test Set Performance

Table [table3] shows the best greedy algorithm performance on the test
set compared to the baselines. Even when selecting the best scoring
function on the basis of development set results, it seems that the key
phrases performed consistently. There is not big difference between
their performance on the development set and the test set.

The macro-averaged scores reported until now are useful in selecting the
best general algorithm, but as can be seen in the full results in
Appendix Table [appendixb], there is a huge prevalence effect on
individual target languages.

Even when accounting for the limit on number of tweets returned at any
time, there is some variability in results between individual languages.
We look at some of the outliers in detail in the next section.

Discussion
==========

Performances for each of the target languages are recorded in Appendix
Table [appendixb], and show that while mostly consistent, some outlier
results make it harder to discuss findings in a general way.

We mentioned the prevalence effect on recall earlier and thus focus on
results that were unexpected with regards to language with similar
frequencies on Twitter, specifically Chinese (zh), Esperanto (eo),
Galician (gl) and Azerbaijani (az).

Confusion matrices

Table [table4] shows the binary confusion matrices for four outlier
results with the three most confused languages. Closer inspection of the
confused tweets and selected key phrases give insight into two types of
error.

First, for Chinese (zh), tokenization turned out to be a problem. We
adopted the Twitter standard from @twitter2019-2, which is less suitable
for logographic or abjad writing systems. For Japanese, Thai, Korean,
Arabac and Hewbrew this turned out not to affect results in any
noticeable way. Chinese gets confused often for these other languages
however, and only a small portion of the target tweets is retrieved.

Esperanto (eo), Galician (gl) and Azerbaijani (az) all cope with another
type of error. Their closeness to a more prevalent language (Spanish for
Galician, Turkish for Azerbaijani and multiple highly frequent languages
for Esperanto) forces the precision component in the greedy algorithm to
select very rare occurrences. Although these phrases are successful in
distinguishing between the target and their competition, their
infrequency leads to a low recall for the target language in the test
set.

For each of these outlier cases that bring down averaged performance, it
would be interesting to see follow-up research that investigates how
much improvement can be made, or whether the problem is with the data
and possible code switching that occurs. Framing language identification
on Twitter as a single-label problem introduces these inherent pitfalls.

Robustness and reproducibility

Although there are no major performance differences between applying the
key phrase lists to the development and the test split of the data,
there could be additional testing on the temporal nature of the lists.
Training, development and tests were all performed on data yielded from
the same six month snapshot, and could reflect specific events or topics
of that period.

For example, the optimized key phrase lists contained 9 hashtags on
average. Since hashtags are used mostly as topical and event markers, in
a few years these search terms may have disappeared from Twitter
completely.

Although this should lead to only marginally lower quality of the
supplied phrases, it would be interesting to see an evaluation on data
from another period. For now, the robustness of the method for selecting
optimal key phrases is not under discussion. The code for generating key
phrases on new Twitter snapshots and potentially new target languages is
available at <https://github.com/tjkreutz/twitterphrases>.

Conclusion
==========

We introduced a systemic way of selecting optimal key phrases for the
the 50 most prevalent languages of Twitter. By demonstrating which
tweets can be retrieved using the key phrases in an experimental setting
that closely mirrors the setup with the real-time Twitter data stream,
we provide the statistics that can be cited as limitations for Twitter
collections built this way.

The best performing greedy algorithm for selecting key phrases, scores
each phrase by precision weighted by recall. For the 25 most prevalent
languages, exponentiating the precision with a $\beta$ of 2 helps to
increase the weight of high-precision phrases which limits the number of
false positives in the resulting Twitter collection.

Alongside this paper and the code to generate new phrase lists, we
provide all the lists as resources. Tracking Norwegian (no) tweets can
be as simple as authenticating with your an API key and running curl:

        curl -d `@no.txt'
    https://stream.twitter.com/1.1/statuses/filter.json

The resulting stream should consist of mostly Norwegian ($\pm$96%)
language and make up more than half ($\pm$52%) of all available
Norwegian tweets.