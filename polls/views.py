from django.shortcuts import render
from datetime import datetime
from math import ceil
# Create your views here.
from django.http import HttpResponse
from polls.models import Contact
from polls.models import Product
from polls.models import Order
from django.contrib import messages

def index(request):
    products = Product.objects.all()
    n=len(products)
    params={'product':products, 'nCards':n}
    return render(request, 'index.html', params)

def category(request):   
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"category.html", params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        state=request.POST.get('state')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, state=state, phone=phone,
        desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated.')

       
    
    return render(request, 'contact.html')

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        state=request.POST.get('state')
        pin=request.POST.get('zip')
        order=Order(items_json=items_json, name=name, email=email, state=state, 
        address=address, pin=pin, date=datetime.today())
        order.save()
        messages.success(request, 'New Order')
        thank = True
        return render(request, 'checkout.html', {'thank':thank})
        
    return render(request, 'checkout.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'prodView.html', {'product':product})

def search(request):
    query=request.GET['query']
    if len(query)>50:
        products=Product.objects.none()
    else:
        prname= Product.objects.filter(name__icontains=query)
        prdesc= Product.objects.filter(desc__icontains=query)
        products= prname.union(prdesc)
    if products.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params ={'product':products, 'query':query,}
    return render(request, 'search.html', params)