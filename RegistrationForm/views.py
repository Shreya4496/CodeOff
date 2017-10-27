from django.shortcuts import render
from .form import UserForm
# Create your views here.
def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.username = request.session.get('username')
            data.save()
            return render(request, 'dashboard.html')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})