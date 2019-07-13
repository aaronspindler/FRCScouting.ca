from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def test(request):
    return render(request, 'test.html')
