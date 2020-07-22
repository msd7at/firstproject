from django.shortcuts import render
from django.http import HttpResponse

def showtest(request):
    que="who developed c lang"
    a="ken thompson"
    b="james bond"
    c="narendra modi"
    d="kri ho kisi ne hme kya"
    l="ye level hai"
    data={'que':que,"a":a,"b":b,"c":c,"d":d,"l":l}
    res=render(request,'exam/test.html',context=data)
    return res
def showresult(request):
    s="<h1>राम श्याम और घनश्याम तीनो हो गये फ़ैल अत्यंत दुखद खबर </h1>"
    return HttpResponse(s)
