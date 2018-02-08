from django.shortcuts import render, redirect
from django.views import View
from .models import CustomerMaster
from django.http import HttpResponse


def CustomerDelete(request, user_id):
    CustomerMaster.objects.get(id=user_id).delete()
    return redirect("../../customer")


def CustomerEdit(request, user_id):
    edit_data = CustomerMaster.objects.get(pk=user_id)
    return render(request, 'Customer.html', locals())


class CustomerList(View):

    template ='Customer.html'

    def get(self, request):
        Customer = CustomerMaster.objects.all()
        return render(request, self.template, locals())

    def post(self, request):
        if request.method == 'POST':
            if 'txtSubmit' in request.POST:
                Price = request.POST.get("txtName", None)
                insert_record = CustomerMaster(Price=Price)
                insert_record.save()
                return redirect("../customer")
            elif 'txtUpdate' in request.POST:
                id_ = request.POST.get("txtid", None)
                edit_Customer =CustomerMaster.objects.get(pk=id_)
                edit_Customer.Price = request.POST.get("txtName", None)
                edit_Customer.save()
                return redirect("../customer")











