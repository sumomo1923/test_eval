from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Student, AudioFile, Score, Eval_item
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def student_list(request):
    page = request.GET.get('page', '1')  # 페이지
    item_list = Eval_item.objects.order_by('pub_date')
    paginator = Paginator(item_list, 3)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'item_list': page_obj}
    return render(request, 'eval/student_list.html', context)

def audio_list(request, item_id):

    audio_list = Eval_item.objects.order_by('pub_date')


    item_by_num = get_object_or_404(Eval_item, id=item_id)
    item_by_num2 = Eval_item.objects.filter(id=item_id)
    item_by_num3 = Eval_item.objects.all()

    student_num = get_object_or_404(AudioFile, id=item_id)
    student_num2 = AudioFile.objects.filter(item=item_id)
    student_num3 = AudioFile.objects.all()

    student_num4 = Student.objects.filter(name=item_id)
    student_num5 = get_object_or_404(Student, name=student_num.student_number)

    student_name = student_num.item
    student_obj = student_num.student_number


    paginator = Paginator(audio_list, 5)  # 페이지당 5개씩 보여주기
    page = request.GET.get('page', '1')  # 페이지
    page_obj = paginator.get_page(page)


    for audio_file in student_num2:
        a = audio_file.student_number

    eval_item_type = ''

    for audio_file in student_num2:
        eval_item_type = audio_file.item_type

    eval_item_name = ''
    eval_item_component = ''

    for audio_file in item_by_num2:
        eval_item_name = audio_file.item_text
        eval_item_component = audio_file.item_component

    if request.method == 'POST':
        audio_file_id = request.POST['audio_file_id']
        audio_file = get_object_or_404(AudioFile, id=audio_file_id)

        std = Score()
        std.user = request.user
        std.student = a
        std.eval_item = audio_file
        std.rating_un = request.POST['rating_un']
        std.rating_fu = request.POST['rating_fu']
        std.rating_ac = request.POST['rating_ac']
        std.rating_ph = request.POST.get('rating_ph', 0)
        std.rating_accent = request.POST.get('rating_accent', 0)
        std.rating_rule = request.POST.get('rating_rule', 0)
        std.rating_speed = request.POST.get('rating_speed', 0)
        std.rating_pause = request.POST.get('rating_pause', 0)
        std.save()

    context = {'item_by_num': item_by_num, 'audio_list': page_obj, 'eval_item_component': eval_item_component,
               'item_by_num2': item_by_num2, 'student_num4': student_num4, 'student_num5': student_num5, 'student_num2': student_num2, 'student_num3': student_num3,
               'student_num': student_num, 'student_name': student_name,
               'eval_item_name': eval_item_name, 'item_by_num3': item_by_num3,
               'eval_item_type': eval_item_type, 'a': a}
    return render(request, 'eval/audio_list.html', context)