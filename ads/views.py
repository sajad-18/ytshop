from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import View
from .models import Ads
from .forms import AdCreateForm
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from orders.forms import CartAddForm


class AdsView(View):
    def get(self, request):
        return render(request, 'ads/ad-register.html')


class AdCreateView(LoginRequiredMixin, View):
    form_class = AdCreateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'ads/ad-register2.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_ad = form.save(commit=False)
            new_ad.user = request.user
            new_ad.name = 'اکانت call of duty شماره'
            new_ad.save()
            messages.success(request, "آگهی شما با موفقیت ساخته شد.", 'success')
            return redirect('ads:ad_detail', new_ad.id)
        messages.error(request, 'لطفا اطلاعات را کامل وارد نمایید', 'danger')
        return render(request, 'ads/ad-register2.html', {'form': form})


class AdDetailView(View):
    def get(self, request, ad_id):
        ad = get_object_or_404(Ads, id=ad_id)
        form = CartAddForm()
        return render(request, 'home/product.html', {'ad': ad, 'form': form})

