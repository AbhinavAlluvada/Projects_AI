from transformers import pipeline

mood_ai = pipeline("sentiment-analysis")

print("Model used:", mood_ai.model.name_or_path)

while True:
    text = input("\nType something (or exit): ")
    if text.lower() == "exit":
        break

    result = mood_ai(text)[0]
    label = result["label"]


    print("Mood:", label)


    if label == "POSITIVE":
        print("😊 You sound happy!")
    elif label == "NEGATIVE":
        print("😞 You sound sad!")
