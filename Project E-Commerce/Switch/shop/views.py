from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product, Category, Contact, Order
from django.core.paginator import Paginator
# Create your views here.
def view(request):
    return render(request, 'shop/base.html', {'categories': Category.objects.all})

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {'products': products, 'categories': categories})

def about(request):
    return render(request, 'shop/about.html', {'categories': Category.objects.all()})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('Name', '')
        email = request.POST.get('Email', '')
        phone = request.POST.get('Phone', '')
        message = request.POST.get('Message', '')
        contact = Contact(name=name, email=email, phone=phone, msg_description=message)
        contact.save()
    return render(request, 'shop/contact.html', {'categories': Category.objects.all()})

def product(request):
    category_name = request.GET.get('category')  # Get selected category
    if category_name:
        all_products = Product.objects.filter(category__category_name=category_name)
    else:
        all_products = Product.objects.all()
    paginator = Paginator(all_products, 9)  # 9 products per page
    page_number = request.GET.get('page')   # Get ?page= value from URL
    page_obj = paginator.get_page(page_number)
    print(page_obj.paginator.page_range)
    return render(request, 'shop/product.html', {'products': page_obj, 'current_category': category_name, 'categories': Category.objects.all()})

def prodView(request, id):
    product = Product.objects.get(prod_id=id)
    print(product)
    return render(request, 'shop/prodview.html', {'product':product, 'categories': Category.objects.all()})

def checkOut(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('first_name', '') + " " + request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')

        order = Order(
            items_json=items_json,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone
        )
        order.save()
        return render(request, 'shop/checkout.html', {'orderPlaced': True})

    return render(request, 'shop/checkout.html')

def search(request):
    return HttpResponse("We are at SEARCH page.")

