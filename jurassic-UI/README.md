# AI21 Models

1. Jurassic is AI21 Labs' production-ready family of large language models (LLMs), powering natural language AI in thousands of live applications.
2. Jurassic-2 (J2) is our top-notch series of state-of-the-art Large Language Models. As the new generation following Jurassic-1, J2 not only improves upon the previous series in every aspect, but it also offers new features and capabilities that put it in a league of its own.
3. It offers 6 models such as `j2-large-instruct`, `j2-grande-chat`, `j2-jumbo-chat`, `j2-light`, `j2-mid`, and `j2-ultra`.
4. It offers various types of tasks such as `Paraphrase`, `Summarize`, `Summarize By Segment`, `Text Segmentation`, `Grammatical Error Corrections`, `Text Improvements`, `Library Answer`, `Library Search`, and `Contextual Answers`.

## Important Links

The AI21 platform offers 90$ credit as a usage for the user.

- Website: https://studio.ai21.com/
- Docs: https://docs.ai21.com/docs/task-specific
- SDK: https://docs.ai21.com/reference/python-sdk

## Paraphrase

### Features

#### Choose a style that fits your needs

**You have the choice between five different styles:**

- General - there are fresh and creative ways to rephrase sentences. Offer them to your users.
- Casual - convey a friendlier and more accessible tone for the right audience.
- Formal - present your words in a more professional way.
- Short - express your messages clearly and concisely.
- Long - expand your sentences to give more detail, nuance and depth.

#### Adding context to the paraphrase
You can paraphrase only part of the text while keeping the surrounding text unchanged by specifying a range within the text.

## Grammetical Error Correction

### Features

#### Fix every grammar error
Allow your users to write with flawless grammar, including tenses, verb additions, changing the order, and everything else you forgot since English high school lessons. No more wondering if it's who or whom.


| Before | After |
| ---- | ----- |
|I'm is going | I'm going |
|I'm going go | I'm going to go |
|I was in the there |	I was there |

#### Find all the missing words

It difficult read a sentence like this, isn't it? The GEC API will make it easier for you to do this.

| Before | After |
| ---- | ----- |
| This soup very tasty |	This soup is very tasty |

#### Punctuation: Punctuation, Punctuation!

Give your users peace of mind without having to worry about double whitespaces, incorrect punctuation, and answering the most annoying question - do I need a hyphen here?

| Before | After |
| ---- | ----- |
| Are you going to be there! |	Are you going to be there? |
| Hi you |	Hi, |

#### Take the spelling bee by storm

A spell check, but so much more: Capitalizing, changing words that sound the same but spelled differently, and fixing errors caused by typos.

| Before | After |
| ---- | ----- |
| I'm not aloud to go | I'm not allowed to go |
| i think i tough i saw you tryt | i think i thought i saw you try |
| Let it god | Let it go |

#### Avoid repetition of repetitive word repetitions

Do you know the song "I will will always love you"? How about “I will always love you you”? Doesn’t have the same ring, does it? With GEC API you can make sure you’ll always have a hit.

| Before | After |
| ---- | ----- |
| Gimme Gimme Gimme a man after midnight |	Gimme a man after midnight |

#### Communicate the right message without using any wrong words

Did you ever use words with similar sounds or spellings? GEC API makes sure you want won't!

| Before | After |
| ---- | ----- |
| At times, my job can be quite monogamous |	At times, my job can be quite monotonous |

## Text Improvements

### Features

#### Speak with great fluency

Let your users express themselves more fluently, phrasing the same message in a natural way.

| Before | After |
| ---- | ----- |
|Affiliated with the profession of project management, I have ameliorated myself with a different set of hard skills as well as soft skills. |	Being involved in the profession of project management, I have developed a different set of hard skills as well as soft skills. |

#### Feature description: specificity

Make it easier for users to be more precise by recommending a more specific word to use within the context.

| Before | After |
| ---- | ----- |
| Good sleep |	Full night's sleep |
| I ate a good pizza |	I ate a tasty/delicious/yummy pizza |

#### Enrich the text with variety

Allow your users to avoid multiple repetitions of the same multiple words.

| Before | After |
| ---- | ----- |
| Positive energy balance means that you consume more energy than you burn. With the right types of foods this could mean muscle gain, with the wrong types it could mean fat gain. |	Positive energy balance means that you consume more energy than you burn. With the right types of foods this could mean muscle gain, with the wrong types it could result in fat gain. |

#### Write simple with short sentences

Advise your users how to avoid long and convoluted sentences by splitting them into short sentences.

| Before | After |
| ---- | ----- |
| In addition, it is essential to build trust in their relationships, so they can start having efficient communications, so it will allow them to give feedback and call their peers on their performance without the fear of interpersonal conflicts. | In addition, it is essential to build trust in their relationships, so they can start having efficient communications. This will allow them to give feedback and call their peers on their performance without the fear of interpersonal conflicts. |

#### Conciseness

Make it easier for your users to be concise.

| Before | After |
| ---- | ----- |
| We will arrive home in a period of five days |	We will arrive home in five |days

## Summarize

### Summarization Models

#### Summarize
The /summarize API takes a piece of text or fetches text from a given URL and generates grounded summaries that remain faithful to the original document (i.e. no external information is added during the process). The summaries are formatted as bullet lists, following the original text flow.

#### Summarize by Segment
The /summary-by-segment API takes a piece of text or fetches text from a given URL and breaks it into logical segments, returning summarized content for each segment, rather than one overall summary. This method is particularly useful for enabling users to read the original text faster and more efficiently. They can skim where possible and pay more attention where needed.

## Text Segmentation

### Features

#### Different types
In addition to working with free text, this API can also work directly with your favorite (or least favorite) webpage URLs! No need to spend time and effort scraping text yourself - just input the required URL and let the summarization begin.

Note: if the webpage you are trying to summarize is behind a paywall or restricted access, your call will fail and will result in an error.