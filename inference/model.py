import numpy as np


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
        prediction = [self.inv_item_mappings[x] for x in prediction]
        return prediction
