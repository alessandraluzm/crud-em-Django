from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse
from crud.models import Produto


class CadastroProdutoView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'cadastro.html'
    fields = ['nome','preco','descricao','categoria']
    # Passando o nome da url para redirecionamento caso o usuário não esteja logado
    login_url = 'login'

    def get_success_url(self):
        return reverse('produtos')


class ListaProdutoView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produtos.html'
    login_url = 'login'

    def get_queryset(self):
        result = super(ListaProdutoView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            return result.filter(categoria__nome__iexact=query) | result.filter(nome__icontains=query)
        else:
            return result

class UpdateProdutoView(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = 'edita.html'
    fields = ['nome', 'preco', 'descricao', 'categoria']
    login_url = 'login'

    def get_success_url(self):
        return reverse('produtos')


class DeletaProdutoView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Produto
    template_name = 'deleta.html'

    def get_success_url(self):
        return reverse('produtos')


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('produtos')


class Logout(LogoutView):

    def get_next_page(self):
        return reverse('login')
