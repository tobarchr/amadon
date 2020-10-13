from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)
def checkout_success(request):
    product_id = Product.objects.get(id=request.POST['product_id'])
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(product_id.price)
    total_charge = quantity_from_form * price_from_form  
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')
def checkout(request):
    all_orders= Order.objects.all()
    last_order = Order.objects.last()
    total_spent = 0
    total_quantity = 0
    for invoices in all_orders:
        invoices.total_price
        invoices.quantity_ordered
        total_spent+=invoices.total_price
        total_quantity += invoices.quantity_ordered
    context = {
    "total_spent" : total_spent,
    "last_order" : last_order,
    "total_quantity" : total_quantity
    }
    return render(request, "store/checkout.html",context)