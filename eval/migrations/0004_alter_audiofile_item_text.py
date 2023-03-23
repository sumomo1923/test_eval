# Generated by Django 4.1.4 on 2023-03-22 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eval", "0003_rename_eval_items_score_eval_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiofile",
            name="item_text",
            field=models.CharField(
                choices=[
                    ("", ""),
                    ("가구", "가구"),
                    ("가끔", "가끔"),
                    ("가족", "가족"),
                    ("거리", "거리"),
                    ("궤도", "궤도"),
                    ("그것", "그것"),
                    ("기차", "기차"),
                    ("꼬리", "꼬리"),
                    ("꽃", "꽃"),
                    ("끝", "끝"),
                    ("나의 가방", "나의 가방"),
                    ("날씨", "날씨"),
                    ("더워요", "더워요"),
                    ("돈", "돈"),
                    ("뒤", "뒤"),
                    ("뚱뚱하다", "뚱뚱하다"),
                    ("메모", "메모"),
                    ("몰라요", "몰라요"),
                    ("바다", "바다"),
                    ("바쁘다", "바쁘다"),
                    ("밖", "밖"),
                    ("밤", "밤"),
                    ("밥", "밥"),
                    ("비싸다", "비싸다"),
                    ("빠르다", "빠르다"),
                    ("사과", "사과"),
                    ("사랑", "사랑"),
                    ("소개", "소개"),
                    ("숲", "숲"),
                    ("시간", "시간"),
                    ("시키다", "시키다"),
                    ("쓰다", "쓰다"),
                    ("아이", "아이"),
                    ("아프다", "아프다"),
                    ("야구", "야구"),
                    ("얘기", "얘기"),
                    ("어느", "어느"),
                    ("여기", "여기"),
                    ("예약", "예약"),
                    ("오이", "오이"),
                    ("왜냐하면", "왜냐하면"),
                    ("요리", "요리"),
                    ("우산", "우산"),
                    ("웨이터", "웨이터"),
                    ("의자", "의자"),
                    ("이따가", "이따가"),
                    ("이유", "이유"),
                    ("이틀", "이틀"),
                    ("자동차", "자동차"),
                    ("저희", "저희"),
                    ("주말", "주말"),
                    ("진짜", "진짜"),
                    ("찌개", "찌개"),
                    ("친하다", "친하다"),
                    ("크다", "크다"),
                    ("튼튼하다", "튼튼하다"),
                    ("포도", "포도"),
                    ("하나", "하나"),
                    ("할아버지", "할아버지"),
                    ("해외", "해외"),
                    ("회의", "회의"),
                    ("작년에 생일 선물로 받은 신발입니다.", "작년에 생일 선물로 받은 신발입니다."),
                    ("집에 큰 창문이 없어서 답답해요.", "집에 큰 창문이 없어서 답답해요."),
                    ("좋아하는 노래를 듣고 싶으면 이렇게 하세요.", "좋아하는 노래를 듣고 싶으면 이렇게 하세요."),
                    ("오늘은 할 일이 너무 많은데 뭐부터 시작할까요?", "오늘은 할 일이 너무 많은데 뭐부터 시작할까요?"),
                    ("꽃집 앞에서 오 분만 기다릴 수 있어요?", "꽃집 앞에서 오 분만 기다릴 수 있어요?"),
                    ("아침에는 버스보다 지하철이 더 편리해요?", "아침에는 버스보다 지하철이 더 편리해요?"),
                    ("연락처는 이메일 주소를 쓸까요? 전화번호를 쓸까요?", "연락처는 이메일 주소를 쓸까요? 전화번호를 쓸까요?"),
                    ("내일은 도서관에서 같이 공부합시다.", "내일은 도서관에서 같이 공부합시다."),
                    ("새로 나온 음료수 먹어 봤는데 진짜 맛있네!", "새로 나온 음료수 먹어 봤는데 진짜 맛있네!"),
                    ("식당에 갔는데 문을 닫아서 그냥 왔어요. ", "식당에 갔는데 문을 닫아서 그냥 왔어요. "),
                ],
                default="",
                max_length=200,
                verbose_name="평가 단어/문장",
            ),
        ),
    ]
