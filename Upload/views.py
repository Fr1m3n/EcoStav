from django.shortcuts import render, redirect
from .forms import UploadForm
import os
from Ecopolice.settings import neuro_path, media_path
from Upload.models import Image
from PIL import Image as pil_img


def upload(request):
    # Форма загрузки изображения
    # test = request.method
    title = 'Upload Image'
    if request.method == 'POST':
        # подгружаем форму модели
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # сохраняем поле
            form.save()
            # перенаправление на страницу обработки
            return redirect('/upload/result/' + str(request.FILES['image']))
    else:
        form = UploadForm()
    return render(request, 'uploadImage/upload.html', locals())


def result(request):
    title = 'Result'
    # имя изображения из URL  (пример: http://localhost:8000/upload/result/IMG_7071.JPG -> IMG_7071.JPG
    image_name = str(request.path).split('/')[3]
    # полный путь до фото
    full_path = media_path + '\\data\\' + image_name
    # вызов нейросети для обработки изображения
    os.system('python ' + neuro_path + '\\classify_image.py --image_file ' + full_path)
    # открыть файл с выводом нейросети
    result_file = open(neuro_path + '\\out.txt', 'r')
    # считать файл и разделить его по строкам (":" - конец строки) для HTML
    Result = result_file.read().split(':')
    # переменная для поиска поля в БД
    dbSearch_str = 'data/' + image_name
    # объект поля для HTML
    img = Image.objects.get(image=dbSearch_str)
    # закрыть файл
    result_file.close()
    # открыть файл с помощью pillow, для масштабирования
    pimg = pil_img.open(full_path)
    #   rt = pimg.rotate(90)
    #   rt.save(media_path + '\\data\\' + image_name)
    # получить коефициент для масштабирования
    k = pimg.size[1] / 400
    print(k)
    # задать высоту и ширину изображения для HTML
    hgt = int(pimg.size[1] / k)
    wdt = int(pimg.size[0] / k)
    # приберём за собой с:
    del pimg
    return render(request, 'uploadImage/result.html', locals())
