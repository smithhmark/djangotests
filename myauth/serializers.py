from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from myauth.models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                'first_name', 'last_name', 'tagline', 'password',
                'confirm_password',)
        read_only_fields = ('created_at', 'updated_at')

        def create(self, validated_data):
            print("AS:", validated_data)
            return Account.objects.create(**validated_data)

        def update(self, inst, validated_data):
            print("AS2:", validated_data)
            inst.username = validated_data.get('username', inst.username)
            inst.tagline = validated_data.get('tagline', inst.tagline)
            inst.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)
            if password and confirm_password and password == confirm_password:
                inst.set_password(password)
                inst.save()
            update_session_auth_hash(self.context.get('request'), inst)

            return inst

