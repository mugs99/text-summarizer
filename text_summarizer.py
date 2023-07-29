from transformers import pipeline

def summarize_text(input_text, max_length=500, min_length=30):
    summarizer = pipeline("summarization")
    summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=True)
    return summary[0]['summary_text']

if __name__ == "__main__":
    input_text = input("Enter the text you want to summarize: ")
    summary = summarize_text(input_text)
    print("\nSummary:")
    print(summary)