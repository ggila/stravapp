from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('sport',
                  'date',
                  'end',
                  'distance',)

    def create():
        pass
