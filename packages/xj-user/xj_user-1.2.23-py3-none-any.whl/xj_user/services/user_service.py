# _*_coding:utf-8_*_

from datetime import datetime, timedelta
# import os, logging, time, json, copy
import re

# from django.contrib.auth.hashers import make_password
from pathlib import Path
from main.settings import BASE_DIR
from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator
from django.db.models import Q, F
import jwt
# from django.db.models import F
# from rest_framework import exceptions
from rest_framework import serializers

from config.config import Config
from ..models import Auth
from ..models import BaseInfo
from ..utils.j_config import JConfig
from ..utils.j_dict import JDict
from ..utils.model_handle import format_params_handle

module_root = str(Path(__file__).resolve().parent)
# 配置之对象
main_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_user"))
module_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_user"))

app_id = main_config_dict.app_id or module_config_dict.app_id or ""
app_secret = main_config_dict.secret or module_config_dict.secret or ""
jwt_secret_key = main_config_dict.jwt_secret_key or module_config_dict.jwt_secret_key or ""
expire_day = main_config_dict.expire_day or module_config_dict.expire_day or ""
expire_second = main_config_dict.expire_second or module_config_dict.expire_second or ""


class UserInfoSerializer(serializers.ModelSerializer):
    # 方法一：使用SerializerMethodField，并写出get_platform, 让其返回你要显示的对象就行了
    # p.s.SerializerMethodField在model字段显示中很有用。
    # platform = serializers.SerializerMethodField()

    # # 方法二：增加一个序列化的字段platform_name用来专门显示品牌的name。当前前端的表格columns里对应的’platform’列要改成’platform_name’
    user_id = serializers.ReadOnlyField(source='id')
    permission_value = serializers.SerializerMethodField()

    # platform_id = serializers.ReadOnlyField(source='platform.platform_id')
    # platform_name = serializers.ReadOnlyField(source='platform.platform_name')

    class Meta:
        model = BaseInfo
        fields = [
            'user_id',
            # 'platform',
            # 'platform_uid',
            # 'platform__platform_name',
            # 'platform_id',
            # 'platform_name',
            # 'get_group_desc',
            'user_name',
            'full_name',
            'phone',
            'email',
            'wechat_openid',
            'user_info',
            'user_group',
            'user_group_id',
            'permission',
            'permission_value'
        ]
        # exclude = ['platform_uid']

    def get_permission_value(self, instance):
        pass

    # # 这里是调用了platform这个字段拼成了get_platform
    # def get_platform(self, obj):
    #     return obj.platform.platform_name
    #     # return {
    #     #     'id': obj.platform.platform_id,
    #     #     'name': obj.platform.platform_name,
    #     # }


