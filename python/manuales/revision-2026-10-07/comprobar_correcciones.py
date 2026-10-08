"""Pruebas focalizadas del manual; no sustituyen la revisión de todos los ejemplos."""
import contextlib
import copy
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class CorreccionesManual(unittest.TestCase):
    def test_division(self):
        self.assertEqual(-10 // 3, -4)
        self.assertEqual((23 / 5, 23 // 5, 23 % 5), (4.6, 4, 3))
        self.assertIsInstance(10.0 // 3, float)

    def test_bool(self):
        self.assertEqual([bool(x) for x in (0, '', 1, 'False')],
                         [False, False, True, True])

    def test_tuplas(self):
        self.assertIsInstance(('único'), str)
        self.assertIsInstance(('único',), tuple)
        t = ([1],)
        t[0].append(2)
        self.assertEqual(t, ([1, 2],))

    def test_descuento(self):
        precio, descuento = 100, 20
        self.assertEqual(precio * (1 - descuento / 100), 80.0)
        self.assertEqual((precio - descuento) / 100, 0.8)
        self.assertEqual(precio - descuento / 100, 99.8)

    def test_float(self):
        precio = 100
        self.assertEqual(repr(precio * 1.16), '115.99999999999999')
        self.assertEqual(f'{precio * 1.16:.2f}', '116.00')

    def test_capitalize(self):
        mensaje = '  hola MUNDO  '
        self.assertEqual(mensaje.capitalize(), '  hola mundo  ')
        self.assertEqual(mensaje.strip().capitalize(), 'Hola mundo')

    def test_polimorfismo(self):
        class Animal:
            def hablar(self):
                print('Sonido genérico')
        class Perro(Animal):
            def hablar(self):
                return '¡Guau!'
        class Gato:
            def hablar(self): return 'Miau'
        class Vaca:
            def hablar(self): return 'Muu'
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            for animal in [Gato(), Vaca(), Perro()]:
                print(animal.hablar())
        self.assertEqual(out.getvalue(), 'Miau\nMuu\n¡Guau!\n')

    def test_atributos(self):
        class Persona:
            pass
        Persona.nombre = 'Ana'
        p = Persona()
        p.nombre = 'Juan'
        self.assertEqual((Persona.nombre, p.nombre), ('Ana', 'Juan'))

    def test_iterador(self):
        valores = [10, 20]
        with self.assertRaises(TypeError):
            next(valores)
        it = iter(valores)
        self.assertEqual((next(it), next(it)), (10, 20))
        with self.assertRaises(StopIteration):
            next(it)

    def test_copia(self):
        lista = []
        original = [lista, lista]
        nueva = copy.deepcopy(original)
        self.assertIs(nueva[0], nueva[1])
        self.assertIsNot(nueva[0], lista)

    def test_archivos_y_rutas(self):
        with tempfile.TemporaryDirectory() as temp:
            raiz = Path(temp)
            carpeta = raiz / 'script'
            carpeta.mkdir()
            archivo = carpeta / 'datos.txt'
            with archivo.open('w', encoding='utf-8') as f:
                for _ in range(10):
                    f.write('línea\n')
            self.assertEqual(len(archivo.read_text(encoding='utf-8').splitlines()), 10)
            for _ in range(10):
                with archivo.open('w', encoding='utf-8') as f:
                    f.write('última\n')
            self.assertEqual(archivo.read_text(encoding='utf-8'), 'última\n')
            script = carpeta / 'ejemplo.py'
            script.write_text('from pathlib import Path\n'
                              'print(Path("datos.txt").exists())\n'
                              'print((Path(__file__).resolve().parent / "datos.txt").exists())\n')
            r = subprocess.run([sys.executable, str(script)], cwd=raiz,
                               text=True, capture_output=True, check=True)
            self.assertEqual(r.stdout, 'False\nTrue\n')

    def test_sintaxis_antes_de_ejecucion(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            with self.assertRaises(SyntaxError):
                exec('print("NO DEBE APARECER")\nif True print(1)')
        self.assertEqual(out.getvalue(), '')


if __name__ == '__main__':
    print(sys.version)
    unittest.main(verbosity=2)
