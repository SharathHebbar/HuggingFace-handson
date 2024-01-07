# Convo Bot using GPT2-small

GPT2 small is fine-tuned on vicgalle/alpaca-gpt4 dataset to create ChatGPT2.

## Technical Details

1. The model's repository is in HuggingFace
- Link to the model: https://huggingface.co/Sharathhebbar24/convo_bot_gpt_v1/tree/main
- Model Usage: https://huggingface.co/Sharathhebbar24/convo_bot_gpt_v1
2. The model was trained on the following Specs
- Nvidia RTX 3050 4GB VRAM
- 16GB RAM
- Intel i5 12th gen 12500H
3. It took around 4:25:42 to train the model for 3 epochs with a loss of 1.57.
4. The model achieved Perplexity: 4.744423275536728
5. It was trained on FP16 bit architecture with a batch size of 2.

| license | datasets | language |
| ------- | -------- | -------- |
| apache-2.0 | vicgalle/alpaca-gpt4 | en |

This model is a finetuned version of ```gpt2``` using ```vicgalle/alpaca-gpt4```

## Model description

GPT-2 is a transformers model pre-trained on a very large corpus of English data in a self-supervised fashion. This
means it was pre-trained on the raw texts only, with no humans labeling them in any way (which is why it can use lots
of publicly available data) with an automatic process to generate inputs and labels from those texts. More precisely,
it was trained to guess the next word in sentences.

More precisely, inputs are sequences of continuous text of a certain length and the targets are the same sequence,
shifting one token (word or piece of word) to the right. The model uses a masking mechanism to make sure the
predictions for the token `i` only use the inputs from `1` to `i` but not the future tokens.

This way, the model learns an inner representation of the English language that can then be used to extract features
useful for downstream tasks. The model is best at what it was trained for, however, which is generating texts from a
prompt.

### To use this model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
model_name = "Sharathhebbar24/convo_bot_gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained("gpt2")
def generate_text(prompt):
 inputs = tokenizer.encode(prompt, return_tensors='pt')
 outputs = mod1.generate(inputs, max_length=64, pad_token_id=tokenizer.eos_token_id)
 generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
 return generated
 prompt = """
 Below is an instruction that describes a task. Write a response that appropriately completes the request. 
 ### Instruction: Who is the world's most famous painter? 
 ###
 """
res = generate_text(prompt)
res
```