class UserService:
    def __init__(self):
        pass

    # 检测账户
    @staticmethod
    def check_account(account):
        """
        @param account 用户账户，可以支持三种类型：手机、用户名、邮箱。自动判断
        @description 注意：用户名不推荐由纯数字构成，因为那样容易和11位手机号冲突
        """
        # 账号类型判断
        if re.match(r'(^1[356789]\d{9}$)|(^\+?[78]\d{10}$)', account):
            account_type = 'phone'
        elif re.match(r'^\w+[\w\.\-\_]*@\w+[\.\w]*\.\w{2,}$', account):
            account_type = 'email'
        elif re.match(r'^[A-z\u4E00-\u9FA5]+\w*$', account):
            account_type = 'username'
        else:
            return None, "账号必须是用户名、手机或者邮箱，用户名不能是数字开头"

        # 用户ID
        user_list = BaseInfo.objects.filter(Q(user_name=account) | Q(phone=account) | Q(email=account)) \
            .annotate(user_id=F("id")) \
            .annotate(user_group_value=F("user_group__group")) \
            .annotate(permission_value=F("permission__permission_name")) \
            .values(
            'user_id',
            'user_name',
            'full_name',
            'phone',
            'email',
            'wechat_openid',
            'user_info',
            'user_group_id',
            'user_group_value',
            'permission_id',
            'permission_value'
        )
        if not user_list.count():
            return None, "账户不存在"
        if user_list.count() > 1:
            return None, "登录异常，请联系管理员，发现多账号冲突："
        # print("> user_list:", user_list)
        user_set = user_list.first()

        # serializer = UserInfoSerializer(user_set, many=False)
        # print("> serializer:", serializer)
        return user_set, None

    # 验证密码
    @staticmethod
    def check_login(user_id, password, account):
        """
        @param user_id 用户ID
        @param password 用户密码。
        @param account 登陆账号，必填，用于生成Token令牌。
        @description 注意：目前密码是明文传输，今后都要改成密文传输
        """
        auth_set = Auth.objects.filter(user_id=user_id, password__isnull=False).order_by('-update_time').first()
        if not auth_set:
            return None, "账户尚未开通登录服务：" + account + "(" + str(user_id) + ")"

        # 判断密码不正确
        is_pass = check_password(password, auth_set.password)
        if not is_pass:
            return None, "密码错误"

        # print(int(Config.getIns().get('xj_user', 'DAY', 7)))
        # print(Config.getIns().get('xj_user', 'JWT_SECRET_KEY', ""))

        # 过期时间
        # int(Config.getIns().get('xj_user', 'DAY', 7))
        # int(Config.getIns().get('xj_user', 'SECOND', 0))
        expire_timestamp = datetime.utcnow() + timedelta(days=7, seconds=0)
        # 为本次登录生成Token并记录
        # todo 漏洞，当用户修改用户名时，并可能导致account失效，是否存用户ID更好
        token = jwt.encode(payload={'account': account, 'user_id': user_id, "exp": expire_timestamp},
                           key=Config.getIns().get('xj_user', 'JWT_SECRET_KEY', ""))
        # payload = jwt.decode(token, key=Config.getIns().get('xj_user', 'JWT_SECRET_KEY', ""), verify=True, algorithms=["RS256", "HS256"])
        # print("> payload:", payload)
        auth_set.token = token
        auth_set.save()

        return {'token': token}, None

    # 验证密码
    @staticmethod
    def check_login_wechat(user_id, phone):
        """
        @param user_id 用户ID
        @param phone 登陆账号，必填，用于生成Token令牌。
        @description 注意：目前密码是明文传输，今后都要改成密文传输
        """
        auth_set = Auth.objects.filter(user_id=user_id, password__isnull=False).order_by('-update_time').first()
        if not auth_set:
            return None, "账户尚未开通登录服务：" + phone + "(" + str(user_id) + ")"

        # 过期时间
        expire_timestamp = datetime.utcnow() + timedelta(days=int(Config.getIns().get('xj_user', 'DAY', 7)),
                                                         seconds=int(Config.getIns().get('xj_user', 'SECOND', 1)))
        # 为本次登录生成Token并记录
        # todo 漏洞，当用户修改用户名时，并可能导致account失效，是否存用户ID更好
        token = jwt.encode(payload={'account': phone, 'user_id': user_id, "exp": expire_timestamp},
                           key=Config.getIns().get('xj_user', 'JWT_SECRET_KEY'))
        # payload = jwt.decode(token, key=Config.getIns().get('xj_user', 'JWT_SECRET_KEY'), verify=True, algorithms=["RS256", "HS256"])
        # print("> payload:", payload)
        auth_set.token = token
        auth_set.save()

        return {'token': token}, None

    # 验证密码
    @staticmethod
    def check_login_short(user_id, phone):
        """
        @param user_id 用户ID
        @param phone 登陆账号，必填，用于生成Token令牌。
        @description 注意：目前密码是明文传输，今后都要改成密文传输
        """
        auth_set = Auth.objects.filter(user_id=user_id, password__isnull=False).order_by('-update_time').first()
        if not auth_set:
            return None, "账户尚未开通登录服务：" + phone + "(" + str(user_id) + ")"

        # 过期时间
        expire_timestamp = datetime.utcnow() + timedelta(days=int(expire_day),
                                                         seconds=int(expire_second))
        # 为本次登录生成Token并记录
        # todo 漏洞，当用户修改用户名时，并可能导致account失效，是否存用户ID更好
        token = jwt.encode(payload={'account': phone, 'user_id': user_id, "exp": expire_timestamp},
                           key=jwt_secret_key)
        # payload = jwt.decode(token, key=Config.getIns().get('xj_user', 'JWT_SECRET_KEY'), verify=True, algorithms=["RS256", "HS256"])
        # print("> payload:", payload)
        auth_set.token = token
        auth_set.save()

        return {'token': token}, None

    # 检测令牌
    @staticmethod
    def check_token(token):
        """
        @param token 用户令牌。
        @description 注意：用户令牌的载荷体payload中必须包含两个参数：account账号、exp过期时间，其中账号可以是手机、用户名、邮箱三种。
        @description BEARER类型的token是在RFC6750中定义的一种token类型，OAuth2.0协议RFC6749对其也有所提及，算是对RFC6749的一个补充。BEARER类型token是建立在HTTP/1.1版本之上的token类型，需要TLS（Transport Layer Security）提供安全支持，该协议主要规定了BEARER类型token的客户端请求和服务端验证的具体细节。
        @description 理论上，每次请求令牌后就更新一次令牌，以监测用户长期访问时，不至于到时间后掉线反复登陆。
        """
        # 检查是否有Bearer前辍，如有则截取
        # print("> token 1:", token)
        if not token:
            return None, "请登录"  # 缺少Token

        if re.match(r'Bearer(.*)$', token, re.IGNORECASE):
            token = re.match(r'Bearer(.*)$', token, re.IGNORECASE).group(1).strip()
        # print("> token 2:", token)

        if not token:
            return None, "您尚未登录"

        # # 验证token。另一种方式，从数据库核对Token，通过对比服务端的Token，以确定是否为服务器发送的。今后启用该功能。
        # auth_set = Auth.objects.filter(Q(token=token)).order_by('-update_time')
        # # print("> auth:", auth_set)
        # if not auth_set.count():
        #     raise MyApiError('token验证失败', 6002)
        # auth = auth_set.first()

        try:
            # jwt.decode会自动检查exp参数，如果超时则抛出jwt.ExpiredSignatureError超时
            # jwt_payload = jwt.decode(token, key=Config.getIns().get('xj_user', 'JWT_SECRET_KEY'), verify=True, algorithms=["RS256", "HS256"])
            jwt_payload = jwt.decode(token, key=Config.getIns().get('xj_user', 'JWT_SECRET_KEY', '@zxmxy2021!'),
                                     verify=True, algorithms=["RS256", "HS256"])
            # print("> jwt_payload:", jwt_payload)

        except jwt.ExpiredSignatureError:
            return None, "登录已过期，请重新登录"

        except jwt.InvalidTokenError:
            return None, "用户令牌无效，请重新登录"

        account = jwt_payload.get('account', None)
        user_id = jwt_payload.get('user_id', None)
        if not account:
            return {'payload': jwt_payload}, "错误：令牌载荷中未提供用户账户Account"

        # 检测用户令牌时不应该调用用户信息，这会导致任何接口都会查询用户表，时间会增加
        # user_info = UserService.check_account(account=account)

        return {'account': account, 'user_id': user_id}, None

    # 用户信息列表
    @staticmethod
    def user_list(params, need_pagination=True):
        if not need_pagination:
            res_obj = BaseInfo.objects.filter(**params)
            res_data = []
            if res_obj:
                res_data = list(
                    res_obj.values("id", "user_name", "full_name", "nickname", "phone", "email", "wechat_openid"))
            for i in res_data:
                id(i)
                i['is_user'] = True
            return res_data, None
        # params = format_params_handle(
        #     param_dict=params,
        #     filter_filed_list=["page", "size", "user_id", "email", "full_name", "user_name", "nickname", "id_list",
        #                        "wechat_openid"],
        #     alias_dict={
        #         "full_name": "full_name__full_name",
        #         "user_name": "user_name__contains",
        #         "nickname": "nickname__contains",
        #         "id_list": "id__in",
        #         "user_id": params.get('user_id'),
        #         "user_id__in": params.get('user_id__in'),
        #         "user_id__not_in": params.get("user_id__not_in"),
        #
        #
        #     }
        # )
        # conditions = {k: v for k, v in conditions.items() if v or v == []}
        # 需要分页的时候
        page = params.pop("page", 1)
        size = params.pop("size", 20)
        is_admin = params.pop("is_admin", False)
        res_set = BaseInfo.objects
        # 开始按过滤条件
        try:
            res_set = res_set.annotate(user_id=F("id"))
            if is_admin:
                res_set = res_set.filter(**params)
            else:
                has_auth = False
                if params.get("user_id__not_in"):  # 权限判断1
                    has_auth = True
                    res_set = res_set.filter(~Q(user_id__in=params.pop("user_id__not_in")))

                if params.get("user_id__in"):  # 权限判断2
                    has_auth = True
                    res_set = res_set.filter(user_id__in=params.pop("user_id__in"))

                if has_auth:  # token 验证成功
                    res_set = res_set.filter(**params)
                else:  # 没有传token 只允许看不需要权限的信息
                    res_set = res_set.filter(Q(**params) & Q(need_auth=0))

            # res_set = BaseInfo.objects.filter(**params).annotate(user_id=F("id"))
            count = res_set.count()
            res_set = res_set.values(
                "user_id",
                "email",
                "full_name",
                "user_name",
                "nickname",
                "permission_id",
                "user_group_id",
                "wechat_openid",
            )

        except Exception as e:
            return None, "err:" + e.__str__()
        page_set = Paginator(res_set, size).page(page)
        page_list = []
        if page_set:
            page_list = list(page_set.object_list)
        return {'size': int(size), 'page': int(page), 'count': count, 'list': page_list}, None

    # 胡家萍 用户权限判断闭包
    @staticmethod
    def hjp_user_right_call(user_info):
        # map = {1: "集团用户", 2: "村民用户没有权限"}
        try:
            if user_info[0]['user_group'] == 1:
                return True
            else:
                return False
        except Exception as e:
            return False
