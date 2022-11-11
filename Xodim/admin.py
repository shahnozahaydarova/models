from django.contrib import admin
from .models import Rahbarlar
from .models import Professionallar
from .models import Mutaxasislar
from .models import TexnikXodimlar
from .models import Ichshilar
from .models import MalakaliIshchilar


admin.site.register(Rahbarlar)
admin.site.register(Professionallar)
admin.site.register(Mutaxasislar)
admin.site.register(TexnikXodimlar)
admin.site.register(Ichshilar)
admin.site.register(MalakaliIshchilar)