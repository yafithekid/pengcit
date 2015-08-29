from django.shortcuts import render
from pengcit.rgb.services import RGBCounter
from pengcit.settings import PENGCIT_UPLOAD_DIR


def test(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'])
        rgbcounter = RGBCounter()
        # rgbcounter.set_image_from_path("C:\\users\\yafi\\Downloads\\lena.jpg")
        rgbcounter.set_image_from_path(PENGCIT_UPLOAD_DIR + "/gambar.jpg")
        rgbcounter.get_most_frequent_rgb()
        return render(request, "rgb/test.html",
                      {"show_image": True, "count": rgbcounter.count_rgb(),
                       "most_freq": rgbcounter.get_most_frequent_rgb()})
    else:
        return render(request, "rgb/test.html", {"show_image": False})


def handle_uploaded_file(f):
    with open(PENGCIT_UPLOAD_DIR + "/gambar.jpg", "wb+") as dest:
        for chunk in f.chunks():
            dest.write(chunk)
