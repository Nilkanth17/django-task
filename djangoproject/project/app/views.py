from django.shortcuts import render,redirect
from app.models import *
import json 
import time
from datetime import date
from datetime import datetime, time
from django.http import JsonResponse
from rest_framework.decorators import api_view
import re
from django.conf import settings
from .Serializers import *
from app.views import *
from django.db.models import Q
from django.contrib.auth.models import User ###
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

 #nilkanth 
 
# Create your views here.
@api_view(['POST'])
def view_createc(request):
    data=request.POST

    cat = data.get('category_name')

    Category.objects.create(
        name=cat,
        
    )

    return JsonResponse({'msg': 'ok'})

@api_view(['POST'])
def view_Subcatcreate(request):
    data = request.POST
    name = data.get('name')
    category_id = data.get('category_id')

    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return JsonResponse({'msg': 'Category id not match'})

    subcategory = SubCategory.objects.create(name=name, category=category)

    return JsonResponse({'msg': 'sub create '})

@api_view(['GET'])
def View_catview(request):
    category = Category.objects.all()
    print(category)
    list1 = []
    for i in category:
       list1.append({'id':i.id,'name':i.name})

    print(list1)
    return JsonResponse({'Category': list1})
    
@api_view(['GET'])
def Sub_view(request):
    sc = SubCategory.objects.all() 

    list2=[]
      
    for i in sc:
        try:
            category_name = Category.objects.get(id=i.category_id).name
            print(category_name)
        except Category.DoesNotExist:
            category_name = ""
        data = {'id':i.id,'name':i.name,'category_id':i.category_id,'category_name':category_name}

        list2.append(data)
    
    return JsonResponse({'data1': list2})

@api_view(['GET'])
def sub_view1(request):
    list2=[]
    sc = SubCategory.objects.get(id=3) 
    category_name = Category.objects.get(id=sc.category_id).name
    data = {'id':sc.id,'name':sc.name,'category_id':sc.category_id,'category_name':category_name}
    print(sc)

    list2.append(data)
    
    return JsonResponse({'data1': list2})
     
@api_view(['POST'])
def sub_view2(request):
    a=request.POST['id']
    list2=[]
    try:
        sc = SubCategory.objects.get(id=a) 

        try:
            category_name = Category.objects.get(id=sc.category_id).name
            print(SubCategory)

        except Category.DoesNotExist:
            category_name = ""
        
        data = {'id':sc.id,'name':sc.name,'category_id':sc.category_id,'category_name':category_name}

        list2.append(data)
        return JsonResponse({'data1': list2})
    except SubCategory.DoesNotExist:
        return JsonResponse({'data1':list2})
    
@api_view(['POST'])
def sub_view3(request):#
    list2=[]
    a=request.POST.get('id', None)

    if a:
        sc = SubCategory.objects.get(category_id=a) 
        try:
            category_name = Category.objects.get(id=sc.category_id).name
            print(SubCategory)

        except Category.DoesNotExist:
            category_name = ""

        data = {'sub_id':sc.id,'Sub_name':sc.name,'category_id':sc.category_id,'category_name':category_name}

        list2.append(data)
    else:
        sc = SubCategory.objects.all()
        for i in sc:
            try:
                category_name = Category.objects.get(id=i.category_id).name

            except Category.DoesNotExist:
                category_name = ""

            data = {'Sub_id':i.id,'Sub_name':i.name,'category_id':i.category_id,'category_name':category_name}

            list2.append(data)
            
    return JsonResponse({'data':list2})

@api_view(['POST'])
def filter_cat(request):
    list2=[]
    a=request.POST.get('category_id', None)


    sc = SubCategory.objects.filter(category_id=a)
    for i in sc:

        try:
            category_name = Category.objects.get(id=i.category_id).name
        except Category.DoesNotExist:
            category_name = ""
        data = {'id':i.id,'name':i.name,'category_id':i.category_id,'category_name':category_name}
        print('ok')
        print('data', data)

        list2.append(data)
        
    return JsonResponse({'data1': list2})

@api_view(['POST'])
def Cat_Update(request):

    id = request.POST.get('category_id')
    cat = request.POST.get('category_name')
    try :
        sc = Category.objects.get(id=id)

        if cat != '': 
            sc.name=cat
        sc.save

        return JsonResponse({'msg': 'Update'})
    except Category.DoesNotExist:
        return JsonResponse({'msg': 'id not match'})
    
