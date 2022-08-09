from django.urls import path
from .views import *


urlpatterns = [
    path('', PortalHome.as_view(), name='home'),
    path('commercial/<str:comm_slug>/', CommercialArticleView.as_view(), name='comm_article'),
    path('operations<str:oper_slug>/', OperationsArticleView.as_view(), name='oper_article'),
    path('finance/<str:fin_slug>/', FinancialArticleView.as_view(), name='fin_article'),
    path('accounting/<str:acc_slug>/', AccountingArticleView.as_view(), name='acc_article'),
    path('development/<str:dev_slug>/', DevelopmentArticleView.as_view(), name='dev_article'),
    path('it/<str:it_slug>/', ItArticleView.as_view(), name='it_article'),
    path('personnel/<str:pers_slug>/', PersonnelArticleView.as_view(), name='pers_article'),
    path('marketing/<str:mark_slug>/', MarketingArticleView.as_view(), name='mark_article'),
    path('security/<str:sec_slug>/', SecurityArticleView.as_view(), name='sec_article'),
    path('leaders/', LeaderView.as_view(), name='leaders'),
    
    path('commercial_structure/', CommercialStructureView.as_view(), name='comm_structure'),
    path('oper_structure/', OperationsStructureView.as_view(), name='oper_structure'),
    path('finance_structure/', FinancialStructureView.as_view(), name='fin_structure'),
    path('accounting_structure/', AccountingStructureView.as_view(), name='acc_structure'),
    path('development_structure/', DevelopmentStructureView.as_view(), name='dev_structure'),
    path('it_structure/', ItStructureView.as_view(), name='it_structure'),
    path('personnel_structure/', PersonnelStructureView.as_view(), name='pers_structure'),
    path('marketing_structure/', MarketingStructureView.as_view(), name='mark_structure'),
    path("search/", Search.as_view(), name='search'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
]
