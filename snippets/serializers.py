# snippets/serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICE

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    DRF의 ModelSerializer를 확장하여 SnippetSerializer
    모델을 사용하는 클래스를 만들고 테이블 필드를 출력한다.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html'
    )

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos',
            'language', 'style', 'owner',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
