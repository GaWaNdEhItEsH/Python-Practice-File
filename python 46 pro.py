# if__name__=="__main__":


import data_processor
# They can still use the function

df = data_processor.load_data("TATAMOTOREQ.csv")
data_processor.process_data(df)

print(data_processor.add(10,50))
