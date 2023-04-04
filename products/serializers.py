from rest_framework import serializers

from .models import Product, Category, File


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'avatar', 'url')


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('title', 'file', 'file_type')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    foo = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'is_enable',
                  'created_time', 'categories', 'files', 'foo', 'url')

    def get_foo(self, obj):
        return str(obj.id) + ': ' + obj.title
