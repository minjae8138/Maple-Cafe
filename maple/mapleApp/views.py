


from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import *
from .models import *


#----------------------< 공통 : 메뉴이동>--------------------#

# landing / login
def index(request):
    return render(request,'index.html')

# order
# def order(request):
#     return render(request,'order.html')

# orderStatus
def orderStatus(request):
    return render(request,'orderStatus.html')

# menu
# def menu(request):
#     return render(request,'menu.html')

# staff
def staff(request):
    return render(request,'staff.html')

# salesStatus
def salesStatus(request):
    return render(request,'salesStatus.html')



#----------------------< 김민재 >----------------------#
def order(request):
    # return redirect('menuProduct')
    return redirect('serchorder')

def serchorder(request):
    print('*> serchmenu :')
    menus = Menu.objects.all()
    print('menus', menus)
    # title  writer  content  regdata  viewcnt
    # print('*>producs -', type(producs), producs)
    context = {'menus': menus}


    return render(request, 'order.html', context)


#----------------------< 심영석 >----------------------#

#----------------------< 박우환 >----------------------#


#----------------------< 오은영 >----------------------#


#----------------------< 정연욱 >----------------------#
# order page 실험
def menu(request):
    return redirect('serchmenu')


def serchmenu(request):
    print('*> serchmenu :')
    menus = Menu.objects.all()
    print('menus', menus)
    # title  writer  content  regdata  viewcnt
    # print('*>producs -', type(producs), producs)
    context = {'menus': menus}


    return render(request, 'menu.html', context)


# 샘플CRUD - 입력
def insertmenu(request):
    print('*> insertmenu :')

    # Client 값 확인
    mId = request.POST.get('menuId','0')
    menuName = request.POST.get('menuName', '0')
    menuPrice = request.POST.get('menuPrice',0)
    print('--------------------------------',mId)


    # 데이터 저장
    pro = Menu(menuid=mId, menuname=menuName, price=menuPrice)
    pro.save()

    return redirect('serchmenu')
# 샘플CRUD - 수정
def updatemenu(request):
    print('*> updateProduct :')
    # Client 값 확인

    #id = request.POST['id']

    mId = request.POST.get('menuid', 0)
    menuName=request.POST.get('menuname', '0')
    menuPrice=request.POST.get('price', 0 )

    print('request modify - ', mId, menuName, menuPrice)

    # 데이터 수정
    men = Menu.objects.get(menuid=mId)
    men.menuname = menuName
    men.price = menuPrice
    men.save()
    return redirect('serchmenu')

# menu- 삭제
def deletemenu(request):
    print('*> deleteProduct :')
    # Client 값 확인
    mId = request.POST.get('mId','0')
    print('request bbs_remove param - ' , mId)
    # 데이터 수정
    Menu.objects.get(menuid=mId).delete()
    #화면이동
    return redirect('serchmenu')




#----------------------< 최유숙 >----------------------#


#----------------------< sample >----------------------#
# 샘플화면 
def sampleUi(request):
    print('*> sampleUi :')
    
    return render(request,'sample_ui.html')
# 샘플CRUD - 상품관리 
def sampleCrud(request):
    print('*> sampleCrud :')
    
    return redirect('serchProduct')

# 샘플CRUD - 상품조회
def serchProduct(request):
    print('*> serchProduct :')
    producs = SampleProduct.objects.all()
    print('producs',producs)
    # title  writer  content  regdata  viewcnt
    # print('*>producs -', type(producs), producs)
    context = {'producs': producs}
    
    return render(request, 'sample_crud.html', context)

# 샘플CRUD - 입력
def insertProduct(request):
    print('*> insertProduct :')
    
    # Client 값 확인
    pdName=request.POST.get('pdName', '0')
    pdPrice=request.POST.get('pdPrice', 111)

    # 데이터 저장
    pro=SampleProduct(pd_name = pdName,pd_price = pdPrice)
    pro.save()

    return redirect('serchProduct')

# 샘플CRUD - 수정
def updateProduct(request):
    print('*> updateProduct :')
    # Client 값 확인

    #id = request.POST['id']

    pID = request.POST.get('pID', 0)
    pdName=request.POST.get('pdName', '0')
    pdPrice=request.POST.get('pdPrice', 0 )

    print('request modify - ', pID, pdName, pdPrice)

    # 데이터 수정
    pro = SampleProduct.objects.get(id=pID)
    pro.pd_name = pdName
    pro.pd_price = pdPrice
    pro.save()

    #화면이동
    return redirect('serchProduct')



# 샘플CRUD - 삭제
def deleteProduct(request):
    print('*> deleteProduct :')
    # Client 값 확인
    pID = request.POST.get('pID',0)
    print('request bbs_remove param - ' , pID)
    # 데이터 수정
    SampleProduct.objects.get(id=pID).delete()
    #화면이동
    return redirect('serchProduct')






