---
place: Proceedings of the 12th Web as Corpus Workshop
redirect: /files/PeetersEtAl.pdf
layout: redirect-internal
date: 2022-02-17
type: publication
authors: ['Jeroen Peeters', 'Michael Opgenhaffen', 'Tim Kreutz', 'Peter van Aelst']
title: "Understanding the Online Relationship Between Politicians and Citizens"
keywords: ['posts', 'politicians', 'engagement', 'facebook', 'periods']
---
Social media have offered politicians a way to reach a broader audience and citizens a dynamic way 
to respond and interact with politicians’ communication. In this study we focus on how two 
important dimensions of the social media messages of politicians impact different types of user 
engagement: the distinction between political and private posts and the degree of emotionality of 
the post. Additionally, we compare the amount and types of interaction between routine periods 
and election periods. Supported by automatic data gathering and coding we analyze all Facebook 
posts of 124 Belgian politicians for a period of more than two years (N = 34,408). Our results indicate 
that different types of Facebook posts lead to different types of user engagement. Private posts 
generate more reactions, while political posts are more often shared and commented on. 
Additionally, Facebook posts with positive, and, negative emotional language garner more interaction than those with less emotionality. Finally, during election campaigns both politicians and 
citizens are more active. There is a proliferation of the amount of Facebook messages that 
politicians post, and these messages also score higher on engagement.
KEYWORDS 
Social media; Facebook 
metrics; user engagement; 
political communication; 
automatic coding; emotions; 
election campaign; machine 
learning
Introduction
Politicians are known as strategic actors who use 
the media to promote their views and improve their 
reputation among the electorate (Strömbäck & 
Kiousis, 2014). Since the rise of the internet and 
the growing popularity of social media, politicians 
have new channels to connect with the public and 
bypass the traditional media. Social media have 
offered politicians a fast and unfiltered way to 
reach their (potential) supporters without journalistic interference (Chadwick, 2017; Larsson & 
Kalsnes, 2014). At the same time, these platforms 
have given citizens a way to respond and interact 
with politicians’ communication. By engaging with 
specific messages followers can indicate what kind 
of messages they like or want to share with their 
own network. This has created a more dynamic way 
of understanding the relationship between politicians and citizens (Xenos, Macafee, & Pole, 2017).
The rise of social media as political tools has 
provided researchers with a new way to study and 
understand politicians’ online performance and 
popularity. Social media metrics can give us insight 
into the amount of audience engagement 
a politician is able to attract. For instance, some 
studies focused on the overall popularity of politicians on social media and identified factors that 
explain why some have more followers than others 
(O’Connell, 2020; Vaccari & Nielsen, 2013). Social 
media metrics also allow us to study the popularity 
of politicians’ online communication strategies at 
an even more fine-grained level (Bene, 2017a; 
Heiss, Schmuck, & Matthes, 2019). In general, we 
can argue that more engagement by the public on 
social media means that politicians are performing 
better in terms of audience response and have an 
effective online communication strategy. This can 
be consequential, as liking, and certainly sharing 
a politician’s Facebook post, means it will reach 
a much larger audience, often going beyond the 
small network of supporters (Bene, 2017b). 
Furthermore, studies suggest that audience engagement on social media with politicians’ posts is 
a good, but far from perfect, predictor of offline 
voting behavior (e.g., Kristensen et al., 2017; 
Vepsäläinen, Li, & Suomi, 2017). Finally, studying 
user engagement is relevant as research has shown 
that user reactions have implications for how 
CONTACT Peeters Jeroen.peeters4@uantwerpen.be University of Antwerp, Lange Nieuwstraat 55, Antwerp 2000, Belgium
Supplemental data for this article can be accessed on the publisher’s website.
JOURNAL OF INFORMATION TECHNOLOGY & POLITICS 
https://doi.org/10.1080/19331681.2022.2029791
© 2022 Taylor & Francis 
politicians communicate on social media. More 
concretely, politicians adapt their communication 
based on both actual audience reactions and perceived audience expectations (Kelm, 2020; 
Tromble, 2018).
In this study we focus on two important dimensions of the online communication of politicians 
that have been addressed in previous research. 
First, we deal with the distinction between political and private messages. Politicians try to convince voters by expressing their political views or 
promoting their political accomplishments, but at 
the same time want to connect with their followers by showing their ‘private persona’ 
(Colliander et al., 2017; Graham, Jackson, & 
Broersma, 2018). Is it successful to show parts of 
their private life and do these private messages 
lead to a different type of engagement than political messages? Second, we look at the sort of 
language politicians use in addressing their followers. More specifically, we focus on the degree 
of emotionality in the posts. Several studies have 
shown that more emotional posts lead to more 
user engagement (Eberl, Tolochko, Jost, 
Heidenreich, & Boomgaarden, 2020; Heiss et al., 
2019). However, we know less about how that 
degree of emotionality interacts with the type of 
posts (private versus political), and the type of 
engagement (reacting versus sharing and 
commenting).
This study goes beyond the existing literature in 
two important ways. First, by scrutinizing the differences between elections and routine times, 
a distinction that has been neglected in most studies 
so far. Today, more than ever, social media allow 
politicians to ‘campaign’ permanently (Larsson, 
2016), blurring the difference with election campaign periods. However, election campaigns 
remain periods in which politicians and parties 
are extra active, citizens are more interested in 
political messages, and news media are more open 
to publicize political content (Van Aelst & De 
Swert, 2009). It is therefore not surprising that 
during election periods there is a proliferation of 
the amount of social media content that politicians 
share (Ceccobelli, 2018). It is unclear, however, to 
what extent campaign periods change the online 
strategies of politicians and lead to different types 
of user engagement on social media. Do politicians 
adjust the type or style of posts in campaign time? 
Or is it rather the public that reacts differently when 
elections near?
Second, to examine the role of election campaigns we analyze a much longer period of study 
than previous research has done, containing two 
election campaigns. This choice also requires automatic forms of gathering and coding social media 
data. In this sense our study is innovative from 
a methodological perspective by using automatic 
language processing techniques and machine learning to analyze large amounts of Facebook data. We 
analyze the audience metrics of the Facebook posts 
of 124 Belgian politicians for two and a half years, 
collecting over 34,000 Facebook posts. We focus on 
Facebook, which is still the most used platform 
among both politicians and the wider public in 
most Western democracies (Gil-Clavel & Zagheni, 
2019).
User engagement on Facebook and political 
messages
Studying different types of user engagement
Facebook users have a wide range of options to 
engage with messages on the platform; people can 
follow an account, they can click on a post if it 
contains a hyperlink, they can react, comment on 
and/or share a post. The user is no longer a passive 
consumer but actively rates the message or shares it 
with friends and strangers. For the author of the 
posts there is the advantage that the message generates a larger reach through this engagement. The 
authors can also learn from this engagement, since 
this behavior is quantified through the so-called 
engagement metrics that indicate how a particular 
post performs in relation to previous posts.
However, the three forms of Facebook engagement should not be considered equal, as they all 
represent a different aspect of engagement. It is 
assumed that a reaction such as a like is given the 
quickest, since it requires less commitment and less 
involvement compared to a comment or a share 
(e.g. Kim & Yang, 2017). In recent years, Facebook 
also added the option to not only like a post but also 
display other types of reactions, such as ‘haha’ or 
‘love.’ Combined we can call these “reactions.” 
Clicking the reactions button has even become 
2 J. PEETERS ET AL.
a kind of habit or ritual in this way (Alhabash, 
Almutairi, Lou, & Kim, 2019). Also in a political 
context these reactions are the most common type 
of user engagement (Gerodimos & Justinussen, 
2015; Larsson, 2015) and these are – perhaps even 
counterintuitively – often studied as the only 
dependent variable to measure the success of political posts (e.g. Nave, Shifman, & TenenboimWeinblatt, 2018). Posting a comment is a totally 
different type of engagement than giving reactions. 
Burke and Kraut (2016) refer to “one-click communication” when talking about reactions, while 
they see posting a comment as a form of “composed 
communication” that requires more effort, and can 
thus be seen as a more meaningful indicator of 
genuine care and interest than reactions (Zell & 
Moeller, 2017). Sharing a post on Facebook also 
requires a more complex handling and more cognitive effort than these simple reactions. A share 
also creates more visibility for a post than 
a comment, a comment remains limited to the 
feed under a post, while a share ensures that the 
shared post appears on your timeline and therefore 
contributes to your own online profile and identity 
(Kim & Yang, 2017). The fact that the three forms 
of engagement are different is also shown by the 
fact that they are not triggered in the same way by 
the characteristics of the (political) messages. This 
is evident from various research that has studied, 
for example, the impact of post length, facial attractiveness, references to political competitors, emotions, etc. on the behavior of the public, with 
features provoking more reactions than shares 
and/or comments, or vice versa (see e.g. Heiss 
et al., 2019; Markowitz-Elfassi, Yarchi, & SamuelAzran, 2019). With this study, we aim to provide 
further insight into how the content and tone of 
political messages affects the reactions, comments 
and shares of Facebook users, focusing on the differences between political vs. private post, and on 
the influence of emotionality, and this inside and 
outside election periods.
Private versus political posts
The social media posts created by politicians can 
serve different functions. Graham, Broersma, 
Hazelhoff, and van ’T Haar (2013) distinguished 
several functions that can be regrouped into three 
categories: campaign information, privatized messages and political messages of substance. 
Campaign information includes calls to vote, 
updates on the campaign trail, etc. These types 
of messages generally do not contain any substance in terms of policy plans or political opinions. Functions that fall under the category of 
political messages are, for instance, taking positions, critiquing opponents or giving advice. 
These types of posts have more substance in the 
sense that they go into more detail about policy 
and often can be linked to a specific issue topic. 
The third category consists of messages that contain information about, or images of, the politicians’ private life, such as their families and leisure 
time.
This threefold distinction will be used in the 
remainder of this paper to help us understand 
why some Facebook posts of politicians attract 
more engagement than others. Several studies indicated that online content showing the private life of 
politicians has become a significant part of the 
social media strategy of politicians across the 
globe (e.g. Geber & Scherer, 2015; Metz, 
Kruikemeier, & Lecheler, 2020). When politicians 
post about their private life, it deepens the amount 
of empathy voters have toward the politician as 
a regular person, as someone who is like them 
(Graham et al., 2018). It generates a sort of authenticity as opposed to the more formal and impersonal communication parties tend to have. In that 
sense, social media help politicians bridge the gap 
between themselves and the people they represent 
(Coleman, 2011; Graham et al., 2018). Lee and Oh 
(2012) show that personalized messages increase 
the (imagined) intimacy between voters and the 
politician and positively impact the evaluations 
that they make about the politician. This is also 
known as a ‘para-social interaction,’ where 
a person feels they have a friendly relationship 
with a public figure, even though they have never 
met (Derrick, Gabriel, & Tippin, 2008). This process of politicians developing a more intimate relationship with voters, has potentially positive 
outcomes for politicians. For instance, a study 
done by O’Connell (2020) on the Instagram posts 
of US politicians shows that family photos and pets 
posts, among others, receive significantly more 
likes than impersonal content.
JOURNAL OF INFORMATION TECHNOLOGY & POLITICS 3
This positive effect of privatized posts on 
users’ engagement, however, might not be the 
same for each of the three types of engagement. 
In fact, we could expect that privatized posts 
might have a positive effect on the number of 
reactions, while having a negative effect on the 
amount of shares and comments. People enjoy 
encountering privatized social media content 
from politicians and probably want to express 
their para-social appreciation toward the politician through an easily given reaction (see e.g., 
Alhabash et al., 2019). In contrast, people share 
online messages, news stories and such because 
they contain useful information. For example, 
reviews of restaurants or movies might help 
others make better decisions (Berger & 
Milkman, 2012; Wojnicki & Godes, 2008). 
Privatized posts, in essence, do not contain 
such useful information. When people do comment on, or share a post by, a politician, they 
might be more likely to do so when the post 
contains relevant or practical information that 
makes them want to inform other people or 
appear knowledgeable (Berger & Milkman, 
2012; Wojnicki & Godes, 2008), or to share 
their political point of view, known as partisan 
sharing (An et al., 2014). This variation in types 
of user engagement has found some confirmation in a recent study that showed that the 
private posts of German politicians received 
more reactions, but not significant more shares 
or comments (Metz et al., 2020).
Thus, we expect the following: 
H1a: Privatized posts will receive more reactions 
than political posts
H1b: Privatized posts will receive less comments and 
shares than political posts
We did not have clear expectations related to 
campaign posts as they fall somewhat in between. 
They can contain useful information (e.g., place on 
the list), but often only refer to the ‘fun’ aspects of 
being on the campaign trail with supporters. 
Therefore, we limit ourselves to a research 
question. 
RQ1: How much user engagement (reactions, comments, shares) will campaign posts receive compared to political and private posts?
Emotionality of social media posts
Emotions are important in building strong relationships with others. The importance of emotionality becomes clear when we look at which types of 
news people prefer. Audiences are drawn toward 
news that isn’t just a neutral description of events. 
Emotionality, whether positive or negative, draws 
an audience to the story (Berger, 2011). This is also 
reflected in people’s response to political posts on 
social media. Berger and Milkman (2012) showed 
that stories that were better in creating emotionality 
were able to achieve higher viral effects than news 
events that lacked such positive or negative tones. 
Echoing this finding, Kalsnes and Larsson (2018) 
found that the Norwegian newspapers articles that 
were being shared the most on social media were 
those that contained high amounts of emotionality. 
Additionally, multiple studies show that in political 
communication, a more emotional tone results in 
more audience engagement on Facebook posts 
(Heiss et al., 2019; Keller & Kleinen-von 
Königslöw, 2018; Nave et al., 2018).
In general, we can say that when a political post 
on Facebook carries a certain level of emotionality, 
it affects the user and consequentially the corresponding engagement. Less clarity exists about the 
determining influence of positive versus negative 
emotions and the impact on the different types of 
engagement. In line with the success of negative 
campaigning (Lau, Sigelman, & Rovner, 2007), it 
is plausible that negative emotions and tonality in 
the posts would lead to more attention and consequently more engagement, as angry and outraged 
users want to offer their point of view. A study on 
the Facebook pages of Hungarian politicians indeed 
showed that posts with a negative tone or emotion 
provoked more comments and shares than positive 
ones (Bene, 2017a). However, there are also arguments to believe that posts with a positive tone or 
emotion could provoke more engagement as they 
allow people to create a more positive self-image on 
4 J. PEETERS ET AL.
Facebook (Qiu, Lin, & Leung, 2013). For example, 
recent research on Austrian politicians has shown 
that political posts that contain language or pictures 
that refer to positive emotions provoked more likes, 
comments and shares, while posts with negatively 
loaded emotions only had a positive effect on the 
number of likes (Heiss et al., 2019).
Based on these mixed findings, our expectation is 
that when Facebook posts of politicians contain 
more emotionality, both positive or negative, their 
followers will engage more with the content. 
H2a: Posting more positive emotional messages has 
a positive effect on the likes, comments and shares of 
social media messages of politicians
H2b: Posting more negative emotional messages has 
a positive effect on the likes, comments and shares of 
social media messages of politicians
As the research so far is mixed or inconclusive, 
we do not formulate concrete expectations about 
potential different effects for the three types of user 
engagement but formulate a research question.
RQ2: How much will the effect of (positive and 
negative) emotionality differ for the different types 
of user engagement (reactions, comments, shares)?
Election versus routine periods
In election research the notion of a ‘permanent 
campaign’ (Blumenthal, 1982) suggests that the differences between election periods and routine periods are blurring and that it becomes ever more 
difficult to distinguish between the two. Mainly 
because politicians feel a constant need to maintain 
popular support, they constantly (want to) communicate with the public (Heclo, 2000). This would 
imply that it is empirically unnecessary to make 
a distinction between campaign and routine periods. 
However, scholars suggest that both periods are 
structurally different for the main actors involved. 
Most clearly, for politicians there is more at stake, 
and therefore they become more active in developing activities to attract public and media attention. 
Van Aelst and De Swert (2009) claim that election 
periods also change how the media handle political 
news and information. For instance, they show that 
journalists devote more attention to domestic news 
items and more attention is given to political parties 
as central actors in the news. This suggests that the 
amount and nature of the political information citizens encounter during elections is different.
Furthermore, citizens also behave in a different 
way. Elections are periods when attention for politics is at an all-time high. People become more 
interested in politics and information about politics 
becomes more relevant to citizens because people 
need to make an informed decision at the ballot box 
(Neudert, Howard, & Kollanyi, 2019). There is 
a heightened attention for politics and consequently politicians operate under stricter observation by both the public and the media. Thus, there 
are several reasons to assume the short period 
before an election day is different from routine 
periods (Walgrave & Van Aelst, 2006).
However, one can argue that nowadays social 
media allow or even force politicians to remain in 
a permanent campaign mode. Nevertheless, studies 
that focus on the social media behavior of politicians find differences over time. Larsson (2016) 
showed that Norwegian politicians and parties 
became much more active on Facebook in the run 
up to election day. Stier, Bleier, Lietz, and 
Strohmaier (2018) found a similar effect for 
German politicians on Twitter. Ceccobelli (2018) 
assessed the permanent campaign theory on the 
Facebook communication of party leaders in different countries and found that the amount of 
Facebook posts politicians put on their page is significantly higher during election times than during 
routine periods.
Thus, we can expect that politicians become 
more active on Facebook during election time, 
but less is known about whether this also 
changes what politicians post about and how. 
Only a few studies explicitly distinguish between 
campaign and routine periods in studying the 
social media activities of political actors. The 
study of Ceccobelli (2018) showed that election 
campaigns increase the personalization of party 
leaders’ Facebook posts, but not the degree of 
privatization of posts. The leaders become more 
central, but not their personal life. Additionally, 
the number of posts about policy issues 
decreased. He concludes by saying that “on 
Facebook, not every day is Election Day” 
(p. 137), meaning that the behavior of political 
JOURNAL OF INFORMATION TECHNOLOGY & POLITICS 5
leaders on social media is fundamentally different during campaigns. In a similar study of US 
parliamentarians on Twitter, Vasko and Trilling 
(2019) confirm that election campaigns change 
the behavior of politicians. For instance, the 
level of hard news went down during campaigns, 
and the level of negativity was lower than in 
routine periods. The authors conclude that “the 
notion of a permanent campaign does not 
appropriately describe political campaigning on 
Twitter, but that the exact differences are still 
poorly understood” (p. 342).
Although the research on the role of different 
time periods on how politicians use social media is 
gradually increasing, the empirical knowledge on 
how this impacts online user engagement is still 
absent. We can expect citizens to be more attentive 
and active online (e.g., Gerbaudo, Marogna, & 
Alzetta, 2019) but we do not know whether and 
how this impacts their preference for certain types 
of messages or the emotional learning of the communication. For instance, campaign periods might 
stimulate citizens to be more eager to interact with 
political content, but the higher supply of political 
messages might also have the opposite effect. 
Similarly, campaign periods are ‘heated’ periods 
that might increase the emotionality of the communication, but that does not mean that these posts 
have the same effect on user engagement as people 
might be more reluctant to comment or share 
emotionally charged posts (Liu et al., 2017). 
Because of these mixed expectations and our limited knowledge on how campaign periods influence 
the precise online interaction between politicians 
and citizens we formulate the following research 
questions: 
RQ3: How do election periods impact the type (private-political-campaign) of politicians’ Facebook 
posts?
RQ4: How do election periods impact the (negativepositive) emotionality of politicians’ Facebook posts?
RQ5: How do election periods impact the interaction 
of different types of user engagement (reaction-share 
-comment) with the type and emotionality of politicians’ Facebook posts?
Data & methodology
We gathered Facebook posts of 124 Dutch-speaking 
Belgian politicians from five political parties represented in parliament between the first of 
January 2017 and the first of July 2019. Originally, 
we considered 237 politicians for the study, this 
included all Flemish regional and federal 
parliamentarians,1 all ministers and party presidents. 
We used CrowdTangle to collect Facebook posts 
from publicly available pages.2 This meant that not 
all Dutch-speaking Belgian politicians could be 
included as some politicians only had a personal 
profile or did not have Facebook altogether. 
Considering this, we opted to leave out the few 
remaining members of the Green party and independent parliamentarians as their number was too 
low for the statistical analyses. This resulted in 124 
Facebook pages of politicians that were included in 
our study. Most politicians that were omitted were 
backbenchers or politicians that were inactive on 
social media (see Table S4 in the Appendix for an 
overview of the distribution across parties).
We classified our Facebook posts into three 
groups: political posts, private posts and campaign posts. As described earlier, political posts 
are those that contain a political issue, private 
posts are about the personal life and leisure time 
of politicians, and campaign posts do not contain any political substance or opinion, but cover 
calls to vote, etc. Although some of the indicators for a certain type of post may be contained 
in the attached image or video, we only based 
our codes on the textual information contained 
in a post. Training a multimodal machine classifier was beyond the scope of this paper. The 
codes were first manually assigned to the posts 
by four annotators. A machine learning model, 
specifically a support vector machine, was simultaneously trained using the coded posts to suggest a label to the human coders to streamline 
the process. After manually coding 15,000 
Facebook posts with substantial agreement 
(0.81 Krippendorff’s alpha) a pretrained BERT 
language model3 was trained for the task of 
recognizing the post types. This model assigned 
labels autonomically (without correction by 
human annotators) correctly in 86% of the test 
cases.
6 J. PEETERS ET AL.
The automatic coding process then involved 
assigning a score from 0 to 100 of how confident 
the trained model was about each of the labels 
(political, private and campaign). Each post was 
labeled as the classification that scored the highest 
confidence of the three. However, if a post did not 
score at least 70 on any of the three classifications, it 
was removed from the dataset because it could not 
confidently be classified. In order to test the effectiveness of this operationalization, we compared 
a random subset (N = 311) of posts that were 
manually coded with the label that was automatically assigned to it using the aforementioned 
method. We ran correlations for each of the three 
categories. This resulted in a correlation of 0.96 for 
campaign posts, 0.97 for political posts and 0.93 for 
private posts. This shows the robustness of our 
operationalization.
This automatic encoding process reduced our 
total amount of Facebook posts from over 50,000 
to 34,408 Facebook posts that were labeled, with 
19,690 political posts (57%), 8,362 campaign posts 
(24%) and 6,356 private posts (19%).
To look at the engagement scores of political 
messages, we distinguish between three separate 
measures: reactions, shares and comments that 
a Facebook post got.4 Table 1 shows the average 
numbers of reactions, shares and comments that 
Facebook posts of politicians got, as well as the 
standard deviation, median and maximum. In validation of previous work, reactions are more freely 
given than shares or comments. A Facebook post 
by a Belgian politician averaged 375 likes, 47 comments and 56 shares in our dataset. The high standard deviation and low median indicate the large 
variation in user engagement that political 
posts get.
In order to test our hypotheses we included several 
additional predictors in our study. First, to measure 
emotionality we used the LiLaH emotion lexicon for 
Dutch created by Daelemans et al. (2020). The LiLaH 
lexicon is translated from the NRC emotion lexicon 
(Mohammad & Turney, 2013) which has been used 
to extract emotion scores for social media texts for 
the purpose of sentiment mining (Rouvier & Favre, 
2016) and online hate speech detection (Gao & 
Huang, 2017, Markov et al., 2021). LiLaH associates 
words with a polarity (positive or negative sentiment) 
and eight emotion categories. We processed the 
Facebook posts by taking each word and looking 
up its base form (lemma) in the lexicon. If a lemma 
was associated with a polarity or emotion, it contributed to an overall emotion score of a Facebook post. 
Posts that did not contain any word present in the 
LiLaH lexicon thus received a score of 0 and were 
considered completely neutral. Posts got both 
a positive and a negative score, which corresponds 
to the amount of positive and negative words that 
were present in the Facebook post. On average 
a Facebook post made by a politician contains 2.6 
positive words and 1.25 negative words. Both variables were logarithmically transformed to account for 
the very skewed distribution.5
Next, we annotated whether the post was made 
during a campaign. Our dataset comprises two election periods, namely the local elections of 
October 2018 and the regional, federal and 
European elections of May 2019 (all three elections 
were on the same day). To investigate if Facebook 
posts score better during these periods, we added 
a variable that indicated if a post was created in the 
four weeks leading up to one of the two elections 
periods.
Multiple control variables were added. First, we 
included the function of the politician; our dataset 
is comprised of parliamentarians, party leaders and 
ministers. These were recoded into a variable that 
indicates if a politician is a high profile (minister or 
party leader) or not. Second, we control for the 
number of likes a page had when the post was 
created and divided this by 10,000, which means 
that an increase of 1 means an actual increase of 
10,000 page likes. This was included to account for 
the overall popularity of politicians on Facebook. 
Thirdly, we checked the level activity by adding the 
number of posts a politician made during our 
2.5 year time period (and divided this by a 1,000). 
Fourth, we included the party of the politician to 
account for the overall popularity of some parties. 
And lastly, we included the type of post. Previous 
studies have shown that adding visuals or video can 
Table 1. Different types of engagement on political Facebook 
posts (N = 34.408).
Mean Std. Dev. Median Max
Reactions 375.0 1133.3 56 33036
Shares 53.2 439.7 3 41283
Comments 47.1 167.9 3 7599
JOURNAL OF INFORMATION TECHNOLOGY & POLITICS 7
lead to more user engagement (Yuki, 2015). 
CrowdTangle records this variable and distinguishes eight distinct types: status, photo, link, 
video, live video, live video complete, native video 
and YouTube. We recoded all types of video and 
YouTube into one category, resulting in 4 types. 
For a descriptive overview of all dependent and 
independent variables see Table S5 and Table S6 
in the appendix.
Results
Our first hypothesis revolves around the distinction 
between private posts and political posts. As a first 
indication Table 2 shows the average number of 
reactions, shares and comments for each of the 
three types. In line with our expectations, private 
posts seem to garner the most reactions. 
Apparently, when people encounter messages or 
photos of politicians as ‘private persons,’ they are 
more inclined to give that post a reaction. In contrast, private posts appear to be less shareworthy. 
Here we can see that political posts are the most 
popular. As expected, it appears that people prefer 
to share posts that contain substance and/or political 
views. Finally, the difference in the average number 
of comments shows us that political posts receive 
more comments than both campaign posts and private posts. It seems that posts with political substance incite more discussions among the followers 
of politicians’ Facebook pages. For a standardized 
version of the table, see the appendix.
Next, for a more formal test of our hypotheses we conducted fixed effects negative binomial regressions (Table 3). This type of analysis 
is warranted because our Facebook posts are 
nested in politicians and because our engagement scores are in essence count variables. All 
the results in the table are incidence rate ratios. 
We expected that private posts would score 
more reactions than political posts (H1a) but 
score less on comments and shares (H1b). It 
appears that both assumption are confirmed. 
There are significant differences between private posts and political posts. Political posts 
receive on average 16% less reactions than private posts. Also campaign posts receive less 
reactions than private posts (about 10%). In 
other words, private posts are more ‘likeable’ 
than political posts. Our analysis shows that the 
opposite is true for shares and comments. 
Percentage-wise our results show that private 
posts get 42% less shares than political posts. 
Political posts score also higher on comments 
(around 6%) than private posts. All in all, our 
hypotheses confirm that political and private 
posts attract different types of behavior from 
citizens following the pages of politicians. The 
conclusion for campaign posts is less clear-cut. 
Just as political posts they receive less reactions 
(about 10%), but more shares than private 
posts. However, in terms of comments they 
score even lower than private posts (almost 
9%) suggesting that campaign posts provoke 
the least discussion on the platform. Which 
answers our first research question: campaign 
posts attract the least amounts of reactions and 
comments, but seem to score better on shares 
than private posts.
Table 2. Average engagement per classification of post 
(N = 34,408).
Reactions Shares Comments
Mean SD Mean SD Mean SD
Campaign 275.6 1108.8 19.2 555,5 27.2 175.7
Private 462.8 1408.1 27.1 257,0 40.6 195.2
Political 389.9 931.1 81.4 126,0 57.7 116.6
Table 3. Fixed effects negative binomial regressions on number 
of reactions, shares and comments.
Reactions Shares Comments
Classification of post (ref = Private)
Political 0.84*** 1.42*** 1.06**
Campaign 0.90*** 1.02 0.91***
Negative emotions 1.03*** 1.07*** 1.08***
Positive emotions 1.01*** 1.01* 1.00
Election period 1.27*** 1.35*** 1.17***
Political status (High profile) 0.93*** 1.15*** 1.51***
Page likes 1.02*** 1.02*** 1.02***
Number of posts 1.05** 0.98 1.08***
Type of post (ref = Photo)
Status 0.85*** 0.88** 1.20***
Link 0.81*** 0.94*** 0.99
Video 0.90*** 1.26*** 1.06**
Party (Ref = N-VA)
Open VLD 0.98 0.99 0.71***
CD&V 1.03 1.17*** 0.78***
sp.a 1.15*** 1.23*** 0.98
Vlaams Belang 1.03 1.20*** 1.04
Intercept 1.22*** 0.28*** 0.41***
N (total) 34,408 34,408 34,408
N (Politicians) 124 124 124
AIC 389,204.1 219,983.9 231,517.7
*p < .05; **p < .01;***p < .001
8 J. PEETERS ET AL.
Hypothesis 2a and 2b state that using more emotional language (both positive and negative) will 
have a positive effect on the reactions, shares and 
comments of a Facebook post made by politicians. 
Our analysis shows a clear effect of both negative 
emotions and positive emotions on the amount of 
interaction a post gets. This means that emotionally 
charged language makes users engage more with 
posts. Citizens seem to be more drawn toward 
emotionality then to neutral posts. However, the 
effects of negative language are more outspoken 
and have a significant effect on all types of engagement. Positive language helps to get more reactions, 
but the effect on shares is modest, and there does 
not seem to be a significant effect of positively 
charged language on the amount of comments. 
Negativity seems to lead more often to a written 
reaction in which the user can express his shared 
anger or frustration with the message. Therefore, 
we find evidence for both hypothesis 2a and 2b.
A part of the explanation of the different 
effects of emotionality are related to the types 
of posts. Negative emotions mainly strengthen 
the engagement of political posts, while positive 
emotions seem to boost engagement with private posts. This becomes clear when we perform interaction effects between emotionality 
and type of post (see Table S9; and Figure S6 
appendix). Mainly, the effects of negative emotionality appear to vary for different types of 
posts. Negative emotional language has a slight 
negative effect for the number of reactions of 
private posts, while it has a modest positive 
effect on campaign posts and a strong positive 
effect on liking political posts. When it comes 
to the number of comments, negative emotionally charged language has no effect on private 
posts, while it does have a positive effect on the 
amount of comments for both campaign and 
political posts – which answers our second 
research question.
Some of our control variables also yielded 
significant results. As expected, the overall 
online popularity of a politician matters. The 
more likes a page has, the higher the amount 
of reactions, shares and comments the posts of 
that politician will get. A similar effect is at play 
for the number of posts a politician has made. 
More active politicians get more reactions and 
comments, but not necessarily more shares. 
Next, we see that the status of politicians has 
an impact, in particular with the more demanding forms of user engagement. High-profile politicians such as party leaders and ministers can 
attract more shares and especially more comments than regular parliamentarians. 
Nonetheless they tend to do worse in terms of 
reactions. This might be partly explained by the 
fact that high profile politicians are not only 
followed by people who ‘like’ them, but also by 
people who oppose them and use social media to 
vocally protest them. We can also report some 
modest party differences. Interestingly, again, the 
variation between parties is not consistent over 
the three measures of user engagement. For 
instance, the posts of politicians from the 
Christian Democratic party (CD&V), controlling 
for other factors, get more shares, but less comments than the Flemish nationalists (N-VA). 
Finally, regarding the type of post, it seems 
0.00 50.00 100.00 150.00
Total number of posts Jan 1, 2017
Jul 1, 2017
Jan 1, 2018
Jul 1, 2018
Jan 1, 2019
Jul 1, 2019
Day post was made
Local elections 14 Oct 2018 National elections 26 May 2019
Figure 1. Total posts per day.
JOURNAL OF INFORMATION TECHNOLOGY & POLITICS 9
that photos are the best at garnering the most 
reactions, but videos do best in terms of shares 
and comments.
Campaign versus routine periods
Next, we explore the differences in the amount 
of interaction the Facebook posts of politicians 
get between routine periods and election 
campaign periods. Figure 1 shows that the 
amount of Facebook posts increases during 
election times. One smaller spike during the 
2018 local elections in the beginning of 
October 2018, and a second bigger one, during 
the national elections at the end of May 2019. 
Overall, the number of posts in an average 
routine month (about 1,000) almost doubles in 
the four weeks before election day. Remarkably 
0 .1 .2 .3 .4 .5
Linear Prediction
Figure 2. Reactions in election and routine periods between types of post.
-1.2 -1 -.8 -.6 -.4
Linear Prediction Campaign Private Political
Routine Elections
Shares
Figure 3. Shares in election and routine periods between types of post.
10 J. PEETERS ET AL.
both elections are followed by a significant drop 
in the amount of Facebook posts. It is as if 
politicians have been working tremendously 
hard during a campaign and therefore need 
a break after the election day itself.
When we zoom in to the types of posts, we 
can state that during elections all types of posts 
appear more often. However, to answer RQ3, we 
look more in detail at the composition of posts. 
In routine times around 22% of posts are campaign posts, 19% private posts and 60% political 
posts. In the weeks leading up to an election 
around 45% of posts are campaign posts, 15% 
private posts and 40% political posts. This indicates that mainly political posts, focusing on 
substantial issues or political opinions, lose in 
relative importance. However, it is important to 
note that in absolute numbers both political and 
private posts increase significantly, but their 
share decreases because of the exponential 
growth of campaign posts.
Next, to explore if the amount of emotionality 
differs between election and routine periods 
(RQ4), evidence shows that the average for 
both positive and negative emotionality is significantly lower during election periods. The positive emotionality score is on average 0.12 lower 
in election periods (p < .05) and the negative 
emotionality score is on average 0.22 lower in 
election periods (p < .001). Our results thus 
show that during election campaigns, politicians 
are more neutral in terms of the language that 
they use.
Table 3 shows that there is a general positive 
effect of campaigns on the user engagement of 
politicians’ Facebook posts. Users produce more 
reactions (27%), more shares (35%) and more comments (17%). However, we were interested to see if 
different types of posts get different types of user 
engagement in elections times compared to routine 
times. Thus, to answer RQ5 regarding the effects of 
elections on user engagement, we interacted the 
campaign period with our threefold typology (private, campaign and political), as well as with emotionality (for the full regression see Table S6 in 
appendix). Figures 2, 3 and 4 show us the difference 
in engagement between the three main types of 
posts both in election times (red triangle) and routine times (blue circle). At first sight, it becomes 
clear that all three types receive more reactions, 
shares and comments during election periods. 
Figure 4 indicates that the amount of comments 
posts received in election times is slightly higher for 
some types of posts. In the run-up to an election, 
campaign posts score clearly better in terms of 
comments, while private posts seem to benefit less 
in this regard. However, all in all, we conclude that 
for the most part citizens do not show a different 
engagement behavior with Facebook posts of politicians between routine and elections periods.
-.9 -.8 -.7 -.6 -.5
Linear Prediction Campaign Private Political
Routine Elections
Comments
Figure 4. Comments in election and routine periods between types of post.
JOURNAL OF INFORMATION TECHNOLOGY & POLITICS 11
Figure 5 shows the difference in the interaction rate of both positive and negative emotionality between routine periods (blue) and election 
periods (red). We do find significant differences 
between the two periods. It appears that emotional language, both positive and negative, does 
not have an impact during a campaign period. 
In contrast to routine periods, higher levels of 
emotionality do not lead to more engagement. 
An exception to this trend is negative emotionality as affects the amount of comments. Also 
during election periods, negative emotionality 
has a positive effect on this specific type of 
engagement. Overall, these results indicate that 
emotional language has a smaller influence on 
Facebook engagement during election 
campaigns.
Conclusion
The social media revolution has not only changed 
the opportunities for politicians to spread their 
message, but also for citizens to interact with 
them. A recent but growing number of studies try 
to explain which messages from politicians will lead 
to more interaction than others. Our study adds to 
this literature in several ways. First, we have shown 
that the type of social media post co-determines 
how the online public engages with it. For instance, 
when politicians share private matters, which happens in one out of five Facebook posts, these posts 
lead to more reactions than political posts, while 
simultaneously they are less likely to be shared or 
commented on. This means that the so-called parasocial interaction between politician and citizen 
remains rather superficial. The politician gives 
a quick insight into an aspect of his/her personal 
life, and the follower shows a form of appreciation 
with an even more hasty response. For political 
posts another dynamic is at play. When politicians 
share their political ideas, opinions or accomplishments, people more often react to them in a more 
meaningful way by commenting on them and sharing the message with others. As these types of 
interaction require a bit more effort from the user, 
they also show more involvement and commitment 
to the user’s community.
Second, if politicians want to get more interaction on their Facebook page, the use of emotional 
language is key. Overall, and in line with previous 
studies, we find that messages containing more 
positive or negative emotional words lead to more 
user engagement. The effect of negativity is clearly 
more outspoken, and much stronger on the higher 
levels of interaction such as comments and shares, 
where the effect of positivity becomes small or nonexistent. Our data suggest that this difference is also 
related to the type of message. Where positive language works well to improve the number of reactions on private messages, negative language has 
a stronger effect on the shares and comments for 
political posts.
Third, and most innovatively, we focused on the 
role of the political context, by distinguishing by 
routine and election periods. Our findings are in 
line with previous studies that state that the idea of 
a permanent campaign does not imply that 
“every day is election day” (Ceccobeli, 2018). Both 
0 .1 .2 .3 .4
Linear Prediction
0 .1 .2 .3 .4
Linear Prediction
-1 -.8 -.6 -.4
Linear Prediction
-1 -.8 -.6 -.4
Linear Prediction
-1 -.8 -.6 -.4 -.2
Linear Prediction
-.8 -.7 -.6 -.5 -.4
Linear Prediction
Figure 5. Reactions, shares and comments in election and routine periods for negative and positive emotionality.
12 J. PEETERS ET AL.
politicians and citizens are more active on social 
media during this ‘exceptional period,’ but the 
dynamic of the interaction between political actors 
and the public remains largely the same. All types of 
posts get almost to the same extent substantially 
more reactions, shares and comments. Therefore, 
we can conclude that election campaigns intensify 
the interactions between politicians and citizens but 
do not change the dynamic. Campaign periods also 
do not mean that politicians start using more emotional language, on the contrary, campaigns lead to 
less emotional messages and emotionality has less 
effect on user engagement. Only for the most active 
people who make the effort to comment on a post 
does negative language work better during campaigns. This seems to suggest that during campaign 
periods, when stakes are higher, politicians do not 
need to use strong language to provoke public 
interaction on social media.
More broadly, our study can weigh in on the 
ongoing debate on the effectiveness of negative 
campaigning (Lau et al., 2007), as our results 
suggest that ‘going negative’ is a fruitful political 
strategy to increase one’s online popularity. 
However, there are a few important nuances. 
First, it is unclear whether more interaction is 
always positive for the politician. In particular 
posts of leading politicians seem to generate 
a large number of comments that critique the 
message or its sender. We should thus be careful 
when interpreting these numbers purely in terms 
of success and popularity. Second, negative emotional language is less used and less effective in 
the important period preceding an election. In 
that sense the notion of ‘negative campaigning’ 
is somewhat misleading, as negative language is 
more present and more successful in routine 
times than in election time. This could be due 
to the fact that in election times Facebook posts 
containing negative emotional language are seen 
as less sincere, or more strategic, by the public, 
which causes it to have less of an impact. Outside 
election time, negative emotionality might be perceived as more related to actual policy and less as 
a form of negative campaigning to damage an 
opponent and gain votes. This finding echoes 
what Aaldering, van der Meer, and Van der 
Brug (2018) found in their study on the lower 
effect of negative news coverage of political 
leaders during campaign times compared to routine times. Third, our study tells us little about 
the right ‘doses’ of negative language. It is possible that negative messages mainly attract attention if they are not the norm and are mixed with 
more positive communication. In a similar way, it 
is possible that private messages only get more 
likes if they are not the dominant form of communication. Put differently, further research is 
needed to determine what a successful combination is of both emotionality and types of 
messages.
However, the present study has other limitations that could be addressed in future work. Our 
findings are based on a large N dataset, which 
means that there was less room for personal differences. For instance, we did not include a lot of 
variables on the post level, such as pictures, 
videos or the timing. Thus, big data research 
such as this, is best used in combination with 
qualitative analyses to further deepen our understanding of which factors of the Facebook posts 
of politicians result in a more audience engagement. Although, we devoted ample attention to 
the different types of user engagement when 
studying how people interact with Facebook 
posts of politicians, we combined the seven different types of reactions. We are, however, aware 
that a more fine-grained analysis could provide 
more accurate insights on what types of posts 
lead to ‘positive’ (like, love, care) or more ‘negative’ (angry, sad) reactions. Finally, the present 
study only took the textual content of the 
Facebook posts into account when labeling each 
post. After all, there might be a difference in 
terms of meaning and content between the textual and visual messages of a Facebook post. 
Whereas a politician might post a private message in the form of a status update, the accompanying photo or video might well have 
a political focus, or vice versa. This (non-)congruence between textual and visual elements and 
associated meanings is therefore valuable to 
study in the future. Despite these limitations, we 
hope that our large-N study and partly automatic 
analyses of social media posts of political actors 
will inspire others to further develop our understandings on when, how and why politicians and 
citizens interact on social media.
JOURNAL OF INFORMATION TECHNOLOGY & POLITICS 13
Notes
1. Substitutes who (temporarily) filled in the parliamentary seat of a ministers were also included.
2. For more info see https://www.crowdtangle.com
3. A BERT-transformer using the GroNLP/bert-basedutch-cased pretrained model (12-layers, GELU 
activation).
4. For Reactions, all sub types of reactions were aggregated 
(likes, wow, haha, sad, angry and love).
5. Skewness for Positive words = 3.47 and skewness for 
negative words is 3.12.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
This work was supported by the BOF GOA
Notes on contributors
Jeroen Peeters is a PhD candidate at the University of Antwerp 
(Belgium) and a member of research group Media, 