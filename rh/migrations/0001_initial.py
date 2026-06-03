# Generated migration for rh models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('presupuesto_anual', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('jefe_departamento', models.CharField(blank=True, default='', max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('salario_base', models.DecimalField(decimal_places=2, max_digits=12)),
                ('salario_maximo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('requisitos', models.TextField(blank=True, default='')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='puestos', to='rh.departamento')),
            ],
            options={'ordering': ['titulo'], 'verbose_name_plural': 'Puestos'},
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_empleado', models.CharField(max_length=20, unique=True)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=120)),
                ('apellido', models.CharField(max_length=120)),
                ('edad', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, default='', max_length=20)),
                ('direccion', models.TextField(blank=True, default='')),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('salario_actual', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tipo_contrato', models.CharField(choices=[('indefinido', 'Indefinido'), ('temporal', 'Temporal'), ('practicante', 'Practicante'), ('consultor', 'Consultor')], default='indefinido', max_length=20)),
                ('status', models.CharField(choices=[('activo', 'Activo'), ('en_licencia', 'En Licencia'), ('suspendido', 'Suspendido'), ('inactivo', 'Inactivo')], default='activo', max_length=20)),
                ('notas', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='empleados', to='rh.departamento')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='empleados', to='rh.puesto')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinados', to='rh.empleado')),
            ],
            options={'ordering': ['apellido', 'nombre'], 'verbose_name_plural': 'Empleados'},
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.PositiveIntegerField()),
                ('año', models.PositiveIntegerField()),
                ('salario_base', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bono', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('descuentos', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('descuento_aporte_empleado', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('descuento_impuestos', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('salario_neto', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('generada', 'Generada'), ('revisada', 'Revisada'), ('pagada', 'Pagada'), ('anulada', 'Anulada')], default='generada', max_length=20)),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_pago', models.DateTimeField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nóminas', to='rh.empleado')),
            ],
            options={'ordering': ['-año', '-mes'], 'unique_together': {('empleado', 'mes', 'año')}, 'verbose_name_plural': 'Nóminas'},
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('status', models.CharField(choices=[('presente', 'Presente'), ('ausente', 'Ausente'), ('licencia', 'Licencia'), ('retardo', 'Retardo'), ('salida_anticipada', 'Salida Anticipada')], default='presente', max_length=20)),
                ('hora_entrada', models.TimeField(blank=True, null=True)),
                ('hora_salida', models.TimeField(blank=True, null=True)),
                ('minutos_retardo', models.PositiveIntegerField(default=0)),
                ('observaciones', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='asistencias', to='rh.empleado')),
            ],
            options={'ordering': ['-fecha'], 'unique_together': {('empleado', 'fecha')}, 'verbose_name_plural': 'Asistencias'},
        ),
    ]
