from DB.continents import querycontinents
from app import get_logger, get_config
import math
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import utils
from . import main
from ..controller.indexdata import cntotaldata, cnzhexian, cnpeidata, cnstorecf, cnhealrate
from ..controller.maincountries import gettrenddata
from ..controller.nationmap import getnationmap
from ..controller.opshnews import get_shnews
from ..controller.predict import predict_maincountries, predict_sh
from ..controller.rankcountry import getrankdata
from ..controller.shanghai import get_shzhexain, get_totaldata, get_peidata, shrate
from ..controller.worldmap import getworldmap

logger = get_logger(__name__)
cfg = get_config()

# 通用列表查询
def common_list(DynamicModel, view):
    # 接收参数
    action = request.args.get('action')
    id = request.args.get('id')
    page = int(request.args.get('page')) if request.args.get('page') else 1
    length = int(request.args.get('length')) if request.args.get('length') else cfg.ITEMS_PER_PAGE

    # 删除操作
    if action == 'del' and id:
        try:
            DynamicModel.get(DynamicModel.id == id).delete_instance()
            flash('删除成功')
        except:
            flash('删除失败')

    # 查询列表
    query = DynamicModel.select()
    total_count = query.count()

    # 处理分页
    if page: query = query.paginate(page, length)

    dict = {'content': utils.query_to_list(query), 'total_count': total_count,
            'total_page': math.ceil(total_count / length), 'page': page, 'length': length}
    return render_template(view, form=dict, current_user=current_user)


# 通用单模型查询&新增&修改
def common_edit(DynamicModel, form, view):
    id = request.args.get('id', '')
    if id:
        # 查询
        model = DynamicModel.get(DynamicModel.id == id)
        if request.method == 'GET':
            utils.model_to_form(model, form)
        # 修改
        if request.method == 'POST':
            if form.validate_on_submit():
                utils.form_to_model(form, model)
                model.save()
                flash('修改成功')
            else:
                utils.flash_errors(form)
    else:
        # 新增
        if form.validate_on_submit():
            model = DynamicModel()
            utils.form_to_model(form, model)
            model.save()
            flash('保存成功')
        else:
            utils.flash_errors(form)
    return render_template(view, form=form, current_user=current_user)


# 根目录跳转
@main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


# 首页
@main.route('/index', methods=['GET'])
@login_required
def index():
    today_data = cntotaldata()
    date_list,cnzhexain_data = cnzhexian()
    cnpie_names, cnpie_list = cnpeidata()
    cnstoreconfirm_list = cnstorecf()
    cnhealrate_list, cndeadrate_list = cnhealrate()
    return render_template('index.html', today_data=today_data,date_list=date_list, cnzhexain_data=cnzhexain_data,cnpie_names=cnpie_names, cnpie_list=cnpie_list, cnstoreconfirm_list=cnstoreconfirm_list,cnhealrate_list=cnhealrate_list, cndeadrate_list=cndeadrate_list, current_user=current_user)


# 全球疫情地图
@main.route('/globalmap', methods=['GET'])
@login_required
def globalmap():
    worldmap_data, world_name_list, world_confirm_list, world_storeconfirm_list = getworldmap()
    return render_template('global_map.html',worldmap_data=worldmap_data, world_name_list=world_name_list, world_confirm_list=world_confirm_list, world_storeconfirm_list=world_storeconfirm_list,  current_user=current_user)


# 全国疫情地图
@main.route('/nationmap', methods=['GET'])
@login_required
def nationmap():
    nationmap_data, provinces_name_list, provinces_confirm_list, provinces_storeconfirm_list,maxvalue = getnationmap()
    return render_template('nation_map.html', nationmap_data=nationmap_data, provinces_name_list=provinces_name_list, provinces_confirm_list=provinces_confirm_list, provinces_storeconfirm_list=provinces_storeconfirm_list, maxvalue=maxvalue, current_user=current_user)


# 全球疫情区域分析
@main.route('/global_region', methods=['GET'])
@login_required
def global_region():
    continents_dead_list, continents_heal_list, continents_confirm_list, continents_addconfirm_list = querycontinents()
    return render_template('global_region.html', continents_dead_list=continents_dead_list, continents_heal_list=continents_heal_list, continents_confirm_list=continents_confirm_list, continents_addconfirm_list=continents_addconfirm_list,current_user=current_user)


# 重点国家疫情排行
@main.route('/rank_countries', methods=['GET'])
@login_required
def rank_countries():
    storeconfirm_top10, confirm_top10, dead_top10, heal_top10 = getrankdata()
    return render_template('rankmaincountry.html',storeconfirm_top10=storeconfirm_top10, confirm_top10=confirm_top10, dead_top10=dead_top10, heal_top10=heal_top10,  current_user=current_user)


# 重点国家疫情趋势分析
@main.route('/trend_countries', methods=['GET'])
@login_required
def trend_countries():
    date_list, trend_storeconfirm, trend_confirm, trend_heal, trend_dead = gettrenddata()
    return render_template('trendmaincountry.html',date_list=date_list, trend_storeconfirm=trend_storeconfirm, trend_confirm=trend_confirm, trend_heal=trend_heal, trend_dead=trend_dead, current_user=current_user)


# 重点地区疫情分析
@main.route('/main_city', methods=['GET'])
@login_required
def main_city():
    date_list, zhexain_data = get_shzhexain()
    today_total_storeconfirm,today_total_confirm,today_total_dead,today_total_heal,today_new_storeconfirm,today_new_confirmadd,today_new_dead,today_new_heal = get_totaldata()
    sh_pei_list = get_peidata()
    sh_news_list = get_shnews()
    shhealrate_list, shdeadrate_list = shrate()
    return render_template('maincity.html',shhealrate_list=shhealrate_list, shdeadrate_list=shdeadrate_list,sh_news_list=sh_news_list, date_list=date_list, zhexain_data=zhexain_data,today_total_storeconfirm=today_total_storeconfirm,today_total_confirm=today_total_confirm,today_total_dead=today_total_dead,today_total_heal=today_total_heal,today_new_storeconfirm=today_new_storeconfirm,today_new_confirmadd=today_new_confirmadd,today_new_dead=today_new_dead,today_new_heal=today_new_heal,sh_pei_list=sh_pei_list, current_user=current_user)


# 境外输入分析
@main.route('/from_aboard', methods=['GET'])
@login_required
def from_aboard():
    return render_template('fromaboard.html', current_user=current_user)


# 疫情发展趋势预测
@main.route('/predict', methods=['GET'])
@login_required
def predict():
    sh_month_future_date, sh_month_future_confirm = predict_sh()
    uk_month_future_date, uk_month_future_confirm = predict_maincountries('uk')
    france_month_future_date, france_month_future_confirm = predict_maincountries('france')
    germany_month_future_date, germany_month_future_confirm = predict_maincountries('france')
    return render_template('predict.html',germany_month_future_date=germany_month_future_date, germany_month_future_confirm=germany_month_future_confirm,sh_month_future_date=sh_month_future_date, sh_month_future_confirm=sh_month_future_confirm,uk_month_future_date=uk_month_future_date, uk_month_future_confirm=uk_month_future_confirm, france_month_future_date=france_month_future_date, france_month_future_confirm=france_month_future_confirm,current_user=current_user)
