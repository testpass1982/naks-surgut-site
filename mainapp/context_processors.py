from .models import DocumentCategory, Post

def document_categories(request):
    try:
        categories = DocumentCategory.objects.all().order_by('number')
    except DocumentCategory.DoesNotExist:
        categories = {'message': 'Добавьте категории документов'}
    if categories.count() == 0:
        categories = {'message': 'Добавьте категории документов'}
    return {'document_categories': categories }

def service_descriptions(request):
    try:
        service_pages = Post.objects.filter(service_description=True).order_by('number')
    except Post.DoesNotExist:
        service_pages = {'message': 'Добавьте страницу с описанием услуги'}
    if service_pages.count() == 0:
       service_pages = {'message': 'Добавьте страницу с описанием услуги'}
    # import pdb; pdb.set_trace()
    return {'service_pages': service_pages}