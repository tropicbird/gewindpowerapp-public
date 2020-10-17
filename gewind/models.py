from django.db import models
import ulid

# Create your models here.

class Color(models.Model):
    color=models.CharField('色',max_length=255,unique=True)
    def __str__(self):
        return self.color

class ProjectInfo(models.Model):
    id=models.CharField(
        default=ulid.new,
        max_length=26,
        primary_key=True,
        editable=False
    )

    proj_id = models.CharField('プロジェクト名', max_length=255, unique=False,help_text='※Google Earth上に表示される名前です。')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name='風車の色',default=8)
    heading=models.IntegerField('風車の向き(0～360)',default=0,help_text='※数字は北（=0）から時計回り（参考：東=90, 南=180, 西=270）')
    hub_height=models.FloatField('ハブ高(m)',default=100)
    blade_length=models.FloatField('ブレードの長さ(m)',default=80,help_text='※値はローター直径ではなく、ローター半径です。')
    created_at=models.DateTimeField('作成日',auto_now_add=True)
    updated_at=models.DateTimeField('更新日',auto_now=True)
    appearance = models.BooleanField('ブレードの回転位置',help_text='※ブレードの回転位置をランダムにする場合はチェックを入れる。')
    paint_it_black = models.BooleanField('バードストライク対策', help_text='※ブレードの一部を黒くする場合はチェックを入れる。',default=False)#10/05

    def __str__(self):
        return self.proj_id

class Coordinates(models.Model):
    turbine_name=models.CharField('風車の名称',max_length=32,blank=True,help_text='a')
    lon=models.FloatField('経度',help_text='a',blank=False)
    lat = models.FloatField('緯度',help_text='a',blank=False)
    export_id = models.ForeignKey(ProjectInfo, on_delete=models.PROTECT, verbose_name='出力ID')

    def __str__(self):
        return self.turbine_name

class Uploadfile(models.Model):
    file = models.FileField('ファイル')
    name = models.CharField('ファイル名',max_length=32,blank=True)

    def __str__(self):
        return self.file.url