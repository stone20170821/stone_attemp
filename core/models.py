#! encoding:utf-8
from django.db import models


# Create your models here.


# class HorseBasicBackup(models.Model):
#     """
#     股票列表的备份表，每次更新之后，可以把就的数据备份一次。
#     原因：因为包含了股东人数，所以怀疑是不是这个表会经常的变化？那是不是有必要保存一个history ？
#     """
#     code = models.CharField(max_length=10, verbose_name='代码')
#     name = models.CharField(max_length=20, verbose_name='名称')
#     industry = models.CharField(max_length=50, verbose_name='所属行业')
#     area = models.CharField(max_length=50, verbose_name='地区')
#     pe = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='市盈率')
#     outstanding = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='流通股本（亿）')
#     totals = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='总股本（亿）')
#     total_assets = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='总资产（万）')
#     liquid_assets = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='流动资产')
#     fix_assets = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='固定资产')
#     reversed = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='公积金')
#     reversed_per_share = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='每股公积金')
#     esp = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='每股收益')
#     bvps = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='每股')
#     pb = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='市净率')
#     timeToMarket = models.BigIntegerField(verbose_name='上市日期')
#     updp = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='未分利润')
#     perupdp = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='每股未分')
#     rev = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='收入同比（%）')
#     profit = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='利润同比（%）')
#     gpr = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='毛利率（%）')
#     npr = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='净利润率（%）')
#     holders = models.BigIntegerField(verbose_name='股东人数')
#
#     class Meta:
#         verbose_name = '股票列表备份'


class HorseBasicTemp(models.Model):
    """
    股票列表的临时表，只是用来测试的
    """
    code = models.CharField(max_length=10, verbose_name='代码')
    name = models.CharField(max_length=20, verbose_name='名称')
    industry = models.CharField(max_length=50, verbose_name='所属行业')
    area = models.CharField(max_length=50, verbose_name='地区')
    pe = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='市盈率')
    outstanding = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='流通股本（亿）')
    totals = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='总股本（亿）')
    total_assets = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='总资产（万）')
    liquid_assets = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='流动资产')
    fix_assets = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='固定资产')
    reversed = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='公积金')
    reversed_per_share = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='每股公积金')
    esp = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='每股收益')
    bvps = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='每股')
    pb = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='市净率')
    timeToMarket = models.BigIntegerField(verbose_name='上市日期')
    updp = models.DecimalField(max_digits=14, decimal_places=4, verbose_name='未分利润')
    perupdp = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='每股未分')
    rev = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='收入同比（%）')
    profit = models.DecimalField(max_digits=9, decimal_places=4, verbose_name='利润同比（%）')
    gpr = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='毛利率（%）')
    npr = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='净利润率（%）')
    holders = models.BigIntegerField(verbose_name='股东人数')

    class Meta:
        verbose_name = '股票列表临时'



