from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('name',
                  'sport',
                  'date',
                  'end',
                  'distance',)

    def create():
        pass
