from django.views import generic
from django.urls import reverse_lazy

from .forms import MemoCreateForm, MemoUpdateForm
from .models import Memo


class IndexView(generic.TemplateView):
    template_name = "wemo_app/index.html"


class MemoListView(generic.ListView):
    template_name = "wemo_app/memo_list.html"

    def get_queryset(self):
        return Memo.objects.all()


class MemoView(generic.DetailView):
    model = Memo
    template_name = "wemo_app/memo_view.html"


class MemoCreateFormView(generic.edit.FormView):
    template_name = "wemo_app/memo_create.html"
    form_class = MemoCreateForm


class MemoCreateView(generic.edit.CreateView):
    model = Memo
    fields = ("memo_title", "memo_text")
    success_url = reverse_lazy("wemo_app:memo_list")


class MemoUpdateView(generic.edit.UpdateView):
    model = Memo
    form_class = MemoUpdateForm
    template_name = "wemo_app/memo_update.html"
    success_url = reverse_lazy("wemo_app:memo_list")


class CreditView(generic.TemplateView):
    template_name = "wemo_app/credit.html"


class MemoDeleteView(generic.edit.DeleteView):
    model = Memo
    success_url = reverse_lazy("wemo_app:memo_list")


class HelpView(generic.TemplateView):
    template_name = "wemo_app/help.html"
