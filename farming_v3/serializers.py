from rest_framework import serializers
from farming_v3.models import  PestisidaPupuk, Tanaman, Hama, Panenan
from django.contrib.auth.models import User

# class PetaniSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Petani
#         fields = ('id', 'username','password','nama', 'luas_tanah')
        
class PanenanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panenan
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'hasil_panen', 'berat_ton']
        
class TanamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanaman
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'nama_tanaman', 'jenis', 'waktu_tanam_hari', 'harga_perTon', 'peluang_hama']

class PestisidaPupukSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestisidaPupuk
        fields = ['id', 'jenis', 'nama_obat', 'produsen', 'warna']
        
class HamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hama
        fields = ['id', 'nama_hama', 'rate_bahaya', 'makhluk', 'obat']


# Serializer for table relation panenan --> tanaman, panenan --> petani 
class PanenanDetailSerializer(serializers.ModelSerializer):
    # petani_nama = serializers.CharField(source='petaninya.nama', read_only=True)
    # tanaman_nama = serializers.CharField(source='hasil_panen.nama_tanaman', read_only=True)
    tanaman_nama = serializers.CharField(source='hasil_panen.nama_tanaman', read_only=True)
    waktu_tanam = serializers.IntegerField(source='hasil_panen.waktu_tanam_hari', read_only=True)
    tanggal_panen = serializers.DateTimeField(source='created',  format='%Y-%m-%d %H:%M:%S')
    harga = serializers.IntegerField(source='hasil_panen.harga_perTon', read_only=True)
    total_harga = serializers.SerializerMethodField()
    petani = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Panenan
        fields = ['id','tanggal_panen', 'tanaman_nama', 'waktu_tanam', 'berat_ton','harga', 'total_harga', 'petani']
        
    def get_total_harga(self, obj):
        # Menghitung total pendapatan
        return obj.berat_ton * obj.hasil_panen.harga_perTon

# Serializer for table relation panenan -->- tanaman
class HamaDetailSerializer(serializers.ModelSerializer):
    nama_hama = serializers.CharField( read_only=True)
    
    # source hanya untuk mengambil data dari tabel relasi (relasi ke pestisida pupuk)
    # bukan tabel nys sendiri (hama)
    nama_obat = serializers.CharField(source='obat.nama_obat', read_only=True)
    makhluk = serializers.CharField(read_only=True)
    
    class Meta:
        model = Hama
        fields = ['id', 'nama_hama', 'nama_obat', 'makhluk']
        
        
class UserSerializer(serializers.ModelSerializer):
    panenan = serializers.PrimaryKeyRelatedField(many=True, queryset=Panenan.objects.all())
    tanaman = serializers.PrimaryKeyRelatedField(many=True, queryset=Tanaman.objects.all())
    # pestisida_pupuk = serializers.PrimaryKeyRelatedField(many=True, queryset=PestisidaPupuk.objects.all())
    # hama = serializers.PrimaryKeyRelatedField(many=True, queryset=Hama.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'panenan', 'tanaman']