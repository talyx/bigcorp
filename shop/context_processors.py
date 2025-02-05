from .models import Category

def categories(request):
    """
    Returns a dictionary containing top-level categories.
    
    This function retrieves all Category objects that do not have a parent,
    indicating they are top-level categories. It is intended to be used as
    a context processor to make these categories available in templates.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        dict: A dictionary with a single key 'categories' containing a queryset
        of top-level Category objects.
    """

    categories = Category.objects.filter(parent=None)
    return {'categories': categories}