from django.conf.urls import url
from qa.views import test, mainpg, question, popular

urlpatterns = [
	url(r'^$', mainpg, name='mainpg'),
	url(r'^question/(?P<pk>\d+)/$', question, name='question'),
	url(r'^popular/', popular, name='popular'),
	url(r'^ask/', test, name='test'),
	url(r'^new/', test, name='test'),
	url(r'^login/', test, name='test'),
	url(r'^signup/', test, name='test'),
]
