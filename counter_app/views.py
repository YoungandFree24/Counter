from django.shortcuts import render,redirect



def some_function(request):
    print("%%%%%%%%%%%%%%%%%%%%%%%")
    # use brackets for session on backend
    request.session["visit"] = "visitor"
    if "tommy" not in request.session:
        request.session["tommy"] = 0
    return render(request, 'homepage.html')

def process_form(request):
    request.session["tommy"] += 1
    print(request.session["tommy"])
    return redirect('/')

def destroy_session(request):
    del request.session["tommy"]
    return redirect('/')