# Generated by Django 4.2 on 2023-06-16 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(unique=True)),
                ('gmail', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=20)),
                ('avatar', models.ImageField(upload_to='avatar/archivos')),
                ('ubicacion', models.CharField(max_length=70)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_profesor', models.BooleanField(default=False)),
                ('is_registro', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarrerasModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pemsum', models.FileField(upload_to='pemsun/')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
        ),
        migrations.CreateModel(
            name='DirectorModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_reverce', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'director',
                'verbose_name_plural': 'directores',
            },
        ),
        migrations.CreateModel(
            name='EscuelasModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portada/')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('carreras', models.ManyToManyField(blank=True, related_name='carreras_reverce', to='users.carrerasmodels')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_reverce', to='users.directormodels')),
            ],
            options={
                'verbose_name': 'escuela',
                'verbose_name_plural': 'escuelas',
            },
        ),
        migrations.CreateModel(
            name='EstudiantesModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rango', models.CharField(blank=True, max_length=50, null=True)),
                ('cedula', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrera_estudiante_revercs', to='users.carrerasmodels')),
                ('escuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='escuela_estudent', to='users.escuelasmodels')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_estudiantes_reverce', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'estudiante',
                'verbose_name_plural': 'estudiantes',
            },
        ),
        migrations.CreateModel(
            name='MateriasModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=20)),
                ('credito', models.PositiveIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrera_materia_reverce', to='users.carrerasmodels')),
            ],
            options={
                'verbose_name': 'materias',
            },
        ),
        migrations.CreateModel(
            name='SemestreModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semestre_carrera', to='users.carrerasmodels')),
                ('materia', models.ManyToManyField(related_name='materia_semestres', to='users.materiasmodels')),
            ],
            options={
                'verbose_name': 'semestre',
                'verbose_name_plural': 'semestres',
            },
        ),
        migrations.CreateModel(
            name='SecionModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('estudiante', models.ManyToManyField(blank=True, related_name='estudiante_secion_reverce', to='users.estudiantesmodels')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cesion_reverce', to='users.materiasmodels')),
            ],
            options={
                'verbose_name': 'secion',
                'verbose_name_plural': 'seciones',
            },
        ),
        migrations.CreateModel(
            name='ProfesoresModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rango', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesor_user_reverce', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profesore',
                'verbose_name_plural': 'profesores',
            },
        ),
        migrations.CreateModel(
            name='Notamodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('estudiate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estudiante_nota_reverce', to='users.estudiantesmodels')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nota_reverce', to='users.materiasmodels')),
            ],
            options={
                'verbose_name': 'nota',
                'verbose_name_plural': 'notas',
            },
        ),
        migrations.AddField(
            model_name='materiasmodels',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materia_reverce', to='users.profesoresmodels'),
        ),
        migrations.AddField(
            model_name='materiasmodels',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materia_semestre_reverce', to='users.semestremodels'),
        ),
        migrations.CreateModel(
            name='HistorialEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_basico', models.CharField(blank=True, max_length=50, null=True)),
                ('institucion_escuelas_basico', models.CharField(blank=True, max_length=50, null=True)),
                ('lugar_basico', models.CharField(blank=True, max_length=50, null=True)),
                ('finalizacion_basico', models.DateField()),
                ('grado_basico', models.CharField(blank=True, max_length=15, null=True)),
                ('nivel_bachiller', models.CharField(blank=True, max_length=50, null=True)),
                ('institucion_escuelas_bachiller', models.CharField(blank=True, max_length=50, null=True)),
                ('lugar_bachiller', models.CharField(blank=True, max_length=50, null=True)),
                ('finalizacion_bachiller', models.DateField()),
                ('grado_bachiller', models.CharField(blank=True, max_length=15, null=True)),
                ('nivel_uni', models.CharField(blank=True, max_length=50, null=True)),
                ('institucion_escuelas_uni', models.CharField(blank=True, max_length=50, null=True)),
                ('lugar_uni', models.CharField(blank=True, max_length=50, null=True)),
                ('finalizacion_uni', models.DateField()),
                ('grado_uni', models.CharField(blank=True, max_length=15, null=True)),
                ('estudiante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='historia_educativo_reverce', to='users.estudiantesmodels')),
            ],
            options={
                'verbose_name': 'historial educativo',
                'verbose_name_plural': 'historial educativos',
            },
        ),
        migrations.AddField(
            model_name='escuelasmodels',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, related_name='estudiantes_reverce', to='users.estudiantesmodels'),
        ),
        migrations.AddField(
            model_name='escuelasmodels',
            name='profesores',
            field=models.ManyToManyField(blank=True, related_name='profesores_reverce', to='users.profesoresmodels'),
        ),
        migrations.CreateModel(
            name='DatosSiEsMilitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rango', models.CharField(blank=True, max_length=35, null=True)),
                ('institucion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_ingreso', models.DateField()),
                ('ultimo_asenso', models.DateField()),
                ('nombre_liceo', models.CharField(max_length=45)),
                ('sector_educativo', models.CharField(choices=[('P', 'PUBLICO'), ('PR', 'PRIVADO')], max_length=10)),
                ('idiomas_dominas', models.CharField(choices=[('español', 'ESPAÑOL'), ('ingles', 'INGLES'), ('otros', 'OTROS')], max_length=10)),
                ('estudiante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Datos_militar_reverce', to='users.estudiantesmodels')),
            ],
            options={
                'verbose_name': 'Datos Del Militar',
                'verbose_name_plural': 'Datos Del Militar',
            },
        ),
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siglas_escuela', models.CharField(blank=True, max_length=75, null=True)),
                ('promocion', models.CharField(blank=True, max_length=75, null=True)),
                ('matricula', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('Secion', models.CharField(max_length=35)),
                ('estado_civil', models.CharField(choices=[('s', 'SOLTERO'), ('c', 'CASADO'), ('u', 'UNION LIBRE')], max_length=20)),
                ('no_cedula', models.CharField(max_length=15)),
                ('telefono_res', models.CharField(blank=True, max_length=20, null=True)),
                ('direcion', models.CharField(max_length=150)),
                ('celular', models.CharField(max_length=20)),
                ('telefono_ofic', models.CharField(blank=True, max_length=20, null=True)),
                ('lugar_trabajo', models.CharField(max_length=75)),
                ('alguna_discapasidad', models.CharField(max_length=20)),
                ('tipo_sangre', models.CharField(max_length=25)),
                ('funcion_desenpeña', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('alergico', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('m', 'MASCULINO'), ('f', 'FEMENINO')], max_length=20)),
                ('militar', models.BooleanField(default=True)),
                ('estudiante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Datos_personales_reverce', to='users.estudiantesmodels')),
            ],
            options={
                'verbose_name': 'Datos Personale',
                'verbose_name_plural': 'Datos Personales',
            },
        ),
        migrations.CreateModel(
            name='DatosFamiliares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('padre', models.CharField(blank=True, max_length=50, null=True)),
                ('madre', models.CharField(blank=True, max_length=50, null=True)),
                ('esposa', models.CharField(blank=True, max_length=50, null=True)),
                ('hijos', models.CharField(blank=True, max_length=75, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('contacto_emergencia', models.CharField(blank=True, max_length=70, null=True)),
                ('estudiante', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='datos_familiares_reverce', to='users.estudiantesmodels')),
            ],
            options={
                'verbose_name': 'Datos De la familia',
                'verbose_name_plural': 'Datos De las familia',
            },
        ),
        migrations.AddField(
            model_name='carrerasmodels',
            name='materias',
            field=models.ManyToManyField(blank=True, related_name='materia_carreras_reverce', to='users.materiasmodels'),
        ),
    ]
