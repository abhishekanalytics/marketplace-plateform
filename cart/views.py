
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from Tradecore.models import CustomUser,Product


@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)
    
    try:
        product = Product.objects.get(pk=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user, product_id=product_id)
        cart.quantity = quantity
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Product.DoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def remove_from_cart(request, item_id):
    try:
        cart_item = Cart.objects.get(pk=item_id, user=request.user)
        cart_item.delete()
        return Response({"item successfully deleted"},status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return Response({"error": "Item does not exist in cart"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({"error": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)

