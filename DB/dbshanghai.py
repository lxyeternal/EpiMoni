# -*- coding: utf-8 -*-
# @Project ：EpiMoni
# @Time    : 2022/5/5 23:57
# @Author  : honywen
# @FileName: dbshanghai.py
# @Software: PyCharm


from common.model.ShangHaiModel import ShangHaiModel

def addshanghai(lastUpdateTime, sh_confirm, sh_confirm_add, sh_dead, sh_heal, sh_newConfirm, sh_newDead, sh_newHeal, sh_wzz, sh_wzz_add):

    shanghaimodel = ShangHaiModel()
    shanghaimodel.lastUpdateTime = lastUpdateTime
    shanghaimodel.sh_confirm = sh_confirm
    shanghaimodel.sh_confirm_add = sh_confirm_add
    shanghaimodel.sh_dead = sh_dead
    shanghaimodel.sh_heal = sh_heal
    shanghaimodel.sh_newConfirm = sh_newConfirm
    shanghaimodel.sh_newDead = sh_newDead
    shanghaimodel.sh_newHeal = sh_newHeal
    shanghaimodel.sh_wzz = sh_wzz
    shanghaimodel.sh_wzz_add = sh_wzz_add

    shanghaimodel.save()