@api_view(['POST'])
def sub_Update(request):

    category_id = request.POST.get('category_id')
    sub_id = request.POST.get('s_id')
    sub_name = request.POST.get('s_name')

    try:
        sub_category = SubCategory.objects.get(id=sub_id)
        category = Category.objects.get(id=category_id)

        if category_id != '':
            sub_category.category_id = category_id
            
        if sub_name != '':
            sub_category.name = sub_name

        sub_category.save()

        return JsonResponse({'msg': 'Update'})
    
    except SubCategory.DoesNotExist:
        return JsonResponse({'msg': 'Sub cat id not match'})

    except Category.DoesNotExist:
        return JsonResponse({'msg': 'id not match'})

@api_view(['POST'])
def cat_delete(request):
    try:
        category_id_sc = request.POST.get('category_id')
        category = Category.objects.get(id=category_id_sc)

        category.delete()

        return JsonResponse({'msg': 'remove'})

    except Category.DoesNotExist:
        return JsonResponse({'msg': 'id not match'})
    except ValueError:
        return JsonResponse({'msg':'ValueError'})
    
@api_view(['POST'])
def view_create(request):

    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('Description')
    image = request.FILES.get('file')
    print("____----___")
    print(name)
    print(price)
    print(description)
    print(image)

    item.objects.create(name=name, price=price, Description=description, image=image)

    return JsonResponse({'msg': 'ok'})


@api_view(['GET'])
def item_view(request):
    iv = item.objects.all()

    list=[]
  
    for i in iv:
        a = 'http://'+ request.META['HTTP_HOST']+'/media/'+str(i.image)
        print(a)

        list.append({'item_id':i.id,'item_mname':i.name,'item_price':i.price,'item_discription':i.description,'item_image':a,})


    return JsonResponse({'items':list})


@api_view(['GET'])
def item_viewall(request):
    iv = item.objects.all()
    
    print(iv)   
    print('---------')

    list=[]
  
    for i in iv:
       # print('--------------------->>>>>>>',i.subcategoryid.id if i.subcategoryid.id != None else None)
        try :
            if i.subcategory != None :
                sc = SubCategory.objects.get(id=i.subcategory.id )
                
            else:
               sc =  None
            if i.category != None :

                c = Category.objects.get(id=i.category.id) 
            else:   
                 c =None
        
            a = 'http://'+ request.META['HTTP_HOST']+'/media/'+str(i.image)

            list.append({'item_id':i.id,'item_name':i.name,'item_price':i.price,'item_discription':i.description,'Category id':c.id if c != None else None,'category name': c.name, 'subcategory id': sc.id  if sc != None else None , 'Subcategory name': sc.name, 
                        'datetime':i.created_at,'item_image':a})
        except SubCategory.DoesNotExist:
            sc.name = ""
        except Category.DoesNotExist:
            category_name = ""

    return JsonResponse({'items':list})

