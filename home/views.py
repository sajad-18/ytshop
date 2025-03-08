from django.shortcuts import render
from django.views import View
from ads.models import Ads
from .models import Post
from .forms import ProductFilterForm
from django.core.paginator import Paginator


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        ads = Ads.objects.filter(verification=True)
        last_20_ads = ads.order_by('-id')[:8]
        return render(request, 'home/home.html', {'ads': last_20_ads, 'posts': posts})


class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Post.objects.get(pk=post_id, slug=post_slug)
        return render(request, 'home/blog.html', {'post': post})


class StoreView(View):
    def get(self, request):
        ads = Ads.objects.filter(verification=True)
        paginator = Paginator(ads, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if page_number is not None and page_number.isdigit():
            page_number = int(page_number)
            if page_number < 1:
                page_number = 1
        else:
            page_number = 1
        filter_form = ProductFilterForm(request.GET)
        if filter_form.is_valid():
            if filter_form.cleaned_data.get('price_asc'):
                ads = ads.order_by('price')
            elif filter_form.cleaned_data.get('price_desc'):
                ads = ads.order_by('-price')
            regions = filter_form.cleaned_data.get('region')
            if regions:
                ads = ads.filter(region__in=regions)
            price_range = filter_form.cleaned_data.get('price_range')

            if price_range:
                price_min, price_max = map(int, price_range.split('-'))
                ads = ads.filter(price__range=(price_min, price_max))

        return render(request, 'home/store.html', {'ads': ads, 'filter_form': filter_form, 'page_obj': page_obj})
