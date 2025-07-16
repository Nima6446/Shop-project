from django.core.paginator import Paginator
from django.db.models import Q, Case, When, IntegerField
from django.shortcuts import render
from product_module.models import product


def search_view(request):
    query = request.GET.get('query', '')
    products = []

    if query:
        products = product.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(short_description__icontains=query) |
            Q(slug__icontains=query) |
            Q(brand__title__icontains=query) |
            Q(category__title__icontains=query) |
            Q(products_tag__caption__icontains=query)
        ).annotate(
            priority=Case(
                When(title__istartswith=query, then=0),
                When(title__icontains=query, then=1),
                default=2,
                output_field=IntegerField()
            )
        ).distinct().order_by('priority')

    # صفحه‌بندی
    page_number = request.GET.get('page', 1)
    paginator = Paginator(products, 12)  # مثلا 12 محصول در هر صفحه
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_module/search_list.html', {
        'query': query,
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'paginator': paginator,
    })