@api_view(['POST'])
def item_Create(request):
    category = request.POST.get('category_id')
    subcategory = request.POST.get('subcategory_id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('description')   
    image = request.FILES.get('file')

    try:
        category = Category.objects.get(id=category)
        #subcategory = SubCategory.objects.get(id=subcategory, category = category)
        subcategory = SubCategory.objects.get(id=subcategory)

        if not category == subcategory.category:
            return JsonResponse({'message':'this subcategory does not belongs to category'})

    except Category.DoesNotExist:
        return JsonResponse({'msg': 'Category id not match'})
    except SubCategory.DoesNotExist:
        return JsonResponse({'msg': 'Subcategory id not match'})

    item.objects.create(category=category,subcategory=subcategory,name=name,price=price,description=description,image=image)

    return JsonResponse({'msg': 'ok'})

@api_view(['POST'])#
def item_datefilter(request):
    startdate = request.POST.get('s_date')
    endtdate = request.POST.get('e_date',date.today())
    starttime = time(0, 0, 0)  
    endtime = time(23, 59, 59) 

    start_datetime = datetime.strptime(f'{startdate} {starttime}', "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(f'{endtdate} {endtime}', "%Y-%m-%d %H:%M:%S")
    
    item_object = item.objects.filter(created_at__range=(start_datetime, end_datetime))
    list = []
    for i in item_object:
        try:
            if i.subcategory:
                sub_category = SubCategory.objects.get(id=i.subcategory.id)
            else:
                sub_category = None

            if i.category:
                category = Category.objects.get(id=i.category.id)
            else:
                category = None

           # image_stored = 'http://' + request.META['HTTP_HOST'] + '/media/' + str(i.image)
            image_stored = settings.MEDIA_ROOT + str(i.image)

            list.append({'item_id': i.id,'item_name': i.name,'item_price': i.price,'item_description': i.description,'category_id': category.id ,'category_name': category.name ,'subcategory_id': sub_category.id ,'subcategory_name': sub_category.name ,'date_time': i.created_at,'item_image': image_stored})
        except SubCategory.DoesNotExist:
            sub_category.name = ""
        except Category.DoesNotExist:
            category.name = ""

    return JsonResponse({'items':list})

@api_view(['POST'])
def item_datefilter1(request):

    startdate = request.POST.get('s_date')
    d = date.today()
    endtdate = request.POST.get('e_date',d)



    #start_datetime = datetime.strptime(f'{startdate} {starttime}', "%Y-%m-%d %H:%M:%S")
    #end_datetime = datetime.strptime(f'{endtdate} {endtime}', "%Y-%m-%d %H:%M:%S")
    
    iv = item.objects.filter(created_at__range=(startdate,endtdate))
   

    list = []
    print('__________________>>>>>>>>>>>>')
    print(startdate)
    print(endtdate)

    for i in iv:
        try:
            if i.subcategory:
                sc = SubCategory.objects.get(id=i.subcategory.id)
            else:
                sc = None

            if i.category:
                c = Category.objects.get(id=i.category.id)
            else:
                c = None

            a =  settings.MEDIA_URL + str(i.image)

            list.append({'item_id': i.id,'item_name': i.name,'item_price': i.price,'item_description': i.description,'Category id': c.id ,'category name': c.name ,'subcategory id': sc.id ,'Subcategory name': sc.name ,'datetime': i.created_at,'item_image': a})
        except SubCategory.DoesNotExist:
            sc.name = ""
        except Category.DoesNotExist:
            category_name = ""

    return JsonResponse({'items':list})
    
@api_view(['POST'])
def item_view_filter(request):
    startdate = request.POST.get('s_date')
    endtdate = request.POST.get('e_date',date.today())
    starttime = time(0, 0, 0)  
    endtime = time(23, 59, 59) 
    list = []
    if startdate:
        start_datetime = datetime.strptime(f'{startdate} {starttime}', "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime(f'{endtdate} {endtime}', "%Y-%m-%d %H:%M:%S")        
        item_object = item.objects.filter(created_at__range=(start_datetime, end_datetime))
        
    else:
        item_object = item.objects.all()

    for i in item_object:        
        try:
            if i.subcategory:
                sub_category = SubCategory.objects.get(id=i.subcategory.id)
            else:
                sub_category = None
            if i.category:
                category = Category.objects.get(id=i.category.id)
            else:
                category = None
            image_stored = settings.MEDIA_URL + str(i.image)

        except SubCategory.DoesNotExist:
            sub_category.name = ""
        except Category.DoesNotExist:
            category.name = ""

        image_stored = settings.MEDIA_URL + str(i.image)
        list.append({'item_id': i.id,'item_name': i.name,'item_price': i.price,'item_description': i.description,'category_id': category.id ,'category_name': category.name ,'subcategory_id': sub_category.id ,'subcategory_name': sub_category.name ,'date_time': i.created_at,'item_image': image_stored })
    total_itam = len(list)
    print("_____________>>>>>>>>>>>")
    print (total_itam)
    return JsonResponse({'items':list, 'total_item': total_itam})

@api_view(['GET'])
def student_data(request):
    students = Student.objects.all()
    model_serializer = StudentModelSerializer(students, many=True)
    return JsonResponse({'data1':model_serializer.data})

@api_view(['POST'])
def student_viewid(request):
    s_id=request.POST.get('Student_id',None)

    if s_id is None:
        return JsonResponse({'msg': 'Student ID None'})
    try:
        students = Student.objects.get(id = s_id)
        model_serializer = StudentModelSerializer(students, many=False)
        return JsonResponse({'data':model_serializer.data})
    
    except Student.DoesNotExist:
      return JsonResponse({'msg':'Student not found'})
    except ValueError:
        return JsonResponse({'msg':'Value Error'})
    
@api_view(['GET'])
def student_datac(request):
    students = Student.objects.all()
    model_serializer = StudentModelSerializer(students, many=True)
    return JsonResponse({'data1':model_serializer.data}) 

@api_view(['POST'])
def studentpage_create(request):
    serializer = StudentModelSerializer(data=request.data)
    print(serializer)
    print('-------------------->>>>>>>>')
    print(request.data)
    print('-------------------->>>>>>>>')

    category_id = request.data.get('category')

    subcategory_id = request.data.get('subcategory')
    print(category_id)
    print(subcategory_id)
    print('************************************')
    if category_id is "":
        return JsonResponse({'msg': 'Category id not found'}) 
    if subcategory_id is "":
        return JsonResponse({'msg': 'Subcategory id not found'}) 
        
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    
    return JsonResponse(serializer.errors)


@api_view(['POST'])
def item_filters(request):
    query_data = request.data.get('query', '')
    startdate = request.POST.get('s_date')
    endtdate = request.POST.get('e_date',date.today())
    starttime = time(0, 0, 0)  
    endtime = time(23, 59, 59) 

    if startdate:
        start_datetime = datetime.strptime(f'{startdate} {starttime}', "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime(f'{endtdate} {endtime}', "%Y-%m-%d %H:%M:%S")        
        item_data = item.objects.filter(created_at__range=(start_datetime, end_datetime))
        
    else:
        item_data = item.objects.all()

    if query_data :
        item_data = item_data.filter(Q(name__icontains=query_data) |Q(price__icontains=query_data) |Q(description__icontains=query_data) |Q(category__name__icontains=query_data) |Q(subcategory__name__icontains=query_data) |Q(created_at__icontains=query_data) |Q(image__icontains=query_data))

    serializer = iteamModelSerializer(item_data, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def create_register_page(request):
    username = request.data.get('username')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    is_superuser = request.data.get('is_superuser', False)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"msg": "Change Username"})

    user_data = {'username': username,'password': password,'first_name': first_name,'last_name': last_name,'last_name': last_name,'email': email,'is_superuser': is_superuser}
    print(user_data)

    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"msg": "Registration successful"})
    else:
        return JsonResponse(serializer.errors)

@api_view(['POST'])
def create_login_page(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # try:
    user = User.objects.get(username=username)
    if user.password == password:
        if user.is_superuser:
            return JsonResponse({'msg': 'Login Superuser'})
        else:
            return JsonResponse({'msg': 'Login Successful'})
    else:
        return JsonResponse({'msg': 'Password incorrect'})

    # except User.DoesNotExist:
    #     return JsonResponse({'msg': 'User not found'})
    # except Exception as e:
    #     return JsonResponse({'error': True, 'message': str(e)})
 
@api_view(['POST'])
def create_register_pagemodel(request):
    username = request.data.get('username')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    is_superuser = request.data.get('is_superuser', False)


    try:
        if User.objects.filter(username=username).exists():
            return JsonResponse({"msg": "Change Username"})
        user = User.objects.create(username=username, password=password, email=email, first_name=first_name, last_name=last_name, is_superuser=is_superuser)
        return JsonResponse({"msg": "Registration successful"})
    except Exception as e:
        return JsonResponse({'error': True, 'message': str(e)})
    

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors)


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    if not username or not password:
        return JsonResponse({'msg': 'Username and password are required'})

    if User.objects.filter(username=username).exists():
        return JsonResponse({'msg': 'Username already ragister'})

    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
    token, created = Token.objects.get_or_create(user=user)
    return JsonResponse({'token': token.key})

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key})
    else:
        return JsonResponse({'msg': 'Invalid Credentials'})


@api_view(['POST'])
def ragistertoken(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return JsonResponse({'refresh': str(refresh),'access': str(refresh.access_token),})
    return JsonResponse(serializer.errors)

@api_view(['POST'])
def logintoken(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({'refresh': str(refresh),'access': str(refresh.access_token),})
        return JsonResponse({'msg': 'Invalid '})
    return JsonResponse(serializer.errors)
