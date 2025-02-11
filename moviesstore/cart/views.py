from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Movie
from .utils import calculate_cart_total

def index(request):
    """Display the shopping cart."""
    cart_total = 0
    movies_in_cart = []
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())

    if movie_ids:
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)
        cart_total = calculate_cart_total(cart, movies_in_cart)

    template_data = {
        'title': 'Cart',
        'movies_in_cart': movies_in_cart,
        'cart_total': cart_total
    }

    return render(request, 'cart/index.html', template_data)

def add(request, id):
    """Adds a movie to the cart or updates quantity if it already exists."""
    if request.method != 'POST':
        return redirect('movies.show', id=id)  # Redirect if accessed via GET

    get_object_or_404(Movie, id=id)  # Ensure movie exists
    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity', 1))  # Convert quantity to int

    # Ensure quantity is always stored as an integer
    cart[str(id)] = int(cart.get(str(id), 0)) + quantity

    request.session['cart'] = cart
    request.session.modified = True  # Ensure session updates

    return redirect('cart.index')

def clear(request):
    """Clears the shopping cart."""
    request.session['cart'] = {}
    request.session.modified = True  # Ensure session updates
    return redirect('cart.index')
