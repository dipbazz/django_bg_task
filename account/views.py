from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from account.tasks import send_mail_task

from account.forms import SignUpForm

# Create your views here.
class UserSignupView(FormView):
    template_name = "account/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("success_page")

    def form_valid(self, form):
        form = form.save()
        send_mail_task.delay(
            'You have successfully sigedup',
            'Welcome to example.com and enjoy the benefits of using our system.',
            [form.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class SuccessPage(TemplateView):
    template_name = "account/success.html"
