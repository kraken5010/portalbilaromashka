from django.shortcuts import render
from itertools import chain
from .models import *

from django.views.generic import ListView, DetailView
from django.views.generic.base import View


class Article:
    """Статьи из всех департаментов"""
    def get_commercial_atricles(self):
        return CommercialArticle.objects.filter(draft=False)

    def get_operations_atricles(self):
        return OperationsArticle.objects.filter(draft=False)

    def get_financial_atricles(self):
        return FinancialArticle.objects.filter(draft=False)

    def get_accounting_category(self):
        """"Категории бухгалтерии"""
        return AccountingCategoryArticle.objects.all()

    def get_accounting_atricles(self):
        return AccountingArticle.objects.filter(draft=False)

    def get_development_atricles(self):
        return DevelopmentArticle.objects.filter(draft=False)

    def get_it_category(self):
        """"Категории IT"""
        return ItCategoryArticle.objects.all()

    def get_it_atricles(self):
        return ItArticle.objects.filter(draft=False)

    def get_personnel_atricles(self):
        return PersonnelArticle.objects.filter(draft=False)

    def get_marketing_atricles(self):
        return MarketingArticle.objects.filter(draft=False)

    def get_security_articles(self):
        return SecurityArticle.objects.filter(draft=False)


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


# Представления статей департаментов #
class PortalHome(Article, Structure, ListView):
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


class CommercialArticleView(Article, ListView):
    model = CommercialArticle
    template_name = 'portal/article/comm_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['commercial'] = CommercialArticle.objects.filter(slug=self.kwargs['comm_slug'], draft=False)
        return context


class OperationsArticleView(Article, ListView):
    model = OperationsArticle
    template_name = 'portal/article/oper_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['operations'] = OperationsArticle.objects.filter(slug=self.kwargs['oper_slug'], draft=False)
        return context


class FinancialArticleView(Article, ListView):
    model = FinancialArticle
    template_name = 'portal/article/fin_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['financial'] = FinancialArticle.objects.filter(slug=self.kwargs['fin_slug'], draft=False)
        return context


class AccountingArticleView(Article, ListView):
    model = AccountingArticle
    template_name = 'portal/article/acc_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounting'] = AccountingArticle.objects.filter(slug=self.kwargs['acc_slug'], draft=False)
        return context


class DevelopmentArticleView(Article, ListView):
    model = DevelopmentArticle
    template_name = 'portal/article/dev_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['development'] = DevelopmentArticle.objects.filter(slug=self.kwargs['dev_slug'], draft=False)
        return context


class ItArticleView(Article, ListView):
    model = ItArticle
    template_name = 'portal/article/it_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['it'] = ItArticle.objects.filter(slug=self.kwargs['it_slug'], draft=False)
        return context


class PersonnelArticleView(Article, ListView):
    model = PersonnelArticle
    template_name = 'portal/article/pers_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['personnel'] = PersonnelArticle.objects.filter(slug=self.kwargs['pers_slug'], draft=False)
        return context


class MarketingArticleView(Article, ListView):
    model = MarketingArticle
    template_name = 'portal/article/mark_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['marketing'] = MarketingArticle.objects.filter(slug=self.kwargs['mark_slug'], draft=False)
        return context


class SecurityArticleView(Article, ListView):
    model = SecurityArticle
    template_name = 'portal/article/security_article.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['security'] = SecurityArticle.objects.filter(slug=self.kwargs['sec_slug'], draft=False)
        return context


# Представления структур департаментов #
class CommercialStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/comm_struct.html'

    def get_queryset(self):
        return CommercialStructure.objects.all()


class OperationsStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/oper_struct.html'

    def get_queryset(self):
        return OperationsStructure.objects.all()


class FinancialStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/fin_struct.html'

    def get_queryset(self):
        return FinancialStructure.objects.all()


class AccountingStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/acc_struct.html'

    def get_queryset(self):
        return AccountingStructure.objects.all()


class DevelopmentStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/dev_struct.html'

    def get_queryset(self):
        return DevelopmentStructure.objects.all()


class ItStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/it_struct.html'

    def get_queryset(self):
        return ItStructure.objects.all()


class PersonnelStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/pers_struct.html'

    def get_queryset(self):
        return PersonnelStructure.objects.all()


class MarketingStructureView(Structure, Article, ListView):
    template_name = 'portal/structure/mark_struct.html'

    def get_queryset(self):
        return MarketingStructure.objects.all()


class LeaderView(Structure, Article, ListView):
    template_name = 'portal/structure/leaders.html'

    def get_queryset(self):
        return Leader.objects.all()


class Search(Article, Structure, ListView):
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


class AddArticle(Article, ListView):
    model = Department
    template_name = 'portal/instrukciya.html'







