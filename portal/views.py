from django.shortcuts import render
from itertools import chain
from .models import *

from django.views.generic import ListView, DetailView
from django.views.generic.base import View


class Structure:
    """"Структуры департаментов"""
    def get_leaders(self):
        return Leader.objects.all()

    def get_commercial_structure(self):
        return CommercialStructure.objects.all()

    def get_operations_structure(self):
        return OperationsStructure.objects.all()

    def get_financial_structure(self):
        return FinancialStructure.objects.all()

    def get_accounting_structure(self):
        return AccountingStructure.objects.all()

    def get_development_structure(self):
        return DevelopmentStructure.objects.all()

    def get_it_structure(self):
        return ItStructure.objects.all()

    def get_personnel_structure(self):
        return PersonnelStructure.objects.all()

    def get_marketing_structure(self):
        return MarketingStructure.objects.all()


class Sidebar(Structure, ListView):
    template_name = 'include/sidebar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commercial_articles'] = CommercialArticle.objects.filter(draft=False)
        context['operations_articles'] = OperationsArticle.objects.filter(draft=False)
        context['financial_articles'] = FinancialArticle.objects.filter(draft=False)
        context['accounting_categories'] = AccountingCategoryArticle.objects.all()
        context['accounting_articles'] = AccountingArticle.objects.filter(draft=False).select_related('cat')
        context['development_articles'] = DevelopmentArticle.objects.filter(draft=False)
        context['it_articles'] = ItArticle.objects.filter(draft=False).select_related('cat')
        context['it_categories'] = ItCategoryArticle.objects.all()
        context['personnel_articles'] = PersonnelArticle.objects.filter(draft=False)
        context['marketing_articles'] = MarketingArticle.objects.filter(draft=False)
        context['security_articles'] = SecurityArticle.objects.filter(draft=False)
        return context


# Представления статей департаментов #
class PortalHome(Sidebar, Structure, ListView):
    template_name = 'portal/home.html'
    paginate_by = 8

    def get_queryset(self):
        query_sets = []
        query_sets.append(CommercialArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(OperationsArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(FinancialArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(AccountingArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(ItArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(PersonnelArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(DevelopmentArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(MarketingArticle.objects.filter(draft=False).select_related('dep'))
        query_sets.append(SecurityArticle.objects.filter(draft=False).select_related('dep'))

        final_set = list(chain(*query_sets))
        final_set.sort(key=lambda x: x.time_create, reverse=True)

        final_set = final_set

        return final_set


class CommercialArticleView(Sidebar, ListView):
    model = CommercialArticle
    template_name = 'portal/article/comm_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['commercial'] = CommercialArticle.objects.filter(slug=self.kwargs['comm_slug'], draft=False)
        return context


class OperationsArticleView(Sidebar, ListView):
    model = OperationsArticle
    template_name = 'portal/article/oper_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['operations'] = OperationsArticle.objects.filter(slug=self.kwargs['oper_slug'], draft=False)
        return context


class FinancialArticleView(Sidebar, ListView):
    model = FinancialArticle
    template_name = 'portal/article/fin_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['financial'] = FinancialArticle.objects.filter(slug=self.kwargs['fin_slug'], draft=False)
        return context


class AccountingArticleView(Sidebar, ListView):
    model = AccountingArticle
    template_name = 'portal/article/acc_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounting'] = AccountingArticle.objects.filter(slug=self.kwargs['acc_slug'], draft=False)
        return context


class DevelopmentArticleView(Sidebar, ListView):
    model = DevelopmentArticle
    template_name = 'portal/article/dev_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['development'] = DevelopmentArticle.objects.filter(slug=self.kwargs['dev_slug'], draft=False)
        return context


class ItArticleView(Sidebar, ListView):
    model = ItArticle
    template_name = 'portal/article/it_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['it'] = ItArticle.objects.filter(slug=self.kwargs['it_slug'], draft=False)
        return context


class PersonnelArticleView(Sidebar, ListView):
    model = PersonnelArticle
    template_name = 'portal/article/pers_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['personnel'] = PersonnelArticle.objects.filter(slug=self.kwargs['pers_slug'], draft=False)
        return context


class MarketingArticleView(Sidebar, ListView):
    model = MarketingArticle
    template_name = 'portal/article/mark_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['marketing'] = MarketingArticle.objects.filter(slug=self.kwargs['mark_slug'], draft=False)
        return context


class SecurityArticleView(Sidebar, ListView):
    model = SecurityArticle
    template_name = 'portal/article/security_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['security'] = SecurityArticle.objects.filter(slug=self.kwargs['sec_slug'], draft=False)
        return context


# Представления структур департаментов #
class CommercialStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/comm_struct.html'

    def get_queryset(self):
        return CommercialStructure.objects.all()


class OperationsStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/oper_struct.html'

    def get_queryset(self):
        return OperationsStructure.objects.all()


class FinancialStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/fin_struct.html'

    def get_queryset(self):
        return FinancialStructure.objects.all()


class AccountingStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/acc_struct.html'

    def get_queryset(self):
        return AccountingStructure.objects.all()


class DevelopmentStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/dev_struct.html'

    def get_queryset(self):
        return DevelopmentStructure.objects.all()


class ItStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/it_struct.html'

    def get_queryset(self):
        return ItStructure.objects.all()


class PersonnelStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/pers_struct.html'

    def get_queryset(self):
        return PersonnelStructure.objects.all()


class MarketingStructureView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/mark_struct.html'

    def get_queryset(self):
        return MarketingStructure.objects.all()


class LeaderView(Sidebar, Structure, ListView):
    template_name = 'portal/structure/leaders.html'

    def get_queryset(self):
        return Leader.objects.all()


class Search(Sidebar, Structure, ListView):
    """"Поиск статей по заголовку"""
    template_name = 'portal/search.html'

    def get_queryset(self):

        query_sets = []

        q = self.request.GET.get('q')
        if q != None and q != '':
            query_sets.append(CommercialArticle.objects.filter(title__iregex=q))
            query_sets.append(OperationsArticle.objects.filter(title__iregex=q))
            query_sets.append(FinancialArticle.objects.filter(title__iregex=q))
            query_sets.append(AccountingArticle.objects.filter(title__iregex=q))
            query_sets.append(ItArticle.objects.filter(title__iregex=q))
            query_sets.append(MarketingArticle.objects.filter(title__iregex=q))
            query_sets.append(PersonnelArticle.objects.filter(title__iregex=q))
            query_sets.append(DevelopmentArticle.objects.filter(title__iregex=q))
            query_sets.append(SecurityArticle.objects.filter(title__iregex=q))

            return list(chain(*query_sets))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        return context


class AddArticle(Sidebar, ListView):
    """Страница инструкции по добавлению статей"""
    model = Department
    template_name = 'portal/instrukciya.html'







