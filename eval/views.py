from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Student, AudioFile, Score
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def student_list(request):
    page = request.GET.get('page', '1')  # 페이지
    student_list = Student.objects.order_by('pub_date')
    paginator = Paginator(student_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'student_list': page_obj}
    return render(request, 'eval/student_list.html', context)

def audio_list(request, student_id):
    student_bynum = AudioFile.objects.filter(student_number=student_id)


    for audio_file in student_bynum:
        eval_item_name=audio_file.item_text

    student_num = get_object_or_404(Student, id=student_id)
    student_name = student_num.name

    user_name = request.user.username

    if request.method == 'POST':
        audio_file_id = request.POST['audio_file_id']
        audio_file = get_object_or_404(AudioFile, id=audio_file_id)

        std = Score()
        std.user = request.user
        std.student = student_num
        std.eval_item = audio_file
        std.rating_un = request.POST['rating_un']
        std.rating_fu = request.POST['rating_fu']
        std.rating_ac = request.POST['rating_ac']
        std.rating_ph = request.POST['rating_ph']
        std.rating_accent = request.POST['rating_accent']
        std.rating_rule = request.POST['rating_rule']
        std.rating_speed = request.POST['rating_speed']
        std.rating_pause = request.POST['rating_pause']
        std.save()

    context = {'student_bynum':student_bynum,
               'student_num': student_num, 'student_name': student_name, 'user_name': user_name,
               'eval_item_name': eval_item_name}
    return render(request, 'eval/audio_list.html', context)