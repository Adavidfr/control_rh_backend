# rh/tests/test_basic.py
from django.test import TestCase
from django.contrib.auth.models import User
from rh.models import Departamento, Puesto, Empleado, Nomina, Asistencia
from datetime import date, time


class DepartamentoTestCase(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(
            code='TI',
            nombre='Tecnología de la Información',
            jefe_departamento='Juan García'
        )

    def test_departamento_creation(self):
        self.assertEqual(self.departamento.nombre, 'Tecnología de la Información')
        self.assertEqual(self.departamento.code, 'TI')


class PuestoTestCase(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(
            code='TI',
            nombre='Tecnología de la Información'
        )
        self.puesto = Puesto.objects.create(
            code='DEV001',
            titulo='Desarrollador Python',
            salario_base=1500.00,
            salario_maximo=2500.00,
            departamento=self.departamento
        )

    def test_puesto_creation(self):
        self.assertEqual(self.puesto.titulo, 'Desarrollador Python')
        self.assertEqual(self.puesto.salario_promedio, 2000.00)


class EmpleadoTestCase(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(
            code='TI',
            nombre='Tecnología de la Información'
        )
        self.puesto = Puesto.objects.create(
            code='DEV001',
            titulo='Desarrollador Python',
            salario_base=1500.00,
            salario_maximo=2500.00,
            departamento=self.departamento
        )
        self.empleado = Empleado.objects.create(
            numero_empleado='EMP001',
            cedula='1234567890',
            nombre='Carlos',
            apellido='López',
            edad=30,
            email='carlos@example.com',
            fecha_nacimiento=date(1994, 5, 15),
            fecha_ingreso=date(2020, 1, 1),
            salario_actual=1800.00,
            puesto=self.puesto,
            departamento=self.departamento
        )

    def test_empleado_creation(self):
        self.assertEqual(self.empleado.nombre_completo, 'Carlos López')
        self.assertGreater(self.empleado.dias_en_empresa, 0)


class NominaTestCase(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(
            code='TI',
            nombre='Tecnología de la Información'
        )
        self.puesto = Puesto.objects.create(
            code='DEV001',
            titulo='Desarrollador Python',
            salario_base=1500.00,
            salario_maximo=2500.00,
            departamento=self.departamento
        )
        self.empleado = Empleado.objects.create(
            numero_empleado='EMP001',
            cedula='1234567890',
            nombre='Carlos',
            apellido='López',
            edad=30,
            email='carlos@example.com',
            fecha_nacimiento=date(1994, 5, 15),
            fecha_ingreso=date(2020, 1, 1),
            salario_actual=1800.00,
            puesto=self.puesto,
            departamento=self.departamento
        )
        self.nomina = Nomina.objects.create(
            empleado=self.empleado,
            mes=6,
            año=2024,
            salario_base=1800.00,
            bono=100.00,
            descuentos=50.00,
            salario_neto=1850.00
        )

    def test_nomina_creation(self):
        self.assertEqual(self.nomina.periodo, 'Junio 2024')
        self.assertEqual(self.nomina.bruto, 1900.00)


class AsistenciaTestCase(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(
            code='TI',
            nombre='Tecnología de la Información'
        )
        self.puesto = Puesto.objects.create(
            code='DEV001',
            titulo='Desarrollador Python',
            salario_base=1500.00,
            salario_maximo=2500.00,
            departamento=self.departamento
        )
        self.empleado = Empleado.objects.create(
            numero_empleado='EMP001',
            cedula='1234567890',
            nombre='Carlos',
            apellido='López',
            edad=30,
            email='carlos@example.com',
            fecha_nacimiento=date(1994, 5, 15),
            fecha_ingreso=date(2020, 1, 1),
            salario_actual=1800.00,
            puesto=self.puesto,
            departamento=self.departamento
        )
        self.asistencia = Asistencia.objects.create(
            empleado=self.empleado,
            fecha=date.today(),
            status='presente',
            hora_entrada=time(8, 0),
            hora_salida=time(17, 0)
        )

    def test_asistencia_creation(self):
        self.assertEqual(self.asistencia.es_presente, True)
        self.assertEqual(self.asistencia.horas_trabajadas, 9.0)
