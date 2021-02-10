from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import *
from .models import *
from datetime import datetime
from django.db.models import Max, functions


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
    # print('*> serchmenu :')
    menus = Menu.objects.all()
    # print('menus', menus)
    context = {'menus': menus}
    # print('-------------------------------------')

    return render(request, 'order.html', context)


def saveOrder(request) :
    # ---------------------------
    # 0. 브라우저에서 넘어오는 데이터 확인
    # ---------------------------
    mID = request.POST.getlist('hmid[]')
    mPrice = request.POST.getlist('hprice[]')
    mQty = request.POST.getlist('hqty[]')
    mAmount = request.POST.getlist('hsum[]')

    mPay = request.POST.get('payment')
    mStat = request.POST.get('hstat')

    print('mID ', mID)
    print('mPrice ', mPrice)
    print('mQty ', mQty)
    print('mAmount',mAmount)

    print('mPay ', mPay )
    print('mStat ', mStat)

    # ---------------------------
    # 1. orderno 채번
    # ---------------------------
    today = datetime.today()
    todate = datetime.strftime(today, '%Y-%m-%d')

    # 주문번호 : RYYYYMMDD + '00001'
    new_orderno = 'R' + datetime.strftime(today, '%Y%m%d') + '00001'

    # 주문번호 : 당일 주문  조회
    od = Order.objects.values('orderdate').filter(orderdate=todate).annotate(max_orderno=Max('orderno'))

    # 주문번호 : 당일 주문 있으면  다음번호 채번
    if od:
        a = od[0]['max_orderno']
        new_orderno = 'R' + datetime.strftime(today, '%Y%m%d') + str(int(a[9:]) + 1).zfill(5)
    # print('new_orderno - ', new_orderno)

    # -------------------------------
    # 2. 날짜분할(orderdate, ordertime)
    # -------------------------------

    # 주문날짜(orderdate)
    mDate = datetime.strftime(today, '%Y-%m-%d')

    # 주문시간(ordertime)
    mTime = datetime.strftime(today, '%H:%M:%S')

    # -------------------------------
    # 3. Order 테이블 저장
    # -------------------------------
    ord = Order(orderno=new_orderno,
                orderdate=mDate,
                ordertime=mTime,
                payment=mPay,
                status = mStat)
    ord.save()
    print(ord)

    # -------------------------------
    # 4. OrderDetail 테이블 저장
    # -------------------------------
    # menuid는 menu테이블의 PK이기 때문에 아래와 같이 menuid를 menu테이블로부터 참조해서 가져와서 더 리스트에 담는 작업을 해야함
    menuList = []
    for i in range(len(mID)) :
        menu = Menu.objects.get(menuid=mID[i])
        menuList.append(menu)
    # print('menuList-----',menuList)
    print('----',mAmount[-1])

    for i in range(len(mID)):
        ordd = OrderDetail(
            orderno = ord,
            menuid = menuList[i],
            price = mPrice[i],
            qty = mQty[i],
            sales = mAmount[-1],
        )
        ordd.save()
        print(ordd)
    # ---------------------------------
    return redirect('order')


#----------------------< 심영석 >----------------------#
# ----------------------< 회원가입 페이지 START >-------------------- #
def registerForm(request):
    return render(request, 'registerForm.html')
# ----------------------< 회원가입 페이지 END >---------------------- #
# ----------------------< 회원등록 기능 START >-------------------- #
def register(request):
    if request.method == 'POST' :
        # s_registerForm에서 넘어온 값들을 새로운 변수에 담고
        id = request.POST['new_id']
        pwd = request.POST['new_pwd']
        mail = request.POST['new_mail']
        # register에 User 클래스를 이용해서 각 객체에 담아서
        register = User(user_id=id, user_pwd=pwd, user_mail=mail)
        # 저장
        register.save()
    return render(request, 'index.html')
# ----------------------< 회원등록 기능 END >-------------------- #
# ----------------------< 로그인 기능 START >-------------------- #
def login(request):
    if request.method =='POST':
        id = request.POST['username']
        pwd = request.POST['password']
        user = User.objects.get(user_id = id, user_pwd = pwd)
        if user is not None :
            return redirect('order')  # 로그인 후 주문 페이지로 분기
        else :
            return render(request, 'index.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'index.html')
# ----------------------< 로그인 기능 END >-------------------- #
# ----------------------< 로그아웃 기능 START >-------------------- #
def logout(request):
    request.session['user_name'] = {}
    request.session['user_id'] = {}
    request.session.modified = True
    return redirect('index')
# ----------------------< 로그아웃 기능 END >-------------------- #
#----------------------< 박우환 >----------------------#


#----------------------< 오은영 >----------------------#


#----------------------< 정연욱 >----------------------#
# menu page
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
    menuId = request.POST.get('menuId','0')
    menuName = request.POST.get('menuName', '0')
    menuPrice = request.POST.get('menuPrice',0)
    print(menuId, menuName, menuPrice)
    # 데이터 저장
    pro = Menu(menuid=menuId,menuname=menuName, price=menuPrice)
    pro.save()

    return redirect('serchmenu')
# 샘플CRUD - 수정
def updatemenu(request):
    print('*> updateProduct :')
    # Client 값 확인

    #id = request.POST['id']

    menuId = request.POST.get('menuId', '0')
    menuName=request.POST.get('menuName', '0')
    menuPrice=request.POST.get('menuPrice', 0 )

    print('request modify - ', menuId, menuName, menuPrice)

    # 데이터 수정
    men = Menu.objects.get(menuid=menuId)
    men.menuname = menuName
    men.price = menuPrice
    men.save()
    return redirect('serchmenu')

# menu- 삭제
def deletemenu(request):
    print('*> deleteProduct :')
    # Client 값 확인
    menuId = request.POST.get('menuId','0')
    print('request bbs_remove param - ' , menuId)
    # 데이터 수정
    Menu.objects.get(menuid=menuId).delete()
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
    print('-------------------')
    print(pdName,pdPrice)
    # 데이터 저장
    pro=SampleProduct(pd_name = pdName,pd_price = pdPrice)
    pro.save()

    return redirect('serchProduct')

# 샘플CRUD - 수정
def updateProduct(request):
    print('*> updateProduct :')
    # Client 값 확인

    #id = request.POST['id']

    pID = request.POST.get('pID', '0')
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
    pID = request.POST.get('pID','0')
    print('request bbs_remove param - ' , pID)
    # 데이터 수정
    SampleProduct.objects.get(id=pID).delete()
    #화면이동
    return redirect('serchProduct')





