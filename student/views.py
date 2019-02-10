from django.shortcuts import render




def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form=UserRegisterForm()

        return render(request,'pages/register.html',{'form':form})