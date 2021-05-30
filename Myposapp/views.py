from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Promotion,Employee,Product,Member,Product_order,Bill,History_promotion,Item_in_promotion,List_product,Promotion_member,Subscription_fee,Member_point,Sale,Profit
from django.contrib import messages
from localStoragePy import localStoragePy
from datetime import datetime
from django.db import connection
import time
from django.utils.timezone import datetime
from datetime import date

localStorage = localStoragePy('me.jkelol111.mypythonapp', 'json')

def loginForm(request):
    if request.user.is_authenticated:
        return redirect('/product')
    return render(request,'login.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    user = auth.authenticate(username=username,password=password)
    print("asdasdasdasd",user)
    if user is not None :
        auth.login(request,user)
        userlogin = User.objects.get(username=username)
        print(userlogin)
        em = Employee.objects.get(id_user=userlogin.id)
        localStorage.setItem('username',username )
        
        if em.Role == 'Admin':
            return redirect('/product')
        if em.Role == 'Finance':
            return redirect('/finance')
        if em.Role == 'Cashier':
            return redirect('/cashier')
        return redirect('/product')
    else:
        messages.info(request,'username or password not correct!!')
        return redirect('/loginForm')

@login_required
def Register(request):
    if request.method == 'POST':
        alldata = request.POST
        print(alldata['Firstname'])
        if alldata["password"] == alldata["repassword"]:
            if User.objects.filter(username=alldata["username"]).exists():
                print('Username มีคนใช้เเล้ว')
                return render(request,'Add_employee.html')
            else:
                user = User.objects.create_user(username=str(alldata["username"]),password=alldata["password"])
                user.save()
                datauser = User.objects.get(username=alldata["username"])
                print("-------------------------------------------------------------------------------------------s")
                addEmployee = Employee(id_user=datauser.id,Role=alldata['Role'],IDcard = alldata['IDcard'],
                Title_Name = alldata['Title_Name'],Firstname = alldata['Firstname'],Lastname=alldata['Lastname'],Age=alldata['Age'],Gender=alldata['Gender'],
                Email=alldata['email'],Phonenumber=alldata['Phonenumber'],Blood_Type=alldata['bloodtype'],Birthday=alldata['Birthday'],Ethnicity=alldata['Ethnicity'],
                Nationality=alldata['Nationality'],Religion=alldata['Religion'],Address=alldata['Address'],Maritial_Status=alldata['Maritial_Status'],Education_Level=alldata['Education_Level'],
                Emergency_Tel=alldata['Emergency_Tel'],Relationship=alldata['Relationship'],Father_Name=alldata['FatherFirstname'],Father_Lastname=alldata['FatherLastname'],
                Father_Career=alldata['FatherCareer'],Father_Tel=alldata['FatherPhonenumber'],Father_Ethnicty=alldata['FatherEthnicity'],Father_Nationallity=alldata['FatherNationality'],
                Father_Religion=alldata['FatherReligion'],Father_Address=alldata['FatherAddress'],Mother_Title=alldata['Mother_Title'],Mother_Name=alldata['MotherFirstname'],Mother_Lastname=alldata['MotherLastname'],
                Mother_Career=alldata.get('MotherCareer'),Mother_Tel=alldata['MotherPhonenumber'],Mother_Ethnicty=alldata['MotherEthnicity'],Mother_Nationallity=alldata['MotherNationality'],
                Mother_Religion=alldata['MotherReligion'],Mother_Address=alldata['MotherAddress'],status=1)	
                addEmployee.save()
                # IDcard	Title_Name	Firstname	Lastname	Age	Gender	Email	Phonenumber	Blood_Type	Birthday	Ethinity	Nationality	Religion	
                # Address	Maritial_Status	Education_Level	Emergency_Tel	Relationship	Father_Title	Father_Name	Father_Lastname	Career	Father_Tel	Father_Ethnicty	Father_Nationallity	Father_Religion	
                # Father_Address	Mother_Title	Mother_Name	Mother_Lastname	Mother_Career	Mother_Tel	Mother_Ethnicty	Mother_Religion	Mother_Address	Mother_Nationallity	Role	id_user_id	 )
                time.sleep(1)
                return redirect('/employee/')

        else:
            return render(request,'Add_employee.html')

    return render(request,'Add_employee.html')


def login_error(request):
    return render(request,'login_error.html')

@login_required
def product(request):
    title = "Product"
    data = Product.objects.all()
    return render(request,'product.html',{"title":title,"data":data})

@login_required
def Tax_report(request):
    data = Product.objects.all()
    return render(request,'Tax_report.html',{"data":data})

@login_required
def search_product(request):
    title = "Product"
    alldata = Product.objects.all()
    data = []
    Barcode = request.GET.get("Barcode")
    for i in alldata:
        print(i.id)
        if str(i.Barcode_ID) == str(Barcode):
            data.append(i)
    return render(request,'product.html',{"title":title, "data":data})

@login_required
def del_Product(request,pk):
    item = Product.objects.get(id=pk)
    item.status = 0
    item.save()
    return redirect('/product/')
    
@login_required
def add_Product(request):
    if request.method == 'POST':
        alldata = request.POST
        add = Product()
        add.Barcode_ID = alldata['Barcode']
        if Product.objects.filter(Barcode_ID=alldata["Barcode"]).exists():
            print('Barcode ใช้เเล้ว')
            return render(request,'add_product.html')
        add.Name = alldata['name']
        add.Size = alldata['inlineRadioOptions']
        add.Color = alldata['color']
        add.Type = alldata['type']
        add.Model = alldata['model']
        add.Cost = alldata['cost']
        add.Price = alldata['price']
        add.VAT = alldata['vat1']
        add.Excluding_VAT = alldata['ex-vat1'] 
        add.id_Promotion = 0
        add.status = 1
        add.save()
        return redirect('/product/')
    return render(request,'add_product.html',{"a":False})

def edit_Product(request , pk):
    title = 'Edit Product'
    item = Product.objects.get(id=pk)
    if request.method =='POST':
        alldata = request.POST
        add = Product.objects.get(id=pk)
        add.Barcode_ID = alldata['Barcode'] 
        add.Name = alldata['name']
        add.Size = alldata['inlineRadioOptions']
        add.Color = alldata['color']
        add.Type = alldata['type']
        add.Model = alldata['model']
        add.Cost = alldata['cost']
        add.Price = alldata['price']
        add.VAT = alldata['vat1']
        add.Excluding_VAT = alldata['ex-vat1'] 
        add.save()
        return redirect('product')
    return render(request,'edit_product.html',{'a':True,'item':item,'pk':pk})
# -----------------------------------------------------promotion-------------------------------------------------------------------------    
@login_required
def promotion(request):
    title = 'Promotion'
    data = Promotion.objects.all()
    timecurrent = datetime.today().strftime('%Y-%m-%d')
    print(timecurrent)
    change = 0
    for i in data:
        print(i.end_date,timecurrent)
        if str(i.end_date) <= str(timecurrent):
            print(i.id)
            history = History_promotion(name = i.name , types= i.types ,start_date= i.start_date ,
                        end_date=i.end_date ,
                        apply=i.apply,value = i.value , by= i.by
                        )
            history.save()
            his = History_promotion.objects.get(name=i.name)
            for j in List_product.objects.filter(id_promotion =i.id):
                product =  Product.objects.get(id = j.id_product)
                item = Item_in_promotion(id_history=his.id,Barcode_ID = product.Barcode_ID , Name= product.Name,Size= product.Size,Color= product.Color,
                        Type= product.Type,Model= product.Model,Cost= product.Cost,Price= product.Price,
                        VAT= product.VAT,Excluding_VAT= product.Excluding_VAT)
                item.save()
                j.delete()

            Promotion.objects.filter(id=i.id).delete()
            print('overtime promotion')
            change = 1
    if change == 1:
        data = Promotion.objects.all()
    return render(request,'promotion.html',{"title":title,"data":data})

@login_required
def promotion_view(request,pk):
    title = 'Promotion' 
    item = Promotion.objects.get(id=pk)
    # listpd = List_product.objects.filter(id_promotion=pk)
    # print(listpd)
    # item2 = list(item)
    # ------------------fetch item in table--------------------retern เเค่ของตัวเอง
    cursor = connection.cursor()
    cursor.execute('select * from myposapp_list_product join myposapp_product on myposapp_list_product.id_product = myposapp_product.id WHERE myposapp_list_product.id_promotion = '+pk+'')
    data = cursor.fetchall()
    print(data,'==============================================')
    # -----------------------------------------------------------
    print(item.start_date)
    if item.types == 'Percent off':
        return render(request,'promotion_discount.html',{"title":title,"item":item,"c":"1","data":data})
    elif item.types == 'Amount off':
        return render(request,'promotion_discount.html',{"title":title,"item":item,"c":"1","data":data})
    elif item.types == 'Buy X Get Y':
        cursor3 = connection.cursor()
        cursor2 = connection.cursor()
        cursor3.execute('select * from myposapp_list_product join myposapp_product on myposapp_list_product.id_product = myposapp_product.id WHERE myposapp_list_product.id_promotion = '+pk+' AND myposapp_list_product.Xory = "X" ')
        cursor2.execute('select * from myposapp_list_product join myposapp_product on myposapp_list_product.id_product = myposapp_product.id WHERE myposapp_list_product.id_promotion = '+pk+' AND myposapp_list_product.Xory = "y" ')
        data = cursor3.fetchall()
        data2 = cursor2.fetchall()
        return render(request,'promotion_buyXGetY.html',{"title":title,"item":item,"c":"1","data":data,"data2":data2})
    elif item.types == 'Combo Set':
        return render(request,'promotion_comboset.html',{"title":title,"item":item,"c":"1","data":data})
    elif item.types == 'At least':
        return render(request,'promotion_atlest.html',{"title":title,"item":item,"c":"1"})
    return redirect('/promotion')

@login_required
def delete_promotion(request,pk):
    item = Promotion.objects.get(id=pk)
    history = History_promotion(name = item.name , types= item.types ,start_date= item.start_date ,
                        end_date=item.end_date ,
                        apply=item.apply,value = item.value , by= item.by
                        )
    history.save()
    his = History_promotion.objects.get(name=item.name)
    for j in List_product.objects.filter(id_promotion = pk):
        product =  Product.objects.get(id = j.id_product)
        item1 = Item_in_promotion(id_history=his.id,Barcode_ID = product.Barcode_ID , Name= product.Name,Size= product.Size,Color= product.Color,
                Type= product.Type,Model= product.Model,Cost= product.Cost,Price= product.Price,
                VAT= product.VAT,Excluding_VAT= product.Excluding_VAT)
        item1.save()
        j.delete()

    print(item1.id)
    item.delete()
    return redirect('/promotion')

@login_required
def deleteitem_promotion(request,pk):
    checktype = localStorage.getItem('checktype')
    item = List_product.objects.get(id=pk)
    print(item.id)
    item.delete()
    if  checktype == 'discount':
        return redirect("/promotion/discount")
    if  checktype == 'Buy X Get Y':
        return redirect("/promotion/buyXGetY")
    else:
        return redirect("/promotion/comboset")

@login_required
def additem_promotion(request):                                     
    title = 'Promotion'
    if request.method == 'POST':
        checktype = localStorage.getItem('checktype')
        if request.POST['barcodeID']  is not None or request.POST['barcodeID'] != "" :
            try:
                
                Product.objects.get(Barcode_ID=request.POST['barcodeID'])

                if checktype == 'Buy X Get Y':
                    print('1')
                    try :
                        item = List_product.objects.filter(id_product = int(Product.objects.get(Barcode_ID=request.POST['barcodeID']).id), id_promotion = -1 , Xory=request.POST['xy'] )
                        print(item[0])
                        print('Promotion มีเเล้ว')
                        localStorage.setItem('error','product has been use.')
                        
                    except Exception as e:
                        print(e)
                        item = List_product(id_product=Product.objects.get(Barcode_ID=request.POST['barcodeID']).id,id_promotion = -1,Xory=request.POST['xy'] )
                        item.save()
                       
                    return redirect("/promotion/buyXGetY")
                    
                if checktype == 'discount':
                    print('3')
                    try :
                        item = List_product.objects.filter(id_product=Product.objects.get(Barcode_ID= int(request.POST['barcodeID'])).id, id_promotion = 0 , Xory='a'  )
                        print(Product.objects.get(Barcode_ID=request.POST['barcodeID']).id)
                        print(item[0])
                        print('Promotion มีเเล้วasdasdasdsad')
                        localStorage.setItem('error','product has been use.')
                    except Exception as e:
                        print(e)
                        item = List_product(id_product=Product.objects.get(Barcode_ID=request.POST['barcodeID']).id,id_promotion =0 , Xory='a'  )
                        item.save()
                        
                    return redirect("/promotion/discount")
                if checktype == 'Combo Set':
                    print('3')
                    try :
                        item = List_product.objects.filter(id_product=Product.objects.get(Barcode_ID=request.POST['barcodeID']).id,id_promotion =-2 , Xory='a' )
                        print(item[0])
                        print('Promotion มีเเล้ว')
                        localStorage.setItem('error','product has been use.') 

                    except Exception as e:
                        print(e)
                        item = List_product(id_product=Product.objects.get(Barcode_ID=request.POST['barcodeID']).id,id_promotion =-2 , Xory='a')
                        item.save()
                    return redirect("/promotion/comboset")
                        
            except Exception as e:
                print('44444')
                print(e)
                
                localStorage.setItem('error','Product not found.')
                if checktype == 'Buy X Get Y':
                    return redirect("/promotion/buyXGetY")
                if   checktype == 'discount':
                    return redirect("/promotion/discount")
                else :
                    return redirect("/promotion/comboset")
    
    print('22222222')
    return redirect("/promotion")
# --------------------------------0---------------โปรเดียวห้ามไอเทมซ้ำ
@login_required
def promotion_discount(request):
    title = 'Promotion'
    localStorage.setItem('checktype','discount')
    username = localStorage.getItem('username')
    # ------------------fetch item in table--------------------
    cursor = connection.cursor()
    cursor.execute('select * from myposapp_list_product join myposapp_product on myposapp_list_product.id_product = myposapp_product.id WHERE myposapp_list_product.id_promotion = 0')
    data = cursor.fetchall()
    # -----------------------------------------------------------
    if request.method == 'POST':
        alldata = request.POST
        if Promotion.objects.filter(name=alldata['promotion_name']).exists():
            print('Promotion มีเเล้ว')
            localStorage.setItem('name_error','name has been use.')
        else:
            item = Promotion(name = alldata['promotion_name'] , types=alldata["type"] ,start_date=alldata['startdate'] ,
                            end_date=alldata['enddate'] ,
                            apply=alldata['select'],value = alldata['discount_value'] , by=username
                            )
            item.save()
            promotion.id = Promotion.objects.get(name=alldata['promotion_name']).id
            product = Product.objects.all()
            List_product.objects.filter(id_promotion=0).update(id_promotion=promotion.id)
            for i in List_product.objects.filter(id_promotion=promotion.id):
                product = Product.objects.get(id=i.id_product)
                product.id_Promotion = promotion.id
                product.save()
            localStorage.setItem('checktype','')
            return redirect('/promotion')
    # data = Promotion.objects.all()
    error = localStorage.getItem('error')
    print(error)
    localStorage.setItem('error',"")
    name_error = localStorage.getItem('name_error')
    print(name_error)
    localStorage.setItem('name_error',"")
    return render(request,'promotion_discount.html',{"title":title,'data':data,'error':error,'name_error':name_error})
    # -------------------------------1------------------------
@login_required
def promotion_buyXGetY(request):
    title = 'Promotion'
    localStorage.setItem('checktype','Buy X Get Y')
    username = localStorage.getItem('username')
     # ------------------fetch item in table--------------------
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    cursor.execute('select * from myposapp_list_product join myposapp_product on myposapp_list_product.id_product = myposapp_product.id WHERE myposapp_list_product.id_promotion = -1 AND myposapp_list_product.Xory = "X" ')
    cursor2.execute('select * from myposapp_list_product join myposapp_product on myposapp_list_product.id_product = myposapp_product.id WHERE myposapp_list_product.id_promotion = -1 AND myposapp_list_product.Xory = "y" ')
    data = cursor.fetchall()
    data2 = cursor2.fetchall()
    # -----------------------------------------------------------
    if request.method == 'POST':
        alldata = request.POST
        if Promotion.objects.filter(name=alldata['promotion_name']).exists():
            print('Promotion มีเเล้ว')
            localStorage.setItem('name_error','name has been use.')
        else:
            item = Promotion(name = alldata['promotion_name'] , types='Buy X Get Y' ,start_date=alldata['startdate'] ,
                            end_date=alldata['enddate'] ,
                            value = 0,by=username
                            )
            item.save()
            promotion.id = Promotion.objects.get(name=alldata['promotion_name']).id
            product = Product.objects.all()
            List_product.objects.filter(id_promotion=-1).update(id_promotion=promotion.id)
            for i in List_product.objects.filter(id_promotion=promotion.id):
                product = Product.objects.get(id=i.id_product)
                product.id_Promotion = promotion.id
                product.save()
            localStorage.setItem('checktype','')
            return redirect('/promotion')

    error = localStorage.getItem('error')
    print(error)
    localStorage.setItem('error',"")
    name_error = localStorage.getItem('name_error')
    print(name_error)
    localStorage.setItem('name_error',"")
    return render(request,'promotion_buyXGetY.html',{"title":title,'data':data,'data2':data2,'error':error,'name_error':name_error})
# ---------------------------------------2------------------------
@login_required
def promotion_comboset(request):
    title = 'Promotion'
    localStorage.setItem('checktype','Combo Set')
    username = localStorage.getItem('username')
     # ------------------fetch item in table--------------------
    cursor = connection.cursor()
    cursor.execute('select * from myposapp_list_product join myposapp_product on myposapp_list_product.id_product = myposapp_product.id WHERE myposapp_list_product.id_promotion = -2')
    data = cursor.fetchall()
    # -----------------------------------------------------------
    if request.method == 'POST':
        alldata = request.POST
        if Promotion.objects.filter(name=alldata['promotion_name']).exists():
            print('Promotion มีเเล้ว')
            localStorage.setItem('name_error','name has been use.')
        else:
            item = Promotion(name = alldata['promotion_name'] , types='Combo Set',start_date=alldata['startdate'] ,
                            end_date=alldata['enddate'] ,
                            value = alldata['discount_value'] ,by=username
                            )
            item.save()
            promotion.id = Promotion.objects.get(name=alldata['promotion_name']).id
            product = Product.objects.all()
            List_product.objects.filter(id_promotion=-2).update(id_promotion=promotion.id)
            print(List_product.objects.filter(id_promotion=-2).update(id_promotion=promotion.id),'*************************')
            for i in List_product.objects.filter(id_promotion=promotion.id):
                product = Product.objects.get(id=i.id_product)
                product.id_Promotion = promotion.id
                product.save()
            localStorage.setItem('checktype','')
            return redirect('/promotion')

    error = localStorage.getItem('error')
    print(error)
    localStorage.setItem('error',"") 
    name_error = localStorage.getItem('name_error')
    print(name_error)
    localStorage.setItem('name_error',"")   
    return render(request,'promotion_comboset.html',{"title":title,'data':data,'error':error,'name_error':name_error})

@login_required
def promotion_atlest(request):
    title = 'Promotion'
    username = localStorage.getItem('username')
    if request.method == 'POST':
        alldata = request.POST
        if Promotion.objects.filter(name=alldata['promotion_name']).exists():
            print('Promotion มีเเล้ว')
            localStorage.setItem('name_error','name has been use.')
        else:
            item = Promotion(name = alldata['promotion_name'] , types=alldata["type"] ,start_date=alldata['startdate'] ,
                            end_date=alldata['enddate'] ,
                            atlest = alldata['atlest'] , value= alldata['discount_value'], by=username
                            )
            item.save()
            return redirect('/promotion')

    name_error = localStorage.getItem('name_error')
    print(name_error)
    localStorage.setItem('name_error',"")
    return render(request,'promotion_atlest.html',{"title":title,'name_error':name_error})



@login_required
def history_promotion(request):
    title = 'History Promotion'
    data = History_promotion.objects.all()
    return render(request,'history_promotion.html',{"title":title,'data':data})

@login_required
def history_view(request,pk):
    title = 'Promotion' 
    try:
        item = History_promotion.objects.get(id=pk)
        data = Item_in_promotion.objects.filter(id_history=pk)
        print(data[0].id)
        if item.types == 'Percent off':
            return render(request,'promotion_discount.html',{"title":title,"item":item,"data":data,"c":"1",})
        elif item.types == 'Amount off':
            return render(request,'promotion_discount.html',{"title":title,"item":item,"data":data,"c":"1"})
        elif item.types == 'Buy X Get Y':
            return render(request,'promotion_buyXGetY.html',{"title":title,"item":item,"data":data,"c":"1"})
        elif item.types == 'Combo Set':
            return render(request,'promotion_comboset.html',{"title":title,"item":item,"data":data,"c":"1"})
        elif item.types == 'At least':
            return render(request,'promotion_atlest.html',{"title":title,"item":item,"data":data,"c":"1"})
    except Exception as e:
        print(e)
        if item.types == 'Percent off':
            return render(request,'promotion_discount.html',{"title":title,"item":item,"c":"1"})
        elif item.types == 'Amount off':
            return render(request,'promotion_discount.html',{"title":title,"item":item,"c":"1"})
        elif item.types == 'Buy X Get Y':
            return render(request,'promotion_buyXGetY.html',{"title":title,"item":item,"c":"1"})
        elif item.types == 'Combo Set':
            return render(request,'promotion_comboset.html',{"title":title,"item":item,"c":"1"})
        elif item.types == 'At least':
            return render(request,'promotion_atlest.html',{"title":title,"item":item,"c":"1"})
# --------------------------------------------------------------------------------------------------------------------------
@login_required
def Membership_promotion_discount(request):
    if request.method == 'POST':
        alldata = request.POST
        online = 'online'
        try:
            if request.POST['type'] == 'Discount for member Persent  Off':
                if request.POST['atlest'] == ' ' :
                    item = Promotion_member(name = alldata['promotion_member_name'] , types=alldata['type'] ,start_date=alldata['startdate'] ,end_date=alldata['enddate'] ,atlest = alldata['atlest'],by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname  ,form=alldata['form'],to=alldata['to'],value= alldata['discount_value'],condition=['-'],status=online)
                    item.save()
                else:
                    item = Promotion_member(name = alldata['promotion_member_name'] , types=alldata['type'] ,start_date=alldata['startdate'] ,end_date=alldata['enddate'] ,atlest = 0 ,by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname  ,form=alldata['form'],to=alldata['to'],value= alldata['discount_value'],condition=['-'],status=online)
                    item.save()
            elif request.POST['type'] == 'Discount for member Amount  Off':
                if request.POST['atlest'] == ' ' :
                    item = Promotion_member(name = alldata['promotion_member_name'] , types=alldata['type'] ,start_date=alldata['startdate'] ,end_date=alldata['enddate'] ,atlest = alldata['atlest'],by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname ,form=alldata['form'],to=alldata['to'],value= alldata['discount_value2'],condition= ['-'],status=online)
                    item.save()
                elif request.POST['atlest'] == ' ' :
                    item = Promotion_member(name = alldata['promotion_member_name'] , types=alldata['type'] ,start_date=alldata['startdate'] ,end_date=alldata['enddate'] ,atlest = 0 ,by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname ,form=alldata['form'],to=alldata['to'],value= alldata['discount_value2'],condition= ['-'],status=online)
                    item.save()
        
            return redirect('/membership_promotion')
        except:
            return render(request,'fox.html')
    return render(request,'promotion_member_discount.html')


@login_required
def Membership_promotion_discount2(request):
    if request.method == 'POST':
        alldata = request.POST
        online = 'online'
        if request.POST['type'] == 'Brithday Special Persent  Off' :
             item = Promotion_member(name = alldata['promotion_member_name'] , types=alldata['type'] ,start_date=alldata['startdate'] ,end_date=alldata['enddate'] 
                ,atlest = alldata['atlest'] ,form=alldata['form'], by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname , to=alldata['to'],value= alldata['discount_value'],condition= alldata['con'],status=online)
             item.save()
            
        elif request.POST['type'] == 'Brithday Special Amount  Off' :
            item = Promotion_member(name = alldata['promotion_member_name'] , types=alldata['type'] ,start_date=alldata['startdate'] ,end_date=alldata['enddate'] 
                                        ,atlest = alldata['atlest2'] ,by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname , form=alldata['form'],to=alldata['to'],value= alldata['discount_value2'],condition= alldata['con'],status=online)
            item.save()
        return redirect('/membership_promotion')
    return render(request,'promotion_member_discount2.html')

@login_required
def Membership_promotion(request):
    if request.method == 'POST':
        alldata = request.POST
        online = 'online'
        jo = Subscription_fee.objects.all()
        new = jo[::-1]
        new1 = new[0]
        new1.status = 'expire'
        new1.save()
        if request.POST['start_date_rate'] == '' :
            item = Subscription_fee(start_date = None , end_date=None,old_rate=alldata['oldrate'] ,new_rate=alldata['newrate'] ,start_point = alldata['startpoint'] ,by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname ,status=online)
            item.save()
            
        else:
            item = Subscription_fee(start_date = alldata['start_date_rate'] , end_date=alldata['end_date_rate'] ,old_rate=alldata['oldrate'] ,new_rate=alldata['newrate'] ,start_point = alldata['startpoint'] ,by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname ,status=online)
            item.save()
        return redirect('/membership_promotion')
    fisrttime = 'fisttime'
    i = Promotion_member.objects.filter(status="online")
    his = Promotion_member.objects.all()
    point = Member_point.objects.all()
    rate = Subscription_fee.objects.all()
    today = datetime.now()
    day = today.strftime("%Y-%m-%d")
    min = today.strftime("%H:%M:%S")
    for j in his:
        if day >= str(j.end_date) :
                j.status = 'expire'
                j.save()
                
    for k in rate:
        if day >= str(k.end_date) :
                k.status = 'expire'
                k.save()
    try:
        new = point[::-1]
        new1 = new[0]
        g = rate[::-1]
        gg = g[0]
        if gg.status == 'expire' :
            gg = None
    except:
        item = Member_point(Pay_new = 9999 ,Is_new = 9999,Use_new = 9999,discout_new = 9999,Pay_old = 9999
                            ,Is_old = 9999,Use_old = 9999,discout_old = 9999,by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname ,status= fisrttime)
        item.save()

        item2 = Subscription_fee(start_date = day , end_date=day,old_rate=9999 ,new_rate=9999 ,start_point = 9999 ,by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname ,status=fisrttime)
        item2.save()
        return redirect('/membership_promotion')

    return render(request,'promotion_member.html',{'err':i,'point':new1,'rate':gg})

@login_required
def Membership_History_promotion(request):
    i = Promotion_member.objects.filter(status="expire")
    new = i[::-1]
    return render(request,'history_promotion_member.html',{'err':new})

@login_required
def Membership_History_promotion_point(request):
    i = Member_point.objects.all()
    new = i[::-1]
    
    return render(request,'history_promotion_membe_point.html',{'err':new})

@login_required
def Membership_History_promotion_rate(request):
    i = Subscription_fee.objects.all()
    new = i[::-1]
    
    return render(request,'history_promotion_membe_rate.html',{'err':new})


@login_required
def Membership_promotion_point_set(request):
    if request.method == 'POST':
        alldata = request.POST
        online = 'online'
        i = Member_point.objects.all()
        new = i[::-1]
        new1 = new[0]
        new1.status = 'expire'
        new1.save()
        print(alldata)
        item = Member_point(Pay_new = alldata['pay'],Is_new = alldata['is'],Use_new = alldata['use'],discout_new = alldata['discount'],Pay_old = alldata['Pay_old']
                            ,Is_old = alldata['Is_old'],Use_old = alldata['Use_old'],discout_old = alldata['discout_old'],by = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname ,status=online)
        item.save()
        return redirect('/membership_promotion')


    i = Member_point.objects.all()
    new = i[::-1]
    new1 = new[0]
    return render(request,'point_set.html',{'err':new1}) 

@login_required
def employee(request):
    title = 'Employee'
    data = Employee.objects.all()
    return render(request,'employee.html',{"title":title,'data':data})

@login_required
def AddEmployee(request):
    title = 'Employee'
    return render(request,'Add_employee.html',{"title":title})

@login_required
def edit_employee(request,pk):
    title = 'Edit Employee'
    data = Employee.objects.get(id=pk)
    if request.method == 'POST':
        alldata = request.POST
        datauser = User.objects.get(id=data.id_user)
        
        add = Employee.objects.get(id=pk)
       
        add.IDcard = alldata['IDcard']
        add.Title_Name = alldata['Title_Name']
        add.Firstname = alldata['Firstname']
        add.Lastname=alldata['Lastname']
        add.Age=alldata['Age']
        add.Gender=alldata['Gender']
        add.Email=alldata['email']
        add.Phonenumber=alldata['Phonenumber']
        add.Blood_Type=alldata['bloodtype']
        add.Birthday=alldata['Birthday']
        add.Ethnicity=alldata['Ethnicity']
        add.Nationality=alldata['Nationality']
        add.Religion=alldata['Religion']
        add.Address=alldata['Address']
        add.Maritial_Status=alldata['Maritial_Status']
        add.Education_Level=alldata['Education_Level']
        add.Emergency_Tel=alldata['Emergency_Tel']
        add.Relationship=alldata['Relationship']
        add.Father_Name=alldata['FatherFirstname']
        add.Father_Lastname=alldata['FatherLastname']
        add.Father_Career=alldata['FatherCareer']
        add.Father_Tel=alldata['FatherPhonenumber']
        add.Father_Ethnicty=alldata['FatherEthnicity']
        add.Father_Nationallity=alldata['FatherNationality']
        add.Father_Religion=alldata['FatherReligion']
        add.Father_Address=alldata['FatherAddress']
        add.Mother_Title=alldata['Mother_Title']
        add.Mother_Name=alldata['MotherFirstname']
        add.Mother_Lastname=alldata['MotherLastname']
        add.Mother_Career=alldata.get('MotherCareer')
        add.Mother_Tel=alldata['MotherPhonenumber']
        add.Mother_Ethnicty=alldata['MotherEthnicity']
        add.Mother_Nationallity=alldata['MotherNationality']
        add.Mother_Religion=alldata['MotherReligion']
        add.Mother_Address=alldata['MotherAddress']
        add.save()
        return redirect('/employee')
    return render(request,'Edit_employee.html',{'data':data,'pk':pk})

@login_required
def Search_Employee(request):
    title = 'Employee'
    alldata = Employee.objects.all()
    data = []
    SearchBar = request.GET.get("Searchbar")
    for i in alldata:
        if str(i.id) == str(SearchBar):
            data.append(i)
    return render(request,'employee.html',{"title":title, "data":data})

@login_required
def del_employee(request,pk):
    item = Employee.objects.get(id=pk)
    item.status = 0
    item.save()
    return redirect('/employee/')


@login_required
def Membership(request):
    title = 'Member'
    data = Member.objects.all()
    return render(request,'Member.html',{"title":title,"data":data})

@login_required
def Search_Membership(request):
    title = 'Member'
    alldata = Member.objects.all()
    data = []
    search = request.GET.get("search")
    for i in alldata:
        if str(i.Phonenumber) == str(search):
            data.append(i)
    return render(request,'Member.html',{"title":title, "data":data})
@login_required
def del_Membership(request,pk):
    item = Member.objects.get(Member_ID=pk)
    item.status = 0
    item.save()
    return redirect('/membership/')

@login_required
def add_Membership(request):
    print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    title = 'Add Membership'
    if request.method == 'POST':
        alldata = request.POST
        if Member.objects.filter(Phonenumber=alldata["Phonenumber"]).exists():
            print('เบอร์มีคนใช้เเล้ว')
            return render(request,'AddMember1.html')
        else:
            add = Member()
            try :
                last_mem = Member.objects.all().last()
                last  = last_mem.Member_ID
                last += 1 

            except :
                last = 1

            add.Member_ID = last
            add.IDcard= request.POST['IDcard']
            add.Title_Name= request.POST['title_name']
            add.Firstname=request.POST['name']
            add.Lastname=request.POST['Lastname']
            add.Gender=request.POST['Gender']
            add.Age=request.POST['Age']
            add.Email=request.POST['Email']
            add.Phonenumber=request.POST['Phonenumber']
            add.Birthday=request.POST['Birthday']
            add.Address=request.POST['Address']
            add.Point= 0
            add.status = 1

            add.save()
        return redirect('/membership')
    return render(request,'AddMember1.html')

@login_required
def edit_Membership(request,pk):
    title = 'Edit Membership'
    data = Member.objects.get(Member_ID=pk)
    if request.method == 'POST':
        alldata = request.POST
      
        add = Member.objects.get(Member_ID=pk)
        add.IDcard= alldata['IDcard']
        add.Title_Name= alldata['title_name']
        add.Firstname=alldata['name']
        add.Lastname=alldata['Lastname']
        add.Gender=alldata['Gender']
        add.Age=alldata['Age']
        add.Email=alldata['Email']
        add.Phonenumber=alldata['Phonenumber']
        add.Birthday=alldata['Birthday']
        add.Address=alldata['Address']
        add.save()
        return redirect('/membership')
    return render(request,'Edit_member.html',{'data':data,'pk':pk})

@login_required
def Sales_report(request):
    username = localStorage.getItem('username')
    userlogin = User.objects.get(username=username)
    em = Employee.objects.get(id_user=userlogin.id)
################## ฟังก์ชันดึง วัน เดือน ปี ปัจจุบัน ###########################################
    today=date.today()

################## วนลูปคำนวณค่าบิลทั้งหมด ยอดขายทั้งหมด ยอดกำไรทั้งหมด #################
    bill =Bill.objects.all()
    total_bill=0
    total_quantity=0
    total_profit=0
    total_price=0
    count=0
    years_now=today.strftime("%Y")
    for l in bill :
        years=l.Date.strftime("%Y")
        if  years==years_now: 
            total_bill+=1
            total_quantity+=l.Quantity
            total_profit+=l.Profit
    group=[total_bill,total_quantity,total_profit]

################## คำสั่งหาสินค้าที่ขายดี #######################################
    cursor = connection.cursor()
    q= "SELECT Product_id, SUM( Quantity )FROM myposapp_product_order WHERE ( Date  BETWEEN '2021-01-01' and '2021-12-31') GROUP BY Product_id ORDER BY SUM( Quantity ) DESC LIMIT 5 "
    cursor.execute(q)
    results = cursor.fetchall()
################## เพิ่มสินค้าที่ขายดี ##########################################
    count=0
    top=[]
    value_top=[]
    for i in results:
        
        top.append(i[0])
        value_top.append(i[1])

    datatop=[]
    for j in range(5):
        d = Product.objects.get( id =top[j]).Name
        datatop.append(d)

 ###################### วนloop เอาค่า0ยัดลงdatabase #####################################   
    
    sale= Sale.objects.all()
    for k in sale:
        g = Sale.objects.get(id=k.id)
        g.January = 0
        g.February = 0
        g.March = 0
        g.April = 0
        g.May = 0
        g.June = 0
        g.July = 0
        g.August = 0
        g.September = 0
        g.October = 0
        g.November = 0
        g.December = 0
        g.save()

######################### วนloop เอาค่ากำไรยัดลงdatabase #################################   
     
    for i in bill:
            
        sale=Sale.objects.get(id=i.id)
            
        if str(i.Date)[0:3]==str(today)[0:3]:
                

            if str(i.Date)[5:7]=="01":
                    
               sale.January += i.Quantity  
                    
            elif str(i.Date)[5:7]=="02":
                
                sale.February += i.Quantity 
                    
            elif str(i.Date)[5:7]=="03":
                    
                sale.March  += i.Quantity  
                            
            elif str(i.Date)[5:7]=="04":
                
                sale.April +=i.Quantity 
                    
            elif str(i.Date)[5:7]=="05":
                    
                sale.May += i.Quantity 
                
            elif str(i.Date)[5:7]=="06":
                    
                sale.June += i.Quantity 
                
            elif str(i.Date)[5:7]=="07":
        
                sale.July += i.Quantity 
                    
            elif str(i.Date)[5:7]=="08":

                sale.August += i.Quantity 
                
            elif str(i.Date)[5:7]=="09":
                    
                sale.September += i.Quantity 
                    
            elif str(i.Date)[5:7]=="10":
                
                sale.October += i.Quantity 
                    
            elif str(i.Date)[5:7]=="11":
                      
                sale.November += i.Quantity 
                    
            elif str(i.Date)[5:7]=="12":

                sale.December += i.Quantity 
        sale.save()            

######################### คำนวณค่ากำไรเเต่ละเดือน ##################################
  
    Jan_s = 0
    Feb_s = 0
    Mar_s = 0
    Apr_s = 0
    May_s = 0
    Jun_s= 0
    Jul_s = 0
    Aug_s = 0
    Sep_s = 0
    Oct_s = 0
    Nov_s = 0
    Dec_s = 0 
    sale= Sale.objects.all()
    
    for i in sale:
        Jan_s +=i.January
        Feb_s += i.February
        Mar_s +=  i.March
        Apr_s +=  i.April
        May_s +=  i.May
        Jun_s +=  i.June
        Jul_s +=  i.July
        Aug_s +=  i.August
        Sep_s +=  i.September
        Oct_s +=  i.October
        Nov_s +=  i.November
        Dec_s +=  i.December
######################## เพิ่มค่ากำไรเเต่ละเดือน ######################################
    
    data1=[]
    data1.append(Jan_s)
    data1.append(Feb_s)
    data1.append(Mar_s)
    data1.append(Apr_s)
    data1.append(May_s)
    data1.append(Jun_s)
    data1.append(Jul_s)
    data1.append(Aug_s)
    data1.append(Sep_s)
    data1.append(Oct_s)
    data1.append(Nov_s)
    data1.append(Dec_s)


#profitttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt


    profit= Profit.objects.all()
    for k in profit:
        g = Profit.objects.get(id=k.id)
        g.January = 0
        g.February = 0
        g.March = 0
        g.April = 0
        g.May = 0
        g.June = 0
        g.July = 0
        g.August = 0
        g.September = 0
        g.October = 0
        g.November = 0
        g.December = 0
        g.save()

######################## วนloop เอาค่ากำไรยัดลงdatabase ###########################   
    
    for i in bill:
            
        profit=Profit.objects.get(id=i.id)
            
        if str(i.Date)[0:3]==str(today)[0:3]:
                

            if str(i.Date)[5:7]=="01":
                    
               profit.January += i.Profit 
                    
            elif str(i.Date)[5:7]=="02":
                
                profit.February += i.Profit 
                    
            elif str(i.Date)[5:7]=="03":
                    
                profit.March  += i.Profit 
                            
            elif str(i.Date)[5:7]=="04":
                
                profit.April +=i.Profit 
                    
            elif str(i.Date)[5:7]=="05":
                profit.May+=i.Profit 
                
            elif str(i.Date)[5:7]=="06":
                    
                profit.June += i.Profit 
                
            elif str(i.Date)[5:7]=="07":
        
                profit.July += i.Profit 
                    
            elif str(i.Date)[5:7]=="08":

                profit.August += i.Profit 
                
            elif str(i.Date)[5:7]=="09":
                    
                profit.September += i.Profit 
                    
            elif str(i.Date)[5:7]=="10":
                
               profit.October += i.Profit 
                    
            elif str(i.Date)[5:7]=="11":
                      
                profit.November += i.Profit 
                    
            elif str(i.Date)[5:7]=="12":

                profit.December += i.Profit 
        profit.save()            
######################## คำนวณค่ากำไรเเต่ละเดือน ####################################
    Jan_p = 0
    Feb_p = 0
    Mar_p = 0
    Apr_p = 0
    May_p = 0
    Jun_p= 0
    Jul_p = 0
    Aug_p = 0
    Sep_p = 0
    Oct_p = 0
    Nov_p = 0
    Dec_p = 0 
    profit= Profit.objects.all()

    for i in profit:
        Jan_p +=i.January
        Feb_p += i.February
        Mar_p +=  i.March
        Apr_p +=  i.April
        May_p +=  i.May
        Jun_p +=  i.June
        Jul_p +=  i.July
        Aug_p +=  i.August
        Sep_p +=  i.September
        Oct_p +=  i.October
        Nov_p +=  i.November
        Dec_p +=  i.December

######################## เพิ่มค่ากำไรเเต่ละเดือน #######################################
    data2=[]
    data2.append(Jan_p)
    data2.append(Feb_p)
    data2.append(Mar_p)
    data2.append(Apr_p)
    data2.append(May_p)
    data2.append(Jun_p)
    data2.append(Jul_p)
    data2.append(Aug_p)
    data2.append(Sep_p)
    data2.append(Oct_p)
    data2.append(Nov_p)
    data2.append(Dec_p)
    if em.Role == "Admin" : 
######################## ส่งค่าออกไปที่เว็บ ############################################     
        return render(request,'sale_report.html',{'total_bill':total_bill,'total_quantity':total_quantity,'total_profit':total_profit,'group':group,'datapy1':data1,'datapy2':data2,'datatop':datatop,'value_top':value_top })
    elif em.Role == "Finance" :
        return render(request,'finance_sale_report.html',{'total_bill':total_bill,'total_quantity':total_quantity,'total_profit':total_profit,'group':group,'datapy1':data1,'datapy2':data2,'datatop':datatop,'value_top':value_top })

@login_required
def Bill_info(request,pk):
    item = Bill.objects.get(id=pk)
    new_id = str(pk)
    cursor = connection.cursor()
    cursor.execute('select product.id,product.Barcode_ID,product.Name,product.Size,product.Color,product.Price,product_order.Quantity,product_order.Bill_id,product.Cost,product_order.id from myposapp_product AS product join myposapp_product_order AS product_order on product.id = product_order.product_id WHERE product_order.Bill_id =' + new_id )
    results = cursor.fetchall()
    change = item.Receive - item.Total
    sub = item.Total + item.Discount
    return render(request,'Bill_info.html',{'results':results , 'item':item , "change":change , "sub":sub})

@login_required
def C_Bill_info(request,pk):
    item = Bill.objects.get(id=pk)
    new_id = str(pk)
    cursor = connection.cursor()
    cursor.execute('select product.id,product.Barcode_ID,product.Name,product.Size,product.Color,product.Price,product_order.Quantity,product_order.Bill_id,product.Cost,product_order.id from myposapp_product AS product join myposapp_product_order AS product_order on product.id = product_order.product_id WHERE product_order.Bill_id =' + new_id )
    results = cursor.fetchall()
    change = item.Receive - item.Total
    sub = item.Total + item.Discount
    return render(request,'Bill-info.html',{'results':results , 'item':item , "change":change , "sub":sub})


@login_required
def Daily_report(request):
    all = Bill.objects.all()
    mosprofit =Bill.objects.values_list('Profit')
    mosdiscount =Bill.objects.values_list('Discount')
    mostex =Bill.objects.values_list('Tax')
    mostotal = Bill.objects.values_list('Total')
    sumprofit = 0
    sumdiscount = 0
    sumtex = 0
    sumtotal = 0
    for i in mosprofit:
        print(i[0])
        i = str(i[0])
        sumprofit += int(i)
        print('sumprofit')
        print(sumprofit)
    for j in mosdiscount:
        print(j[0])
        j = str(j[0])
        sumdiscount += int(j)
        print('sumdiscount')
        print(sumdiscount)
    for k in mostex:
        print(k[0])
        k = str(k[0])
        sumtex += int(k)
        print('sumtex')
        print(sumtex)
    for l in mostotal:
        print(l[0])
        l = str(l[0])
        sumtotal += int(l)
        print('sumtex')
        print(sumtotal)
    Total_Net_Sales = (sumprofit-sumdiscount)-sumtex
    Transactions = len(all)
    Net_Sales = sumtotal - sumdiscount
    
    username = localStorage.getItem('username')
    userlogin = User.objects.get(username=username)
    em = Employee.objects.get(id_user=userlogin.id)
    if em.Role == "Admin" : 
        return render(request,'DailyReport.html',{'Total_Net_Sales':Total_Net_Sales,'Discount':sumdiscount,'Tax':sumtex,'Profits':sumprofit,'Transactions':Transactions,'Gross_Sales':sumtotal,'Net_Sales':Net_Sales})
    elif em.Role == "finance" :
        return render(request,'finance_Daily_report.html',{'Total_Net_Sales':Total_Net_Sales,'Discount':sumdiscount,'Tax':sumtex,'Profits':sumprofit,'Transactions':Transactions,'Gross_Sales':sumtotal,'Net_Sales':Net_Sales})
    else :
        return render(request,'finance_Daily_report.html',{'Total_Net_Sales':Total_Net_Sales,'Discount':sumdiscount,'Tax':sumtex,'Profits':sumprofit,'Transactions':Transactions,'Gross_Sales':sumtotal,'Net_Sales':Net_Sales})

@login_required
def Sales_history(request):
    title = 'Sale History'
    data = Bill.objects.all()
    username = localStorage.getItem('username')
    userlogin = User.objects.get(username=username)
    em = Employee.objects.get(id_user=userlogin.id)
    if em.Role == "Admin" : 
        return render(request,'Sale_history.html',{"title":title,"data":data}) 
    elif em.Role == "finance" :
        return render(request,'finance_sale_history.html',{"title":title,"data":data}) 
    else :
        return render(request,'finance_Sale_history.html',{"title":title,"data":data}) 
    
@login_required
def C_Sales_history(request):
    title = 'Sale History'
    data = Bill.objects.all()
    return render(request,'sale-history.html',{"title":title,"data":data})     
      

@login_required
def Check_history_Date(request):
    title = 'Sale History'
    alldata = Bill.objects.all()
    data = []
    ID = request.GET.get("ID")
    date_Start = request.GET.get("date_start")
    date_Stop = request.GET.get("date_stop")
    for i in alldata:
        if str(i.Date) >= date_Start and str(i.Date)<=date_Stop:
            data.append(i)
    return render(request,'Sale_history.html',{"title":title, "data":data})   

def Check_history_ID(request):
    title = 'Sale History'
    alldata = Bill.objects.all()
    data = []
    ID = request.GET.get("ID")
    print(ID)
    for i in alldata:
        print(i.id)
        if str(i.id) == str(ID):
            data.append(i)
    return render(request,'Sale_history.html',{"title":title, "data":data})
@login_required
def Document(request):
    title = 'Document'
    data = Bill.objects.all()
    
    username = localStorage.getItem('username')
    userlogin = User.objects.get(username=username)
    em = Employee.objects.get(id_user=userlogin.id)
    if em.Role == "Admin" : 
        return render(request,'Document.html',{"title":title,"data":data}) 
    elif em.Role == "finance" :
        return render(request,'finance_Doc.html',{"title":title,"data":data}) 
    else :
        return render(request,'finance_Doc.html',{"title":title,"data":data}) 
    
@login_required
def Document_Date(request):
    title = 'Document'
    alldata = Bill.objects.all()
    data = []
    date_Start = request.GET.get("date_start")
    date_Stop = request.GET.get("date_stop")
    for i in alldata:
        if str(i.Date) >= date_Start and str(i.Date)<=date_Stop:
            data.append(i)
    return render(request,'Document.html',{"title":title, "data":data})

@login_required
def finance_mode(request):
    
    return render(request,'layout_finance.html')



@login_required
def Cashier_mode(request):
    username = localStorage.getItem('username')
    userlogin = User.objects.get(username=username)
    em = Employee.objects.get(id_user=userlogin.id)
    order_bill = Product_order.objects.all()
    cursor = connection.cursor()
    cursor.execute('select product.id,product.Barcode_ID,product.Name,product.Size,product.Color,product.Price,product_order.Quantity,product_order.Bill_id,product.Cost,product_order.id from myposapp_product AS product join myposapp_product_order AS product_order on product.id = product_order.product_id WHERE product_order.Bill_id = 0')
    results = cursor.fetchall()
    
    if request.GET.get('phonemember')  is None or request.GET.get('phonemember') == "" :
        if em.Role == 'Admin':
            member = ""
            mem = ""
            print("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff" )
            if request.GET.get('barcodeID') :
                barcode = request.GET.get('barcodeID')
                cus = localStorage.getItem('customer')
                try :
                    cus = int(cus)
                    mem = Member.objects.get(Member_ID= cus)
                except : 
                    mem = {'Firstname' : "-" , 'Lastname' : "-" , "Point" : 0}
                print('Cusssssssssssssssssssssstoooooooooooooooooooooooomerrrrrrrrrrrrrrrrrrrrrrrrrrrrrr' , cus)
                try :
                    product = Product_order.objects.get(Product_id=Product.objects.get(Barcode_ID=barcode).id,Bill_id = 0)
                    qty = int(request.GET['input_price'])
                    product.Quantity += qty
                    product.save()
                except :
                    today = datetime.today()
                    product_or =  Product_order()
                    product_or.Product_id = Product.objects.get(Barcode_ID=barcode).id
                    product_or.Date = today
                    product_or.Bill_id = 0
                    product_or.Employee_id = Employee.objects.get(Firstname=localStorage.getItem('username')).id_user
                    product_or.Quantity = int(request.GET.get('input_price'))
                    product_or.Unit_price = Product.objects.get(Barcode_ID=barcode).Price
                    product_or.Unit_Cost = Product.objects.get(Barcode_ID=barcode).Cost
                    product_or.Unit_Tax = Product.objects.get(Barcode_ID=barcode).VAT
                    product_or.save()
                return redirect('/cashier')   

            
            discount = 0
            if request.GET.get("input_point") :
                print(request.GET.get("input_point"))
                input = request.GET.get("input_point")
                d = Member_point.objects.get(status = 'online') 
                print(d)
                use = d.Use_new
                dis = d.discout_new
                discount = (input%use)*dis
            
            count = 0
            total_price = 0
            profit = 0
            tax = 0
            for i in order_bill :
                if i.Bill_id == 0 :
                    count = count + i.Quantity  
                    price = ((i.Unit_price)*(i.Quantity))-discount
                    t = (i.Unit_Tax)*(i.Quantity)
                    p = price-((i.Unit_Cost)*(i.Quantity))
                    total_price = total_price + price   
                    tax = tax + t
                    profit = profit + p
            
            
            
            return render(request,'cashier_admin.html',{"discount": discount , "mem":mem ,'member':member ,"order_bill":order_bill, "count": count ,"total_price":total_price , "results":results , "username":username,"profit":profit , "tax":tax })
        if em.Role == 'Cashier':
            return render(request,'cashier.html')
    else :
        phone = request.GET.get('phonemember')
        try :
            member = Member.objects.get(Phonenumber=phone).Member_ID
            member2 = Member.objects.get(Phonenumber=phone)
            member1 = str(member)
            print(member)
            print(member2)
            localStorage.setItem('customer',member1)
            cus = localStorage.getItem('customer')
            cus = int(cus)
            print('Cusssssssssssssssssssssstoooooooooooooooooooooooomerrrrrrrrrrrrrrrrrrrrrrrrrrrrrr' , cus)
            mem = ""
            if request.GET.get('barcodeID') :
                barcode = request.GET.get('barcodeID')
                cus = localStorage.getItem('customer')
                try :
                    cus = int(cus)
                    mem = Member.objects.get(Member_ID= cus)
                except : 
                    mem = {'Firstname' : "-" , 'Lastname' : "-" , "Point" : 0}
                
                try :
                    product = Product_order.objects.get(Product_id=Product.objects.get(Barcode_ID=barcode).id,Bill_id = 0)
                    qty = int(request.GET['input_price'])
                    product.Quantity += qty
                    product.save()
                except :
                    today = datetime.today()
                    product_or =  Product_order()
                    product_or.Product_id = Product.objects.get(Barcode_ID=barcode).id
                    product_or.Date = today
                    product_or.Bill_id = 0
                    product_or.Employee_id = Employee.objects.get(Firstname=localStorage.getItem('username')).id_user
                    product_or.Quantity = int(request.GET.get('input_price'))
                    product_or.Unit_price = Product.objects.get(Barcode_ID=barcode).Price
                    product_or.Unit_Cost = Product.objects.get(Barcode_ID=barcode).Cost
                    product_or.Unit_Tax = Product.objects.get(Barcode_ID=barcode).VAT
                    product_or.save()
                return redirect('/cashier') 
            
            discount = 0
            if request.GET.get("input_point") :
                print(request.GET.get("input_point"))
                input = request.GET.get("input_point")
                d = Member_point.objects.get(status = 'online') 
                print(d)
                use = d.Use_new
                dis = d.discout_new
                discount = (input%use)*dis
            
            count = 0
            total_price = 0
            profit = 0
            tax = 0
            for i in order_bill :
                    if i.Bill_id == 0 :
                        count = count + i.Quantity  
                        price = ( (i.Unit_price)*(i.Quantity) )-discount
                        t = (i.Unit_Tax)*(i.Quantity)
                        p = price-((i.Unit_Cost)*(i.Quantity))
                        total_price = total_price + price   
                        tax = tax + t
                        profit = profit + p
            return render(request,'cashier_admin.html',{ "discount":discount , 'member': member ,'member2': member2 ,"order_bill":order_bill,"count": count  ,"total_price":total_price ,"results":results,"username":username ,"profit":profit ,"tax":tax })
        except :
            member = ""
            return render(request,'cashier_admin.html')  
    return redirect('/login')

@login_required
def Tax_report(request):
    data = Bill.objects.all()
    i = 1
    va = 0
    to = 0
    for i in data :
        to += i.Total
        va += i.Tax
    return render(request,'Tax_report.html',{"data":data,"count":i,"to":to,"va":va})

@login_required
def Create_Bill(request):
    order_bill = Product_order.objects.all()
    
    last_bill = Product_order.objects.latest('Bill_id')
    print(last_bill.Bill_id)
    
    count = 0
    total_price = 0
    profit = 0
    tax = 0
    for i in order_bill :
        if i.Bill_id == 0 :
            count = count + 1    
            price = (i.Unit_price)*(i.Quantity)
            t = (i.Unit_Tax)*(i.Quantity)
            p = price-((i.Unit_Cost)*(i.Quantity))
            total_price = total_price + price   
            tax = tax + t
            profit = profit + p
            i.Bill_id = (last_bill.Bill_id)+1
            i.save()
    
    today = datetime.today()
    now = datetime.now()
    bill = Bill()
    bill.Date = today
    bill.Time = now 
    cus = localStorage.getItem('customer')  
    try :
        cus = int(cus)
        bill.Member_id = cus
    except : 
        bill.Member_id = 0
    bill.Total = total_price
    bill.Quantity = count
    bill.Employee_name = Employee.objects.get(Firstname=localStorage.getItem('username')).Firstname
    bill.Employee_role = Employee.objects.get(Firstname=localStorage.getItem('username')).Role
    bill.Discount = 0
    bill.Receive = request.GET.get('amount_input')
    bill.Tax = tax
    bill.Profit = profit
    bill.save()
    
    sale=Sale()
    sale.January =0
    sale.February = 0
    sale.March = 0
    sale.April = 0
    sale.May = 0
    sale.June = 0
    sale.July = 0
    sale.August= 0
    sale.September = 0
    sale.October = 0
    sale.November = 0
    sale.December = 0
    sale.save()
    
    profit=Profit()
    profit.January =0
    profit.February = 0
    profit.March = 0
    profit.April = 0
    profit.May = 0
    profit.June = 0
    profit.July = 0
    profit.August = 0
    profit.September = 0
    profit.October = 0
    profit.November = 0
    profit.December = 0
    profit.save()
    
    
    try :
        localStorage.removeItem('customer');
    except : 
        print("Noooooooooooooooooooooooooooooooo")
    return redirect('/cashier/success/')

@login_required
def Cashier_success(request):
    last_bill = Bill.objects.latest('id')
    print(last_bill)
    last = str(last_bill.id)
    cursor = connection.cursor()
    cursor.execute('select product.id,product.Barcode_ID,product.Name,product.Size,product.Color,product.Price,product_order.Quantity,product_order.Bill_id,product.Cost,product_order.id from myposapp_product AS product join myposapp_product_order AS product_order on product.id = product_order.product_id WHERE product_order.Bill_id = "'+last+'"')
    results = cursor.fetchall()
    bill = Bill.objects.get(id=last_bill.id)
    
    try : 
        mem = Member.objects.get(Member_ID= bill.Member_id)
    except :
        mem = {'Firstname' : "-" , 'Lastname' : "-" , "Point" : 0}
    
    print(mem)
    print(bill)
    
    change = bill.Receive - bill.Total
    return render(request,'cashier_success.html',{"results":results , "last":last , "bill":bill , "change":change , "mem":mem})

@login_required
def delete_product_bill(request,pk):
    item = Product_order.objects.get(id=int(pk))
    item.delete()
    return redirect('/cashier')

@login_required
def Logout(request):
    auth.logout(request)
    localStorage.clear()
    print('logout eiei')
    return redirect('/') 