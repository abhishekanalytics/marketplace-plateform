import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .models import UserActivity, Product,CustomUser

def get_user_item_matrix():
    users = CustomUser.objects.all()
    products = Product.objects.all()

    user_index_mapping = {user.id: index for index, user in enumerate(users)}
    product_index_mapping = {product.id: index for index, product in enumerate(products)}

    user_item_matrix = np.zeros((len(users), len(products)))

    for user in users:
        user_activities = UserActivity.objects.filter(user=user)
        for activity in user_activities:
            user_index = user_index_mapping[user.id]
            product_index = product_index_mapping[activity.product.id]
            if activity.activity_type == 'purchase':
                user_item_matrix[user_index][product_index] = 1
            elif activity.activity_type == 'browse':
                user_item_matrix[user_index][product_index] = 0.5  # Lower weight for browsing

    return user_item_matrix


def get_similar_users(user_id, user_item_matrix):
    similarities = cosine_similarity([user_item_matrix[user_id]], user_item_matrix)[0]
    similar_users = np.argsort(similarities)[::-1][1:]
    return similar_users

def recommend_products(user_id, user_item_matrix, num_recommendations=5):
    similar_users = get_similar_users(user_id, user_item_matrix)
    recommended_products = []
    user_activities = UserActivity.objects.filter(user_id=user_id)
    user_product_ids = set(activity.product_id for activity in user_activities)

    for user in similar_users:
        similar_user_activities = UserActivity.objects.filter(user_id=user)
        similar_user_product_ids = [activity.product_id for activity in similar_user_activities if activity.activity_type == 'purchase']
        for product_id in similar_user_product_ids:
            if product_id not in user_product_ids:
                recommended_products.append(product_id)
        if len(recommended_products) >= num_recommendations:
            break

    return recommended_products[:num_recommendations]
