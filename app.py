import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# language codes
languages = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Bengali": "ben_Beng",
    "Marathi": "mar_Deva",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Urdu": "urd_Arab",
    "Malayalam": "mal_Mlym",
    "Kannada": "kan_Knda",
    "Odia": "ory_Orya",
    "Assamese": "asm_Beng"
}
sentiment_model=pipeline("sentiment-analysis")

def translate(text, src_lang, tgt_lang):
    tokenizer.src_lang = languages[src_lang]

    inputs = tokenizer(text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(languages[tgt_lang]),
        max_length=60
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def format_sentiment(sentiment):
    label = sentiment["label"]
    score = round(sentiment["score"], 2)

    if label == "POSITIVE":
        emoji = "😊"
    elif label == "NEGATIVE":
        emoji = "😡"
    else:
        emoji = "😐"

    return f"{emoji} {label} ({score})"

def analyze(text, src_lng, tgt_lng):

   
    english_text = translate(text, src_lng, "English")

    
    sentiment = sentiment_model(english_text)[0]
    sentiment_result = format_sentiment(sentiment)

   
    translated_output = translate(english_text, "English", tgt_lng)

   
    return english_text, sentiment_result, translated_output


with gr.Blocks() as app:

    gr.Markdown("# 🇮🇳 Multilingual Sentiment Analysis System")
    gr.Markdown("### Analyze sentiment across Indian languages")

    text = gr.Textbox(label="📝 Enter Text")

    src = gr.Dropdown(list(languages.keys()), label="🌐 Source Language", value="Hindi")
    tgt = gr.Dropdown(list(languages.keys()), label="🎯 Target Language", value="English")

    gr.Markdown("## 📊 Results")

    eng_out = gr.Textbox(label="🌍 English Translation")
    sent_out = gr.Textbox(label="😊 Sentiment Analysis")
    trans_out = gr.Textbox(label="🌐 Translated Output")

    btn = gr.Button("🚀 Analyze")

    btn.click(analyze, inputs=[text, src, tgt], outputs=[eng_out, sent_out, trans_out])
    app.launch()