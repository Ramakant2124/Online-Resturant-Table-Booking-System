from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items
# Create your views here.

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html',{'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')

        if name != '' and phone_number and email != '' and total_person != '' and booking_data != '':
            data = BookTable(
                Name=name,
                Phone_number=phone_number,
                Email=email,
                Total_person=total_person,
                Booking_date=booking_data
            )
            data.save()
            return render(request, 'book_table.html', {'success': True})

    return render(request, 'book_table.html')




def FeedbackView(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        rating = request.POST.get('rating', '')
        image = request.FILES.get('image', None)

        if name and description and rating:
            Feedback.objects.create(
                User_name=name,
                Description=description,
                Rating=rating,
                Image=image
            )
            return render(request, 'feedback.html', {'success': True})

    return render(request, 'feedback.html', {'success': True})



