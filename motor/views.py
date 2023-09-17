from django.shortcuts import render

# Create your views here.
def vehicleprice(priceofvehicle):
    if priceofvehicle == 'car':
        return 500
    elif priceofvehicle == 'bike':
        return 250
    else:
        return 0
    
def vehiclemodel(modelofvehicle):
    if modelofvehicle == 'car':
        return 2023
    elif modelofvehicle =='bike':
        return 2022
    else:
        return 0
    
def car(request):
    carprice=vehicleprice('car')
    carmodel=vehiclemodel('car')
    return render(request,'car.html',{'price1':carprice, 'model1':carmodel})


  
def bike(request):
    bikeprice=vehicleprice('bike')
    bikemodel=vehiclemodel('bike')
    return render(request,'bike.html',{'price2':bikeprice, 'model2':bikemodel})
        