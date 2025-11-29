import data_collection
import sentiment_analysis
import model_training
import predict

def start():
    print("1. Download Stock Data")
    print("2. Analyze Sentiment")
    print("3. Train Model")
    print("4. Predict Price")

    choice = int(input("Choose: "))

    if choice == 1:
        data_collection.get_stock_data("AAPL")
    elif choice == 2:
        sentiment_analysis.process_news()
    elif choice == 3:
        model_training.train_model()
    elif choice == 4:
        predict

start()
