from .models import Post, Category

def cats(request):
    return {
        'all_categories': Category.objects.all(),
    }