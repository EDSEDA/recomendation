import numpy as np
import pandas as pd


used_products = pd.read_csv('/home/vorkov/Workspace/recommendation/data/instacart-market-basket-analysis/used_products.csv', usecols=['product_id', 'product_name'])
used_products = pd.Series(used_products['product_name'].values, index=used_products['product_id']).to_dict()

def first_five_unique(arr):
    seen = set()
    return [seen.add(x) or x for x in arr if x not in seen][:5]

# Пример использования функции
array = [1, 2, 3, 2, 1, 4, 5, 6, 5, 7, 8, 9]
result = first_five_unique(array)
print(result)

class Model:

    def __init__(self, model, dataset):
        self.model = model
        user_mappings, _, item_mappings, _ = dataset.mapping()
        self.internal_user_ids = list(user_mappings.values())
        self.internal_product_ids = list(item_mappings.values())
        self.inv_item_mappings = {v: k for k, v in item_mappings.items()}

    def get_recommendations(self, user_ids):
        prediction = self.model.predict(
            user_ids=user_ids,
            item_ids=self.internal_product_ids,
        )

        prediction = np.argsort(prediction)
        prediction = [used_products[product_id] for product_id in [self.inv_item_mappings[x] for x in prediction]]
        prediction = first_five_unique(prediction)
        return prediction
