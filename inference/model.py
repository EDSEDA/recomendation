import numpy as np
import pandas as pd


used_products = pd.read_csv('data/used_products.csv', usecols=['product_id', 'product_name'])
used_products = pd.Series(used_products['product_id'].values, index=used_products['product_name']).to_dict()


class Model:

    def __init__(
        self,
        model,
        dataset,
    ):
        self.model = model
        user_mappings, _, item_mappings, _ = dataset.mapping()
        self.internal_user_ids = list(user_mappings.values())
        self.internal_product_ids = list(item_mappings.values())
        self.inv_item_mappings = {v: k for k, v in item_mappings.items()}
        self.rng = np.random.default_rng()

    def get_recommendations(self):
        similar_user_id = int(self.rng.choice(self.internal_user_ids))
        prediction = self.model.predict(
            user_ids=similar_user_id,
            item_ids=self.internal_product_ids,
        )
        prediction = np.argsort(prediction)[-1:-6:-1]
        prediction = [used_products[product_id] for product_id in [self.inv_item_mappings[x] for x in prediction]]
        return prediction
