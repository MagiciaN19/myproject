from django.shortcuts import render
from .models import Visit

def index(request):
    # Pobierz obiekt licznika lub stwórz, jeśli nie istnieje (ID=1)
    visit_obj, created = Visit.objects.get_or_create(id=1)
    
    # Zwiększ licznik w bazie danych
    visit_obj.count += 1
    visit_obj.save()
    
    # Przekaż do szablonu
    return render(request, 'visitcounter/index.html', {'visit_count': visit_obj.count})