import ai21
import os

ai21.api_key = os.getenv("HF_KEY")


def text_completion(model, prompt, numResults, maxTokens, temperature, topKReturn, topP):
  response = ai21.Completion.execute(
    model=model,
    prompt=prompt,
    numResults=numResults,
    maxTokens=maxTokens,
    temperature=temperature,
    topKReturn=topKReturn,
    topP=topP,
    presencePenalty={
      "scale": 1,
      "applyToNumbers": True,
      "applyToPunctuations": True,
      "applyToStopwords": True,
      "applyToWhitespaces": True,
      "applyToEmojis": True
    },
    countPenalty={
      "scale": 1,
      "applyToNumbers": True,
      "applyToPunctuations": True,
      "applyToStopwords": True,
      "applyToWhitespaces": True,
      "applyToEmojis": True
    },
    frequencyPenalty={
      "scale": 1,
      "applyToNumbers": True,
      "applyToPunctuations": True,
      "applyToStopwords": True,
      "applyToWhitespaces": True,
      "applyToEmojis": True
    },
    stopSequences=[]
  )
  return response.suggestions[0].text

def chat(model, messages, numResults, maxTokens, temperature, topKReturn, topP):
  response = ai21.Chat.execute(
    model=model,
    messages=messages,
    numResults=numResults,
    maxTokens=maxTokens,
    temperature=temperature,
    topKReturn=topKReturn,
    topP=topP,
    presencePenalty={
      "scale": 1,
      "applyToNumbers": True,
      "applyToPunctuations": True,
      "applyToStopwords": True,
      "applyToWhitespaces": True,
      "applyToEmojis": True
    },
    countPenalty={
      "scale": 1,
      "applyToNumbers": True,
      "applyToPunctuations": True,
      "applyToStopwords": True,
      "applyToWhitespaces": True,
      "applyToEmojis": True
    },
    frequencyPenalty={
      "scale": 1,
      "applyToNumbers": True,
      "applyToPunctuations": True,
      "applyToStopwords": True,
      "applyToWhitespaces": True,
      "applyToEmojis": True
    },
    stopSequences=[]
  )
  return response.suggestions[0].text

def GEC(text):
  response =  ai21.GEC.execute(text=text)
  l = len(response.corrections)
  for i in range(l):
    sug = response.corrections[i].suggestion
    start = response.corrections[i].startIndex
    end = response.corrections[i].endIndex
    text = text.replace(
      text[start:end],
      sug
    )
  return text

def summarize(text):
  response = ai21.Summarize.execute(source=text, sourceType="TEXT")
  return response.summary

def improvements(text):
  response = ai21.Improvements.execute(
    text=text,
    types=[
      'fluency',
      'vocabulary/specificity',
      'vocabulary/variety',
      'clarity/short-sentences',
      'clarity/conciseness'
    ]
  )
  l = len(response.improvements)
  for i in range(l):
    sug = response.improvements[i].suggestions[0]
    start = response.improvements[i].startIndex
    end = response.improvements[i].endIndex
    text = text.replace(
      text[start:end],
      sug
    )

  return text

def paraphrase(text):
  response = ai21.Paraphrase.execute(text=text, style="general")
  return response.suggestions[0].text

def contextual_answer(context, question):
  response = ai21.Answer.execute(context=context, question=question)
  return response.suggestions[0].text