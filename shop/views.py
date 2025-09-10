# views.py - Updated with cart functionality

from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Order, Cart
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

def index(request):
    products_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        products_objects = products_objects.filter(title__icontains = item_name)
    
    # Get user's cart count if logged in
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    
    #paginator code
    paginator = Paginator(products_objects, 2)
    page = request.GET.get('page')
    products_objects = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {
        'product_objects': products_objects,
        'cart_count': cart_count
    })

def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Products, id=product_id)
        
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        cart_count = Cart.objects.filter(user=request.user).count()
        
        return JsonResponse({
            'success': True,
            'cart_count': cart_count,
            'message': f'{product.title} added to cart!'
        })
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

@login_required
def get_cart_items(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    cart_data = []
    total_price = 0
    
    for item in cart_items:
        item_total = item.quantity * item.product.discount_price
        total_price += item_total
        cart_data.append({
            'id': item.product.id,
            'name': item.product.title,
            'quantity': item.quantity,
            'unit_price': float(item.product.discount_price),
            'total_price': float(item_total)
        })
    
    return JsonResponse({
        'cart_items': cart_data,
        'total_price': float(total_price),
        'cart_count': len(cart_data)
    })

@login_required
def checkout(request):
    if request.method == "POST":
        # Get cart items for the user
        cart_items = Cart.objects.filter(user=request.user).select_related('product')
        
        if not cart_items.exists():
            messages.error(request, "Your cart is empty!")
            return redirect('checkout')
        
        # Create items string and calculate total
        items_list = []
        total_order = 0
        for item in cart_items:
            item_total = item.quantity * item.product.discount_price
            items_list.append(f"{item.product.title} x {item.quantity}")
            total_order += item_total
        
        items = ", ".join(items_list)
        
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        name = first_name + " " + last_name
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        address2 = request.POST.get("address2", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")

        order = Order(
            user=request.user,  # Associate order with user
            items=items,
            total_order=total_order,
            name=name,
            email=email,
            address=address,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code
        )
        order.save()
        
        # Clear cart after successful order
        cart_items.delete()
        
        return render(request, 'shop/checkout.html', {"success": True})
    
    # GET request - show cart items
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total_price = sum(item.quantity * item.product.discount_price for item in cart_items)
    
    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'shop/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'shop/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')