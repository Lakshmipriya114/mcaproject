from django.shortcuts import render, redirect
from . models import UserPredictModel, UserPersonalModel
from . forms import UserPersonalForm, UserPredictForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
from tensorflow import keras
from PIL import Image, ImageOps
from . import forms


def Home1(request):
    return render(request, 'Home1.html')

def Register(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login')

    context = {'form':form}
    return render(request, 'Register.html', context)


def Login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home2')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'Login.html', context)

def Home2(request):
    return render(request, 'Home2.html')

def Logout(request):
    logout(request)
    return redirect('Home1')

def Info(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, 'Home2.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, 'Info.html', {'form':form})
    
def Deploy(request):
    print("HI")
    if request.method == "POST":
        form = forms.UserPredictForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance

        result1 = UserPredictModel.objects.latest('id')
        models = keras.models.load_model('C:/Users/admin/Music/BIRDS SPECIES/BIRDS SPECIES/DEPLOYMENT/PROJECT/APP/LENET.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("C:/Users/admin/Music/BIRDS SPECIES/BIRDS SPECIES/DEPLOYMENT/PROJECT/media/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['ABBOTTS BABBLER','ABBOTTS BOOBY','ABYSSINIAN GROUND HORNBILL','AFRICAN CROWNED CRANE','AFRICAN EMERALD CUCKOO',
                   'AFRICAN FIREFINCH','AFRICAN OYSTER CATCHER','AFRICAN PIED HORNBILL','AFRICAN PYGMY GOOSE','ALBATROSS',
                   'ALBERTS TOWHEE','ALEXANDRINE PARAKEET','ALPINE CHOUGH','ALTAMIRA YELLOWTHROAT','AMERICAN AVOCET',
                   'AMERICAN BITTERN','AMERICAN COOT','AMERICAN FLAMINGO','AMERICAN GOLDFINCH','AMERICAN KESTREL']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == 'ABBOTTS BABBLER':
            a = 'ABBOTTS BABBLER'
        elif a == 'ABBOTTS BOOBY':
            a = 'ABBOTTS BOOBY'
        elif a == 'ABYSSINIAN GROUND HORNBILL':
            a = 'ABYSSINIAN GROUND HORNBILL'
        elif a == 'AFRICAN CROWNED CRANE':
            a = 'AFRICAN CROWNED CRANE'
        elif a == 'AFRICAN EMERALD CUCKOO':
            a = 'AFRICAN EMERALD CUCKOO'
        elif a == 'AFRICAN FIREFINCH':
            a = 'AFRICAN FIREFINCH'
        elif a == 'AFRICAN OYSTER CATCHER':
            a = 'AFRICAN OYSTER CATCHER'
        elif a == 'AFRICAN PIED HORNBILL':
            a = 'AFRICAN PIED HORNBILL'
        elif a == 'AFRICAN PYGMY GOOSE':
            a = 'AFRICAN PYGMY GOOSE'
        elif a == 'ALBATROSS':
            a = 'ALBATROSS'
        elif a == 'ALBERTS TOWHEE':
            a = 'ALBERTS TOWHEE'
        elif a == 'ALEXANDRINE PARAKEET':
            a = 'ALEXANDRINE PARAKEET'
        elif a == 'ALPINE CHOUGH':
            a = 'ALPINE CHOUGH'
        elif a == 'ALTAMIRA YELLOWTHROAT':
            a = 'ALTAMIRA YELLOWTHROAT'
        elif a == 'AMERICAN AVOCET':
            a = 'AMERICAN AVOCET'
        elif a == 'AMERICAN BITTERN':
            a = 'AMERICAN BITTERN'
        elif a == 'AMERICAN COOT':
            a = 'AMERICAN COOT'
        elif a == 'AMERICAN FLAMINGO':
            a = 'AMERICAN FLAMINGO'
        elif a == 'AMERICAN GOLDFINCH':
            a = 'AMERICAN GOLDFINCH'
        elif a == 'AMERICAN KESTREL':
            a = 'AMERICAN KESTREL'
     

        else:
            a = 'WRONG INPUT'
        
        return render(request, 'Deploy.html',{'form':form,'obj':obj,'predict':a})
    else:
        form = forms.UserPredictForm()
    return render(request, 'Deploy.html',{'form':form})

def Problem_Statement(request):
    return render(request,'ProblemStatement.html')

def Team(request):
    return render(request,'Team.html')

def Result(request):
    return render(request,'Result.html')

def Database1(request):
    models = UserPredictModel.objects.all()
    return render(request, 'Database1.html', {'models':models})

def Database2(request):
    models = UserPersonalModel.objects.all()
    return render(request, 'Database2.html', {'models':models})


