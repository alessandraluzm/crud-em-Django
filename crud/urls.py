from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('cadastro/', views.CadastroProdutoView.as_view(), name='cadastro'),
    path('produtos/', views.ListaProdutoView.as_view(), name='produtos'),
    path('edita/<int:pk>/', views.UpdateProdutoView.as_view(), name='edita'),
    path('deleta/<int:pk>/', views.DeletaProdutoView.as_view(), name='deleta'),
    path('logout/', views.Logout.as_view(), name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)